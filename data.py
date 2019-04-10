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
                    classroom = np.random.randint(0, 6)
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


courses = [Course("Advanced Heuristics", [1, 2]), Course(
    "Algoritmen en complexiteit", [3, 4, 5]), Course(
    "Analysemethoden en -technieken", [6]), Course(
    "Architectuur en computerorganisatie", [7, 8]), Course(
    "Autonomous Agents 2", [9, 10, 11, 12]), Course(
    "Bioinformatica", [13, 14, 15, 16, 17]), Course(
    "Calculus 2", [18, 19]), Course(
    "Collectieve Intelligentie", [20, 21, 22, 23, 24]), Course(
    "Compilerbouw", [25, 26, 27, 28]), Course(
    "Compilerbouw (practicum)", [29]), Course(
    "Data Mining", [30, 31, 32, 33]), Course(
    "Databases 2", [34, 35]), Course(
    "Heuristieken 1", [36, 37]), Course(
    "Heuristieken 2", [28, 39]), Course(
    "Informatie- en organisatieontwerp", [40, 41, 42, 43]), Course(
    "Interactie-ontwerp", [44, 45]), Course(
    "Kansrekenen 2", [46, 47]), Course(
    "Lineaire Algebra", [48, 49]), Course(
    "Machine Learning", [50, 51]), Course(
    "Moderne Databases", [52, 53, 54]), Course(
    "Netwerken en systeembeveiliging", [55]), Course(
    "Programmeren in Java 2", [56]), Course(
    "Project Genetic Algorithms", [57]), Course(
    "Project Numerical Recipes", [58]), Course(
    "Reflectie op de digitale cultuur", [59, 60, 61]), Course(
    "Software engineering", [62, 63, 64]), Course(
    "Technology for games", [65, 66, 67]), Course(
    "Webprogrammeren en databases", [68, 69, 70, 71]), Course(
    "Zoeken, sturen en bewegen", [72])]


lectures = [Lecture(1, "HC", "Advanced Heuristics", []), Lecture(2, "PR", "Advanced Heuristics", [])]
classrooms = ["A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C1.112"]


rooster = Rooster(courses, lectures, classrooms)
rooster.make_grid()
print(rooster.grid)
