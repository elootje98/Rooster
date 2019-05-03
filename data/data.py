import timetable as t

lectures = [
    t.Lecture(1, "HC", "Advanced Heuristics", [3, 4, 5], 22, 0 , []),
    t.Lecture(2, "PR", "Advanced Heuristics", [3, 4, 5], 22, 10, []),
    t.Lecture(3, "HC", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33], 47, 0, []),
    t.Lecture(4, "WC", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33], 47, 25, []),
    t.Lecture(5, "PR", "Algoritmen en complexiteit", [1, 2, 30, 31, 32, 33], 47, 25, []),
    t.Lecture(6, "HC", "Analysemethoden en -technieken", [20, 21, 22, 23, 24, 72], 60, 0, []),
    t.Lecture(7, "HC", "Architectuur en computerorganisatie", [13, 14, 15, 16, 17, 44, 45, 48, 49, 52, 53, 54], 19, 0, []),
    t.Lecture(8, "HC", "Architectuur en computerorganisatie", [13, 14, 15, 16, 17, 44, 45, 48, 49, 52, 53, 54], 19, 0, []),
    t.Lecture(9, "HC", "Autonomous Agents 2", [25, 26, 27, 28], 19, 0, []),
    t.Lecture(10, "HC", "Autonomous Agents 2", [25, 26, 27, 28], 19, 0, []),
    t.Lecture(11, "WC", "Autonomous Agents 2", [25, 26, 27, 28], 19, 10, []),
    t.Lecture(12, "PR", "Autonomous Agents 2", [25, 26, 27, 28], 19, 10, []),
    t.Lecture(13, "HC", "Bioinformatica", [25, 26, 27, 28], 40, 0, []),
    t.Lecture(14, "HC", "Bioinformatica", [25, 26, 27, 28], 40, 0, []),
    t.Lecture(15, "HC", "Bioinformatica", [25, 26, 27, 28], 40, 0, []),
    t.Lecture(16, "WC", "Bioinformatica", [25, 26, 27, 28], 40, 20, []),
    t.Lecture(17, "PR", "Bioinformatica", [25, 26, 27, 28], 40, 20, []),
    t.Lecture(18, "HC", "Calculus 2", [38, 39, 57, 58], 90, 0, []),
    t.Lecture(19, "WC", "Calculus 2", [38, 39, 57, 58], 90, 40, []),
    t.Lecture(20, "HC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 0, []),
    t.Lecture(21, "HC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 0, []),
    t.Lecture(22, "HC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 0, []),
    t.Lecture(23, "WC", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 20, []),
    t.Lecture(24, "PR", "Collectieve Intelligentie", [30, 31, 32, 33, 57, 58], 65, 20, []),
    t.Lecture(25, "HC", "Compilerbouw", [29, 56], 70, 0, []),
    t.Lecture(26, "HC", "Compilerbouw", [29, 56], 70, 0, []),
    t.Lecture(27, "WC", "Compilerbouw", [29, 56], 70, 40, []),
    t.Lecture(28, "PR", "Compilerbouw", [29, 56], 70, 40, []),
    t.Lecture(29, "PR", "Compilerbouw (practicum)", [72], 35, 15, []),
    t.Lecture(30, "HC", "Data Mining", [59, 60, 61], 30, 0, []),
    t.Lecture(31, "HC", "Data Mining", [59, 60, 61], 30, 0, []),
    t.Lecture(32, "WC", "Data Mining", [59, 60, 61], 30, 10, []),
    t.Lecture(33, "PR", "Data Mining", [59, 60, 61], 30, 10, []),
    t.Lecture(34, "HC", "Databases 2", [46, 47, 50, 51, 55], 69, 0, []),
    t.Lecture(35, "WC", "Databases 2", [46, 47, 50, 51, 55], 69, 40, []),
    t.Lecture(36, "HC", "Heuristieken 1", [65, 66, 67], 44, 0, []),
    t.Lecture(37, "WC", "Heuristieken 1", [65, 66, 67], 44, 25, []),
    t.Lecture(38, "HC", "Heuristieken 2", [], 30, 0, []),
    t.Lecture(39, "WC", "Heuristieken 2", [], 30, 20, []),
    t.Lecture(40, "HC", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61], 40, 0, []),
    t.Lecture(41, "HC", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61], 40, 0, []),
    t.Lecture(42, "WC", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61], 40, 15, []),
    t.Lecture(43, "PR", "Informatie- en organisatieontwerp", [46, 47, 50, 51, 55, 59, 60, 61], 40, 15, []),
    t.Lecture(44, "HC", "Interactie-ontwerp", [], 31, 0, []),
    t.Lecture(45, "HC", "Interactie-ontwerp", [], 31, 0, []),
    t.Lecture(46, "HC", "Kansrekenen 2", [72], 70, 0, []),
    t.Lecture(47, "HC", "Kansrekenen 2", [72], 70, 0, []),
    t.Lecture(48, "HC", "Lineaire Algebra", [62, 63, 64], 50, 0, []),
    t.Lecture(49, "HC", "Lineaire Algebra", [62, 63, 64], 50, 0, []),
    t.Lecture(50, "HC", "Machine Learning", [], 25, 0, []),
    t.Lecture(51, "HC", "Machine Learning", [], 25, 0, []),
    t.Lecture(52, "HC", "Moderne Databases", [], 60, 0, []),
    t.Lecture(53, "WC", "Moderne Databases", [], 60, 20, []),
    t.Lecture(54, "PR", "Moderne Databases", [], 60, 20, []),
    t.Lecture(55, "PR", "Netwerken en systeembeveiliging", [72], 50, 20, []),
    t.Lecture(56, "PR", "Programmeren in Java 2", [69, 70, 71], 95, 20, []),
    t.Lecture(57, "PR", "Project Genetic Algorithms", [69, 70, 71], 40, 15, []),
    t.Lecture(58, "PR", "Project Numerical Recipes", [65, 66, 67], 40, 15, []),
    t.Lecture(59, "HC", "Reflectie op de digitale cultuur", [62, 63, 64], 53, 0, []),
    t.Lecture(60, "HC", "Reflectie op de digitale cultuur", [62, 63, 64], 53, 0, []),
    t.Lecture(61, "WC", "Reflectie op de digitale cultuur", [62, 63, 64], 53, 20, []),
    t.Lecture(62, "HC", "Software engineering", [], 75, 0, []),
    t.Lecture(63, "WC", "Software engineering", [], 75, 40, []),
    t.Lecture(64, "PR", "Software engineering", [], 75, 40, []),
    t.Lecture(65, "HC", "Technology for games", [], 50, 0, []),
    t.Lecture(66, "HC", "Technology for games", [], 50, 0, []),
    t.Lecture(67, "WC", "Technology for games", [], 50, 20, []),
    t.Lecture(68, "HC", "Webprogrammeren en databases", [], 46, 0, []),
    t.Lecture(69, "HC", "Webprogrammeren en databases", [], 46, 0, []),
    t.Lecture(70, "WC", "Webprogrammeren en databases", [], 46, 20, []),
    t.Lecture(71, "PR", "Webprogrammeren en databases", [], 46, 20, []),
    t.Lecture(72, "PR", "Zoeken, sturen en bewegen", [], 45, 15, [])]

courses = [t.Course(1, "Advanced Heuristics", [1, 2]), t.Course(
    2, "Algoritmen en complexiteit", [3, 4, 5]), t.Course(
    3, "Analysemethoden en -technieken", [6]), t.Course(
    4, "Architectuur en computerorganisatie", [7, 8]), t.Course(
    5, "Autonomous Agents 2", [9, 10, 11, 12]), t.Course(
    6, "Bioinformatica", [13, 14, 15, 16, 17]), t.Course(
    7, "Calculus 2", [18, 19]), t.Course(
    8, "Collectieve Intelligentie", [20, 21, 22, 23, 24]), t.Course(
    9, "Compilerbouw", [25, 26, 27, 28]), t.Course(
    10, "Compilerbouw (practicum)", [29]), t.Course(
    11, "Data Mining", [30, 31, 32, 33]), t.Course(
    12, "Databases 2", [34, 35]), t.Course(
    13, "Heuristieken 1", [36, 37]), t.Course(
    14, "Heuristieken 2", [28, 39]), t.Course(
    15, "Informatie- en organisatieontwerp", [40, 41, 42, 43]), t.Course(
    16, "Interactie-ontwerp", [44, 45]), t.Course(
    17, "Kansrekenen 2", [46, 47]), t.Course(
    18, "Lineaire Algebra", [48, 49]), t.Course(
    19, "Machine Learning", [50, 51]), t.Course(
    20, "Moderne Databases", [52, 53, 54]), t.Course(
    21, "Netwerken en systeembeveiliging", [55]), t.Course(
    22, "Programmeren in Java 2", [56]), t.Course(
    23, "Project Genetic Algorithms", [57]), t.Course(
    24, "Project Numerical Recipes", [58]), t.Course(
    25, "Reflectie op de digitale cultuur", [59, 60, 61]), t.Course(
    26, "Software engineering", [62, 63, 64]), t.Course(
    27, "Technology for games", [65, 66, 67]), t.Course(
    28, "Webprogrammeren en databases", [68, 69, 70, 71]), t.Course(
    29, "Zoeken, sturen en bewegen", [72])]

classrooms = {"A1.04" = 41, "A1.06" = 22, "A1.08" = 20, "A1.10" = 56, "B0.201" = 48, "C0.110" = 117, "C1.112" = 60}
