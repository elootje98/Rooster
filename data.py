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
            for lecture in course.lectures:
                empty = True
                while empty:
                    restricted = False
                    classroom = np.random.randint(0, 7)
                    slot = np.random.randint(0, 5)
                    day = np.random.randint(0, 5)

                    # checkt of plek vrij is
                    if self.grid[classroom][slot][day] == 0:
                        # checkt of er op dat slot restricted colleges zijn
                        for i in range(7):
                            if self.grid[i][slot][day] in self.lectures[lecture - 1].restricted:
                                restricted = True
                                print("restriced", lecture, self.lectures[lecture - 1].restricted)
                                break

                        if not restricted:
                            self.grid[classroom][slot][day] = lecture
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

lectures = [
    Lecture(1, "HC", "Advanced Heuristics", [3, 4, 5]),
    Lecture(2, "PR", "Advanced Heuristics", [3, 4, 5]),
    Lecture(3, "HR", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33]),
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


rooster = Rooster(courses, lectures, classrooms)
rooster.make_grid()
print(rooster.grid)
