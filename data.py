import numpy as np
import punten as p

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
            print(course.name)
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
        for course in self.courses:
            course.points = p.course_points(course)

        self.courses.sort(key=lambda course: course.points, reverse=True)

        for course in self.courses:
            print(course.name, course.points)

class Course:
    def __init__(self, _id, name, lectures):
        self.name = name
        # lijst van id-nummers van bijbehorende lectures
        self.lectures = lectures
        self._id = _id
        self.points = 0

class Lecture:
    def __init__(self, _id, _type, course, restricted):
        self._id = _id
        self.type = _type
        self.course = course
        # lijst van id-nummers van verboden lectures tegelijk
        self.restricted = restricted


courses = [Course(1, "Advanced Heuristics", [1, 2]), Course(
    2, "Algoritmen en complexiteit", [3, 4, 5]), Course(
    3, "Analysemethoden en -technieken", [6]), Course(
    4, "Architectuur en computerorganisatie", [7, 8]), Course(
    5, "Autonomous Agents 2", [9, 10, 11, 12]), Course(
    6, "Bioinformatica", [13, 14, 15, 16, 17]), Course(
    7, "Calculus 2", [18, 19]), Course(
    8, "Collectieve Intelligentie", [20, 21, 22, 23, 24]), Course(
    9, "Compilerbouw", [25, 26, 27, 28]), Course(
    10, "Compilerbouw (practicum)", [29]), Course(
    11, "Data Mining", [30, 31, 32, 33]), Course(
    12, "Databases 2", [34, 35]), Course(
    13, "Heuristieken 1", [36, 37]), Course(
    14, "Heuristieken 2", [28, 39]), Course(
    15, "Informatie- en organisatieontwerp", [40, 41, 42, 43]), Course(
    16, "Interactie-ontwerp", [44, 45]), Course(
    17, "Kansrekenen 2", [46, 47]), Course(
    18, "Lineaire Algebra", [48, 49]), Course(
    19, "Machine Learning", [50, 51]), Course(
    20, "Moderne Databases", [52, 53, 54]), Course(
    21, "Netwerken en systeembeveiliging", [55]), Course(
    22, "Programmeren in Java 2", [56]), Course(
    23, "Project Genetic Algorithms", [57]), Course(
    24, "Project Numerical Recipes", [58]), Course(
    25, "Reflectie op de digitale cultuur", [59, 60, 61]), Course(
    26, "Software engineering", [62, 63, 64]), Course(
    27, "Technology for games", [65, 66, 67]), Course(
    28, "Webprogrammeren en databases", [68, 69, 70, 71]), Course(
    29, "Zoeken, sturen en bewegen", [72])]

lectures = [
    Lecture(1, "HC", "Advanced Heuristics", [3, 4, 5]),
    Lecture(2, "PR", "Advanced Heuristics", [3, 4, 5]),
    Lecture(3, "HC", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33]),
    Lecture(4, "WC", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33]),
    Lecture(5, "PR", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33]),
    Lecture(6, "HC", "Analysemethoden en -technieken", [20, 21, 22, 23, 24, 72]),
    Lecture(7, "HC", "Architectuur en computerorganisatie", [13, 14, 15, 16, 17, 44, 45, 48, 49, 52, 53, 54]),
    Lecture(8, "HC", "Architectuur en computerorganisatie", [13, 14, 15, 16, 17, 44, 45, 48, 49, 52, 53, 54]),
    Lecture(9, "HC", "Autonomous Agents 2", [25, 26, 27, 28]),
    Lecture(10, "HC", "Autonomous Agents 2", [25, 26, 27, 28]),
    Lecture(11, "WC", "Autonomous Agents 2", [25, 26, 27, 28]),
    Lecture(12, "PR", "Autonomous Agents 2", [25, 26, 27, 28]),
    Lecture(13, "HC", "Bioinformatica", [25, 26, 27, 28]),
    Lecture(14, "HC", "Bioinformatica", [25, 26, 27, 28]),
    Lecture(15, "HC", "Bioinformatica", [25, 26, 27, 28]),
    Lecture(16, "WC", "Bioinformatica", [25, 26, 27, 28]),
    Lecture(17, "PR", "Bioinformatica", [25, 26, 27, 28]),
    Lecture(18, "HC", "Calculus 2", [38, 39, 57, 58]),
    Lecture(19, "WC", "Calculus 2", [38, 39, 57, 58]),
    Lecture(20, "HC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58]),
    Lecture(21, "HC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58]),
    Lecture(22, "HC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58]),
    Lecture(23, "WC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58]),
    Lecture(24, "PR", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58]),
    Lecture(25, "HC", "Compilerbouw", [29, 56]),
    Lecture(26, "HC", "Compilerbouw", [29, 56]),
    Lecture(27, "WC", "Compilerbouw", [29, 56]),
    Lecture(28, "PR", "Compilerbouw", [29, 56]),
    Lecture(29, "PR", "Compilerbouw (practicum)", [72]),
    Lecture(30, "HC", "Data Mining", [59, 60, 61]),
    Lecture(31, "HC", "Data Mining", [59, 60, 61]),
    Lecture(32, "WC", "Data Mining", [59, 60, 61]),
    Lecture(33, "PR", "Data Mining", [59, 60, 61]),
    Lecture(34, "HC", "Databases 2", [46, 47, 50, 51, 55]),
    Lecture(35, "WC", "Databases 2", [46, 47, 50, 51, 55]),
    Lecture(36, "HC", "Heuristieken 1", [65, 66, 67]),
    Lecture(37, "WC", "Heuristieken 1", [65, 66, 67]),
    Lecture(38, "HC", "Heuristieken 2", []),
    Lecture(39, "WC", "Heuristieken 2", []),
    Lecture(40, "HC", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61]),
    Lecture(41, "HC", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61]),
    Lecture(42, "WC", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61]),
    Lecture(43, "PR", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61]),
    Lecture(44, "HC", "Interactie-ontwerp", []),
    Lecture(45, "HC", "Interactie-ontwerp", []),
    Lecture(46, "HC", "Kansrekenen 2", [72]),
    Lecture(47, "HC", "Kansrekenen 2", [72]),
    Lecture(48, "HC", "Lineaire Algebra", [62, 63, 64]),
    Lecture(49, "HC", "Lineaire Algebra", [62, 63, 64]),
    Lecture(50, "HC", "Machine Learning", []),
    Lecture(51, "HC", "Machine Learning", []),
    Lecture(52, "HC", "Moderne Databases", []),
    Lecture(53, "WC", "Moderne Databases", []),
    Lecture(54, "PR", "Moderne Databases", []),
    Lecture(55, "PR", "Netwerken en systeembeveiliging", [72]),
    Lecture(56, "PR", "Programmeren in Java 2", [69, 70, 71]),
    Lecture(57, "PR", "Project Genetic Algorithms", [69, 70, 71]),
    Lecture(58, "PR", "Project Numerical Recipes", [65, 66, 67]),
    Lecture(59, "HC", "Reflectie op de digitale cultuur", [62, 63, 64]),
    Lecture(60, "HC", "Reflectie op de digitale cultuur", [62, 63, 64]),
    Lecture(61, "WC", "Reflectie op de digitale cultuur", [62, 63, 64]),
    Lecture(62, "HC", "Software engineering", []),
    Lecture(63, "WC", "Software engineering", []),
    Lecture(64, "PR", "Software engineering", []),
    Lecture(65, "HC", "Technology for games", []),
    Lecture(66, "HC", "Technology for games", []),
    Lecture(67, "WC", "Technology for games", []),
    Lecture(68, "HC", "Webprogrammeren en databases", []),
    Lecture(69, "HC", "Webprogrammeren en databases", []),
    Lecture(70, "WC", "Webprogrammeren en databases", []),
    Lecture(71, "PR", "Webprogrammeren en databases", []),
    Lecture(72, "PR", "Zoeken, sturen en bewegen", [])]

classrooms = ["A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C1.112"]


def get_lecture(lecture_id):

    return lectures[int(lecture_id) - 1]


def get_course(course_id):

    return courses[int(course_id) - 1]
