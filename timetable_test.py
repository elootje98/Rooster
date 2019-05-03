import numpy as np
from data import points as p
from data import data as d
import objective as o
import math

class Timetable:
    def __init__(self, courses, classrooms):
        # 5 days, 5 timeslots, 7 classrooms
        # index of grid is the same as list + 1
        self.grid = np.full((7, 5, 4), Empty(), dtype=object)
        # list of all courses
        self.courses = courses
        # list of all classrooms
        self.classrooms = classrooms

    def find_lecture(self, _id):
        return np.argwhere(self.grid.id == _id)

    def sort_courses(self):
        self.courses.sort(key=lambda course: course.points, reverse=True)

    def make_lectures(self, lectures):
        

class Course:
    def __init__(self, name):
        self.name = name
        self.lectures = []
        self.points = 0


class Lecture:
    def __init__(self, _type, course, _id, capacity):
        self.type = _type
        self.course = course
        self.id = _id
        self.capacity = capacity
        self.restricted = []
        self.students = 0
