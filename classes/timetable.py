import csv
import math
import os

import numpy as np

from classes import classroom as cla
from classes import course as crs
from classes import empty as emp
from classes import lecture as lec
from classes import restricted as res
from helpers import objective


class Timetable:
    def __init__(self):
        """ Timetable Class.

        Constructs timetable class which holds the grid, list of courses and
        classrooms. Grid is filled with Empty and Restricted objects.

        Attributes:
            grid (numpy.ndarray): 3d-array containing lectures.
            courses [Course]: List of Course objects.
            classrooms [Classroom]: List of Classroom objects.
            objective_score (int): Total score of the timetabl (Default -1500).

        Methods:
            find_lecture: Finds Lecture object for id.
            find_course: Finds Course object for course name.
            find_slot: Finds the slot corresponding to a lecture.
            sort_courses: Sorts courses based on their points.
            make_courses: Fills courses attribute with Course objects.
            make_classrooms: Fills classrooms attribute with Classroom objects.
            make_lectures: Makes all lectures from the Course objects.
            add_restricted: Fills restricted attribute for all Course objects.
            check_restriction: Checks if restricted lectures overlap in a slot.
            check_order: Checks the order of course lectures.
            fill_nightslots: Fills unavailable slots with Restricted objects

        """

        self.grid = np.full((7, 5, 5), emp.Empty(), dtype=object)
        self.courses = []
        self.classrooms = []
        self.make_courses()
        self.make_lectures()
        self.make_classrooms()
        self.add_restricted()
        self.fill_nightslots()
        self.objective_score = -1500

    def find_lecture(self, _id):
        """ Returns the Lecture object with a certain ID (int). """

        for course in self.courses:
            for lecture in course.lectures:
                if lecture.id == _id:
                    return lecture

    def find_course(self, name):
        """ Returns the Course objects with a certain name (str). """

        if name == "empty":
            return emp.Empty()

        for course in self.courses:
            if course.name == name:
                return course

    def find_slot(self, lecture):
        """ Returns the classroom, day and slot of a lecture in the grid.

        Arguments:
            lecture (Lecture): Lecture from the grid.

        Returns:
            coordinates [[classroom (int), day (int), slot (int)]] if lecture
            is in grid, empty list otherwise.

        """

        coordinates = np.argwhere(self.grid == lecture)
        return coordinates

    def sort_courses(self):
        """ Sorts list of courses based on their points from high to low. """

        self.courses.sort(key=lambda course: course.points, reverse=True)

    def make_courses(self):
        """" Fills list of courses with Course objects made from data file. """

        relative_path = os.path.dirname(os.path.abspath("main.py"))
        absolute_path = os.path.join(relative_path, "data", "courses.csv")

        with open(absolute_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line = 0
            courses = []

            # Loops over all lines in csv file
            for row in csv_reader:
                courses.append(row[0])

        for course in courses:
            self.courses.append(crs.Course(course))

    def make_classrooms(self):
        """ Fills list of classrooms with Classroom objects from data file. """

        relative_path = os.path.dirname(os.path.abspath("main.py"))
        absolute_path = os.path.join(relative_path, "data", "classroom.csv")

        with open(absolute_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line = 0
            classrooms = []

            # Loops over all lines in csv file
            for row in csv_reader:
                classrooms.append(row)

        for classroom in classrooms:
            self.classrooms.append(cla.Classroom(classroom[0],
                                   int(classroom[1])))

    def make_lectures(self):
        """ Makes all needed lectures from list of courses.

        Creates Lecture objects for every course. Creates seperate lectures
        when student number exceeds the capacity. Werkcollege and Practicum
        objects are assigned in tracks to enable the objective function.

        """

        _id = 0

        relative_path = os.path.dirname(os.path.abspath("main.py"))
        absolute_path = os.path.join(relative_path, "data", "lectures.csv")

        with open(absolute_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line = 0
            lectures = []

            # Loops over all lines in csv file
            for row in csv_reader:
                lectures.append(row)
        print(lectures)
        # Loops over lecture data (ld)
        for ld in lectures:
            _type = ld[0]
            name = ld[1]
            students = int(ld[2])
            capacity = int(ld[3])

            # Handles Hoorcollege
            if _type == "HC":
                lecture = lec.Lecture(_type, name, _id, students, capacity, 0)
                _id += 1
                self.find_course(name).lectures.append(lecture)

            # Handles Werkcollege & Practicum
            else:
                # Calculates number of needed groups and initializes track
                groups = math.ceil(students / capacity)
                track = 1

                # Makes right amount of lectures
                for group in range(groups):
                    # Full groups
                    if students > capacity:
                        lecture = lec.Lecture(_type, name, _id, capacity,
                                              capacity, track)
                        students -= capacity

                    # Remainder group
                    else:
                        lecture = lec.Lecture(_type, name, _id, students,
                                              capacity, track)
                        _id += 1
                        track += 1

                    self.find_course(name).lectures.append(lecture)

    def add_restricted(self):
        """ Adds restricted courses to each Course object.

        Creates a list of restricted course names for all Course objects. The
        lists are created from a csv file with the restriction data.

        """

        # Joins project path with file path to ensure cross-platform use
        relative_path = os.path.dirname(os.path.abspath("main.py"))
        absolute_path = os.path.join(relative_path, "data", "restricted.csv")

        # Opens CSV file
        with open(absolute_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line = 0

            # Loops over all lines in csv file
            for row in csv_reader:
                # Reads first row with headers
                if line == 0:
                    headers = row
                    line += 1
                # Reads data rows
                else:
                    # Placeholder for restricted courses
                    restricted_holder = []
                    # Processes data
                    for i in range(len(row)):
                        if row[i] == 'x':
                            restricted_holder.append(headers[i])
                        self.find_course(row[0]).restricted = restricted_holder

    def check_order(self, courses):
        """ Checks the lecture order in the grid.

        Checks the order of all lectures in a course. Repeats this check
        for all courses in the argument list.

        Arguments:
            courses [Course]: List of courses to check.

        Returns:
            Returns True if all courses are in the correct order, False if not.

        """

        for course in courses:
            positions = {"HC": [], "WC": [], "PR": []}

            for lecture in course.lectures:
                try:
                    (classroom, day, slot) = self.find_slot(lecture)[0]

                # Ignores exception if course is not in timetable
                except(IndexError):
                    return False

                position = day * 5 + slot
                positions[lecture.type].append(position)

            for position_HC in positions["HC"]:
                for position_not_HC in (positions["WC"] + positions["PR"]):
                    if position_HC >= position_not_HC:
                        return False

        return True

    def check_restriction(self, lecture, day, slot):
        """ Checks restriction for a lecture.

        Loops over all classrooms for a given day and slot to check if
        restricted lectures are being planned simultaneously.

        Arguments:
            lecture (Lecture): Lecture to be planned in.
            day (int): day to be planned in.
            slot (int):slot to be planned in.

        Returns:
            True if no restrictions are violated, False otherwise.

        """

        course = self.find_course(lecture.course)

        for i in range(6):
            try:
                course_i = self.grid[i][day][slot].course

                if (course_i in course.restricted or
                   lecture.course in course_i.restricted):
                    return False

            # Ignores exception if course is not in table
            except(AttributeError):
                pass

        return True

    def fill_nightslots(self):
        """ Fills all unavailable nightslots with Restricted object. """

        for classroom in range(7):
            for day in range(5):
                if classroom != 5:
                    self.grid[classroom][day][4] = res.Restricted()

    def score(self):
        """ Calculates score and both returns it and sets it as atribute. """

        self.objective_score = math.ceil(objective.objective_function(self))

        return math.ceil(self.objective_score)
