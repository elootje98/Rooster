import numpy as np
from data import points as p
from data import data as d
import objective as o
import math

class Timetable:
    def __init__(self, courses, lectures, classrooms):
        # 5 days, 5 timeslots, 7 classrooms
        # index of grid is the same as list + 1
        self.grid = np.zeros((7, 5, 4), dtype=object)
        self.grid.fill(Empty())
        # list of all courses
        self.courses = courses
        # list of all lectures
        self.lectures = lectures
        # list of all child lectures
        self.child_lectures = []
        # list of all classrooms
        self.classrooms = classrooms


    # finds a lecture in the grid TODO: reform
    def find_lecture(self, lecture_id):
        return np.argwhere(self.grid == lecture_id)


    # checks whether restricted lectures have been scheduled on the same
    # timeslot, returns false if this is the case
    def check_restriction(self):

        for days in range(5):
            for slots in range(5):
                lectures_in_slot = []
                restricted_in_slot = []
                for lecture in range(7):
                    lectures_in_slot.append(self.grid[lecture][days][slots])
                    restricted_in_slot.append(get_lecture(self.grid[lecture][days][slots]))

                for i in lectures_in_slot:
                    if i in restricted_in_slot:
                        return False

        return True


    def check_order(self, courses):

        for course in courses:
            lectures = course.lectures
            lecture_dict = {}
            not_HC = False
            for lecture in lectures:
                lecture_dict[self.find_lecture(lecture)[0][1] * 5 +
                self.find_lecture(lecture)[0][2]] = self.lectures[lecture - 1].type

            sorted(lecture_dict)
            for key in lecture_dict:
                if lecture_dict[key] != "HC":
                    not_HC = True
                elif not_HC and lecture_dict[key] == "HC":
                    return False
        return True

    def sort(self):
        self.courses.sort(key=lambda course: course.points, reverse=True)


    # Make a dict with children. The key of the dict will be the lecture Id,
    # The value will be a list of the children of that lecture
    def make_children(self):
        counter = 1
        for lecture in self.lectures:
            # make different numbers of werkcollege students
            if lecture.type != 'HC':
                print(lecture.course)
                nr_child_lectures = math.ceil(lecture.students / lecture.capacity)
                rest_student = lecture.students % lecture.capacity
                nr_students_in_child = lecture.capacity
                for i in range(nr_child_lectures):
                    if i == nr_child_lectures - 1 and rest_student != 0:
                        nr_students_in_child = rest_student
                    self.child_lectures.append(Child_Lecture(lecture, counter, nr_students_in_child))
                    counter += 1
            else:
                self.child_lectures.append(Child_Lecture(lecture, counter, lecture.students))
                counter += 1

        for lecture in self.child_lectures:
            for item in vars(lecture).items():
                print(item)


class Course:
    def __init__(self, _id, name, lectures):
        self.name = name
        # list of id's of corresponding lectures
        self.lectures = lectures
        self._id = _id
        self.points = self.course_points()

    def course_points(self):
        points = 0
        lecture_points = {"restricted": 20, "HC": 10, "WC": 5, "PR": 5}
        lecture = self.lectures[0]
        list_restricted = d.lectures[lecture - 1].restricted
        points += len(list_restricted) * 20
        for lecture in self.lectures:
            points += lecture_points[d.lectures[lecture - 1].type]
        return points

class Lecture:
    def __init__(self, _id, _type, course, restricted, students, capacity, children):
        self._id = _id
        self.type = _type
        self.course = course
        # list of id's of restricted lectures
        self.restricted = restricted
        self.students = students
        self.capacity = capacity
        self.children = []

class Empty:
    def __init__(self):
        self.course = "empty"

class Child_Lecture(Lecture):
    def __init__(self, parent, child_id, child_students):
        super().__init__(parent._id, parent.type, parent.course, parent.restricted, parent.students, parent.capacity, parent.children)
        self.parent_id = self._id
        self._id = child_id
        self.students = child_students

def get_lecture(lecture_id):

    return d.lectures[int(lecture_id) - 1]


def get_course(course_id):

    return d.courses[int(course_id) - 1]
