import csv
import math
import os

import numpy as np

from classes import classroom as cla
from classes import course as crs
from classes import empty as emp
from classes import lecture as lec
from classes import restricted as res
from data import data as d


class Timetable:
    def __init__(self):
        # 7 Classrooms, 5 days, 4(5) timeslots
        self.grid = np.full((7, 5, 5), emp.Empty(), dtype=object)
        self.courses = []
        self.classrooms = []
        self.make_courses()
        self.make_lectures(d.lectures)
        self.make_classrooms()
        self.add_restricted()
        self.fill_nightslots()

    # Finds lecture object for entered ID (int)
    def find_lecture(self, _id):
        for course in self.courses:
            for lecture in course.lectures:
                if lecture.id == _id:
                    return lecture

    # Finds course object with entered name (string)
    def find_course(self, name):
        for course in self.courses:
            if course.name == name:
                return course

    # Finds grid coordinates of lecture object
    def find_slot(self, lecture):
        return np.argwhere(self.grid == lecture)

    # Sorts list of courses based on points
    def sort_courses(self):
        self.courses.sort(key=lambda course: course.points, reverse=True)

    def make_courses(self):
        for course in d.courses:
            self.courses.append(crs.Course(course))

    def make_classrooms(self):
        for classroom in d.classrooms:
            self.classrooms.append(cla.Classroom(classroom[0], classroom[1]))

    # Creates and assigns lecture objects based on list of data
    def make_lectures(self, lectures):
        # ID counter
        _id = 0

        # Loops over lecture data (ld)
        for ld in lectures:
            _type = ld[0]
            name = ld[1]
            students = ld[2]
            capacity = ld[3]

            # Handles Hoorcollege
            if _type == "HC":
                lecture = lec.Lecture(_type, name, _id, students, capacity)
                _id += 1
                self.find_course(name).lectures.append(lecture)

            # Handles Werkcollege & Practicum
            else:
                # Calculates number of needed groups
                groups = math.ceil(students / capacity)

                # Makes right amount of lectures
                for group in range(groups):
                    # Full groups
                    if students > capacity:
                        lecture = lec.Lecture(_type, name, _id, capacity, capacity)
                        students -= capacity
                    # Remainder group
                    else:
                        lecture = lec.Lecture(_type, name, _id, students, capacity)

                    _id += 1
                    self.find_course(name).lectures.append(lecture)

    # Reads and assigns restricted courses to Course objects
    def add_restricted(self):
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
        for course in courses:
            positions = {"HC": [], "WC": [], "PR": []}

            for lecture in course.lectures:
                (classroom, day, slot) = self.find_slot(lecture)[0]
                position = day * 5 + slot
                positions[lecture.type].append(position)

            for position_HC in positions["HC"]:
                for position_not_HC in (positions["WC"] + positions["PR"]):
                    if position_HC >= position_not_HC:
                        return False

        return True

    def check_restriction(self, lecture, day, slot):
        course = self.find_course(lecture.course)

        for i in range(6):
            try:
                if (self.grid[i][day][slot].course in course.restricted or
                   lecture.course in self.grid[i][day][slot].course.restricted):
                    return False
            except(AttributeError):
                pass

        return True


    def fill_nightslots(self):
        for classroom in range(7):
            for day in range(5):
                if classroom != 5:
                    self.grid[classroom][day][4] = res.Restricted()
