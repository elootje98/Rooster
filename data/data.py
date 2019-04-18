import rooster as r

lectures = [
    r.Lecture(1, "HC", "Advanced Heuristics", [3, 4, 5], 22, 0),
    r.Lecture(2, "PR", "Advanced Heuristics", [3, 4, 5], 22, 10),
    r.Lecture(3, "HC", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33], 47, 0),
    r.Lecture(4, "WC", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33], 47, 25),
    r.Lecture(5, "PR", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33], 47, 25),
    r.Lecture(6, "HC", "Analysemethoden en -technieken", [20, 21, 22, 23, 24, 72], 60, 0),
    r.Lecture(7, "HC", "Architectuur en computerorganisatie", [13, 14, 15, 16, 17, 44, 45, 48, 49, 52, 53, 54], 19, 0),
    r.Lecture(8, "HC", "Architectuur en computerorganisatie", [13, 14, 15, 16, 17, 44, 45, 48, 49, 52, 53, 54], 19, 0),
    r.Lecture(9, "HC", "Autonomous Agents 2", [25, 26, 27, 28], 19, 0),
    r.Lecture(10, "HC", "Autonomous Agents 2", [25, 26, 27, 28], 19, 0),
    r.Lecture(11, "WC", "Autonomous Agents 2", [25, 26, 27, 28], 19, 10),
    r.Lecture(12, "PR", "Autonomous Agents 2", [25, 26, 27, 28], 19, 10),
    r.Lecture(13, "HC", "Bioinformatica", [25, 26, 27, 28], 40, 0),
    r.Lecture(14, "HC", "Bioinformatica", [25, 26, 27, 28], 40, 0),
    r.Lecture(15, "HC", "Bioinformatica", [25, 26, 27, 28], 40, 0),
    r.Lecture(16, "WC", "Bioinformatica", [25, 26, 27, 28], 40, 20),
    r.Lecture(17, "PR", "Bioinformatica", [25, 26, 27, 28], 40, 20),
    r.Lecture(18, "HC", "Calculus 2", [38, 39, 57, 58], 90, 0),
    r.Lecture(19, "WC", "Calculus 2", [38, 39, 57, 58], 90, 40),
    r.Lecture(20, "HC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 0),
    r.Lecture(21, "HC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 0),
    r.Lecture(22, "HC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 0),
    r.Lecture(23, "WC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 20),
    r.Lecture(24, "PR", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 20),
    r.Lecture(25, "HC", "Compilerbouw", [29, 56], 70, 0),
    r.Lecture(26, "HC", "Compilerbouw", [29, 56], 70, 0),
    r.Lecture(27, "WC", "Compilerbouw", [29, 56], 70, 40),
    r.Lecture(28, "PR", "Compilerbouw", [29, 56], 70, 40),
    r.Lecture(29, "PR", "Compilerbouw (practicum)", [72], 35, 15),
    r.Lecture(30, "HC", "Data Mining", [59, 60, 61], 30, 0),
    r.Lecture(31, "HC", "Data Mining", [59, 60, 61], 30, 0),
    r.Lecture(32, "WC", "Data Mining", [59, 60, 61], 30, 10),
    r.Lecture(33, "PR", "Data Mining", [59, 60, 61], 30, 10),
    r.Lecture(34, "HC", "Databases 2", [46, 47, 50, 51, 55], 69, 0),
    r.Lecture(35, "WC", "Databases 2", [46, 47, 50, 51, 55], 69, 40),
    r.Lecture(36, "HC", "Heuristieken 1", [65, 66, 67], 44, 0),
    r.Lecture(37, "WC", "Heuristieken 1", [65, 66, 67], 44, 25),
    r.Lecture(38, "HC", "Heuristieken 2", [], 30, 0),
    r.Lecture(39, "WC", "Heuristieken 2", [], 30, 20),
    r.Lecture(40, "HC", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61], 40, 0),
    r.Lecture(41, "HC", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61], 40, 0),
    r.Lecture(42, "WC", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61], 40, 15),
    r.Lecture(43, "PR", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61], 40, 15),
    r.Lecture(44, "HC", "Interactie-ontwerp", [], 31, 0),
    r.Lecture(45, "HC", "Interactie-ontwerp", [], 31, 0),
    r.Lecture(46, "HC", "Kansrekenen 2", [72], 70, 0),
    r.Lecture(47, "HC", "Kansrekenen 2", [72], 70, 0),
    r.Lecture(48, "HC", "Lineaire Algebra", [62, 63, 64], 50, 0),
    r.Lecture(49, "HC", "Lineaire Algebra", [62, 63, 64], 50, 0),
    r.Lecture(50, "HC", "Machine Learning", [], 25, 0),
    r.Lecture(51, "HC", "Machine Learning", [], 25, 0),
    r.Lecture(52, "HC", "Moderne Databases", [], 60, 0),
    r.Lecture(53, "WC", "Moderne Databases", [], 60, 20),
    r.Lecture(54, "PR", "Moderne Databases", [], 60, 20),
    r.Lecture(55, "PR", "Netwerken en systeembeveiliging", [72], 50, 20),
    r.Lecture(56, "PR", "Programmeren in Java 2", [69, 70, 71], 95, 20),
    r.Lecture(57, "PR", "Project Genetic Algorithms", [69, 70, 71], 40, 15),
    r.Lecture(58, "PR", "Project Numerical Recipes", [65, 66, 67], 40, 15),
    r.Lecture(59, "HC", "Reflectie op de digitale cultuur", [62, 63, 64], 53, 0),
    r.Lecture(60, "HC", "Reflectie op de digitale cultuur", [62, 63, 64], 53, 0),
    r.Lecture(61, "WC", "Reflectie op de digitale cultuur", [62, 63, 64], 53, 20),
    r.Lecture(62, "HC", "Software engineering", [], 75, 0),
    r.Lecture(63, "WC", "Software engineering", [], 75, 40),
    r.Lecture(64, "PR", "Software engineering", [], 75, 40),
    r.Lecture(65, "HC", "Technology for games", [], 50, 0),
    r.Lecture(66, "HC", "Technology for games", [], 50, 0),
    r.Lecture(67, "WC", "Technology for games", [], 50, 20),
    r.Lecture(68, "HC", "Webprogrammeren en databases", [], 46, 0),
    r.Lecture(69, "HC", "Webprogrammeren en databases", [], 46, 0),
    r.Lecture(70, "WC", "Webprogrammeren en databases", [], 46, 20),
    r.Lecture(71, "PR", "Webprogrammeren en databases", [], 46, 20),
    r.Lecture(72, "PR", "Zoeken, sturen en bewegen", [], 45, 15)]

courses = [r.Course(1, "Advanced Heuristics", [1, 2]), r.Course(
    2, "Algoritmen en complexiteit", [3, 4, 5]), r.Course(
    3, "Analysemethoden en -technieken", [6]), r.Course(
    4, "Architectuur en computerorganisatie", [7, 8]), r.Course(
    5, "Autonomous Agents 2", [9, 10, 11, 12]), r.Course(
    6, "Bioinformatica", [13, 14, 15, 16, 17]), r.Course(
    7, "Calculus 2", [18, 19]), r.Course(
    8, "Collectieve Intelligentie", [20, 21, 22, 23, 24]), r.Course(
    9, "Compilerbouw", [25, 26, 27, 28]), r.Course(
    10, "Compilerbouw (practicum)", [29]), r.Course(
    11, "Data Mining", [30, 31, 32, 33]), r.Course(
    12, "Databases 2", [34, 35]), r.Course(
    13, "Heuristieken 1", [36, 37]), r.Course(
    14, "Heuristieken 2", [28, 39]), r.Course(
    15, "Informatie- en organisatieontwerp", [40, 41, 42, 43]), r.Course(
    16, "Interactie-ontwerp", [44, 45]), r.Course(
    17, "Kansrekenen 2", [46, 47]), r.Course(
    18, "Lineaire Algebra", [48, 49]), r.Course(
    19, "Machine Learning", [50, 51]), r.Course(
    20, "Moderne Databases", [52, 53, 54]), r.Course(
    21, "Netwerken en systeembeveiliging", [55]), r.Course(
    22, "Programmeren in Java 2", [56]), r.Course(
    23, "Project Genetic Algorithms", [57]), r.Course(
    24, "Project Numerical Recipes", [58]), r.Course(
    25, "Reflectie op de digitale cultuur", [59, 60, 61]), r.Course(
    26, "Software engineering", [62, 63, 64]), r.Course(
    27, "Technology for games", [65, 66, 67]), r.Course(
    28, "Webprogrammeren en databases", [68, 69, 70, 71]), r.Course(
    29, "Zoeken, sturen en bewegen", [72])]

classrooms = ["A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C1.112"]
