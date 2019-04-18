import numpy as np
from data import points as p
from data import data as d
import objective as o
import math

class Rooster:
    def __init__(self, courses, lectures, classrooms):
        # 5 dagen, 5 tijdslots, 7 lokalen
        # index van grid is zelfde als lijst +1
        self.grid = np.zeros((7, 5, 4), dtype=int)
        # lijst van alle vakken
        self.courses = courses
        # lijst van alle lectures
        self.lectures = lectures
        # lijst van alle zalen
        self.classrooms = classrooms


    def find_lecture(self, lecture_id):

        return np.argwhere(self.grid == lecture_id)


        # Checkt of restricted vakken tegelijk zijn ingeroosterd,
        # returns false if this is the case
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

    def make_children(self):
        children = {}
        for lecture in self.lectures:
            if lecture.type != 'HC':
                print(lecture.course)
                children = math.ceil(lecture.students / lecture.capacity)

    # Make a dict with children. The key of the dict will be the lecture Id,
    # The value will be a list of the children of that lecture 

class Course:
    def __init__(self, _id, name, lectures):
        self.name = name
        # lijst van id-nummers van bijbehorende lectures
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
    def __init__(self, _id, _type, course, restricted, students, capacity):
        self._id = _id
        self.type = _type
        self.course = course
        # lijst van id-nummers van verboden lectures tegelijk
        self.restricted = restricted
        self.students = students
        self.capacity = capacity

def get_lecture(lecture_id):

    return d.lectures[int(lecture_id) - 1]


def get_course(course_id):

    return d.courses[int(course_id) - 1]
