import numpy as np


class Rooster:
    def __init__(self, courses, lectures, classrooms):
        # 5 dagen, 5 tijdslots, 7 lokalen
        # index van grid is zelfde als lijst +1
        self.grid = np.zeros((7, 5, 5))
        # lijst van alle vakken
        self.courses = courses
        # lijst van alle lectures
        self.lectures = lectures
        # lijst van alle zalen
        self.classrooms = classrooms

    def make_grid(self):
        for course in self.courses:
            for lecture in self.lectures:
                empty = True
                while empty:
                    day = np.random.randint(0, 4)
                    slot = np.random.randint(0, 4)
                    classroom = np.random.randint(0, 4)
                    if self.grid[day][slot][classroom] == 0:
                        self.grid[day][slot][classroom] = lecture._id
                        empty = False


class Course:
    def __init__(self, name, lectures):
        self.name = name
        # lijst van id-nummers van bijbehorende lectures
        self.lectures = lectures


class Lecture:
    def __init__(self, _id, _type, course, restricted):
        self._id = _id
        self.type = _type
        self.course = course
        # lijst van id-nummers van verboden lectures tegelijk
        self.restricted = restricted


courses = [Course("Advanced Heuristics", [1, 2]), Course("Algoritmen en complexiteit"]
lectures = [Lecture(1, "HC", "Advanced Heuristics", []), Lecture(2, "PR", "Advanced Heuristics", [])]
classrooms = ["A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C1.112"]


rooster = Rooster(courses, lectures, classrooms)
rooster.make_grid()
print(rooster.grid)
