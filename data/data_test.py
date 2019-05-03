import timetable as t

lectures = [
    ["HC", "Advanced Heuristics", 22, 0],
    ["PR", "Advanced Heuristics", 22, 10],
    ["HC", "Algoritmen en complexiteit", 47, 0],
    ["WC", "Algoritmen en complexiteit", 47, 25],
    ["PR", "Algoritmen en complexiteit", 47, 25],
    ["HC", "Analysemethoden en -technieken", 60, 0],
    ["HC", "Architectuur en computerorganisatie", 19, 0],
    ["HC", "Architectuur en computerorganisatie", 19, 0],
    ["HC", "Autonomous Agents 2", 19, 0],
    ["HC", "Autonomous Agents 2", 19, 0],
    ["WC", "Autonomous Agents 2", 19, 10],
    ["PR", "Autonomous Agents 2", 19, 10],
    ["HC", "Bioinformatica", 40, 0],
    ["HC", "Bioinformatica", 40, 0],
    ["HC", "Bioinformatica", 40, 0],
    ["WC", "Bioinformatica", 40, 20],
    ["PR", "Bioinformatica", 40, 20],
    ["HC", "Calculus 2", 90, 0],
    ["WC", "Calculus 2", 90, 40],
    ["HC", "Collectieve Intelligentie", 65, 0],
    ["HC", "Collectieve Intelligentie", 65, 0],
    ["HC", "Collectieve Intelligentie", 65, 0],
    ["WC", "Collectieve Intelligentie", 65, 20],
    ["PR", "Collectieve Intelligentie", 65, 20],
    ["HC", "Compilerbouw", 70, 0],
    ["HC", "Compilerbouw", 70, 0],
    ["WC", "Compilerbouw", 70, 40],
    ["PR", "Compilerbouw", 70, 40],
    ["PR", "Compilerbouw [practicum)", 35, 15],
    ["HC", "Data Mining", 30, 0],
    ["HC", "Data Mining", 30, 0],
    ["WC", "Data Mining", 30, 10],
    ["PR", "Data Mining", 30, 10],
    ["HC", "Databases 2", 69, 0],
    ["WC", "Databases 2", 69, 40],
    ["HC", "Heuristieken 1", 44, 0],
    ["WC", "Heuristieken 1", 44, 25],
    ["HC", "Heuristieken 2", 30, 0],
    ["WC", "Heuristieken 2", 30, 20],
    ["HC", "Informatie- en organisatieontwerp", 40, 0],
    ["HC", "Informatie- en organisatieontwerp", 40, 0],
    ["WC", "Informatie- en organisatieontwerp", 40, 15],
    ["PR", "Informatie- en organisatieontwerp", 40, 15],
    ["HC", "Interactie-ontwerp", 31, 0],
    ["HC", "Interactie-ontwerp", 31, 0],
    ["HC", "Kansrekenen 2", 70, 0],
    ["HC", "Kansrekenen 2", 70, 0],
    ["HC", "Lineaire Algebra", 50, 0],
    ["HC", "Lineaire Algebra", 50, 0],
    ["HC", "Machine Learning", 25, 0],
    ["HC", "Machine Learning", 25, 0],
    ["HC", "Moderne Databases", 60, 0],
    ["WC", "Moderne Databases", 60, 20],
    ["PR", "Moderne Databases", 60, 20],
    ["PR", "Netwerken en systeembeveiliging", 50, 20],
    ["PR", "Programmeren in Java 2", 95, 20],
    ["PR", "Project Genetic Algorithms", 40, 15],
    ["PR", "Project Numerical Recipes", 40, 15],
    ["HC", "Reflectie op de digitale cultuur", 53, 0],
    ["HC", "Reflectie op de digitale cultuur", 53, 0],
    ["WC", "Reflectie op de digitale cultuur", 53, 20],
    ["HC", "Software engineering", 75, 0],
    ["WC", "Software engineering", 75, 40],
    ["PR", "Software engineering", 75, 40],
    ["HC", "Technology for games", 50, 0],
    ["HC", "Technology for games", 50, 0],
    ["WC", "Technology for games", 50, 20],
    ["HC", "Webprogrammeren en databases", 46, 0],
    ["HC", "Webprogrammeren en databases", 46, 0],
    ["WC", "Webprogrammeren en databases", 46, 20],
    ["PR", "Webprogrammeren en databases", 46, 20],
    ["PR", "Zoeken, sturen en bewegen", 45, 15]]

courses = [t.Course[1, "Advanced Heuristics", [1, 2]), t.Course[
    2, "Algoritmen en complexiteit", [3, 4, 5]), t.Course[
    3, "Analysemethoden en -technieken", [6]), t.Course[
    4, "Architectuur en computerorganisatie", [7, 8]), t.Course[
    5, "Autonomous Agents 2", [9, 10, 11, 12]), t.Course[
    6, "Bioinformatica", [13, 14, 15, 16, 17]), t.Course[
    7, "Calculus 2", [18, 19]), t.Course[
    8, "Collectieve Intelligentie", [20, 21, 22, 23, 24]), t.Course[
    9, "Compilerbouw", [25, 26, 27, 28]), t.Course[
    10, "Compilerbouw [practicum)", [29]), t.Course[
    11, "Data Mining", [30, 31, 32, 33]), t.Course[
    12, "Databases 2", [34, 35]), t.Course[
    13, "Heuristieken 1", [36, 37]), t.Course[
    14, "Heuristieken 2", [28, 39]), t.Course[
    15, "Informatie- en organisatieontwerp", [40, 41, 42, 43]), t.Course[
    16, "Interactie-ontwerp", [44, 45]), t.Course[
    17, "Kansrekenen 2", [46, 47]), t.Course[
    18, "Lineaire Algebra", [48, 49]), t.Course[
    19, "Machine Learning", [50, 51]), t.Course[
    20, "Moderne Databases", [52, 53, 54]), t.Course[
    21, "Netwerken en systeembeveiliging", [55]), t.Course[
    22, "Programmeren in Java 2", [56]), t.Course[
    23, "Project Genetic Algorithms", [57]), t.Course[
    24, "Project Numerical Recipes", [58]), t.Course[
    25, "Reflectie op de digitale cultuur", [59, 60, 61]), t.Course[
    26, "Software engineering", [62, 63, 64]), t.Course[
    27, "Technology for games", [65, 66, 67]), t.Course[
    28, "Webprogrammeren en databases", [68, 69, 70, 71]), t.Course[
    29, "Zoeken, sturen en bewegen", [72])]

classrooms = {"A1.04" = 41, "A1.06" = 22, "A1.08" = 20, "A1.10" = 56, "B0.201" = 48, "C0.110" = 117, "C1.112" = 60}
