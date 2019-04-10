## Classes
# HOOOOOOOOOOOOOOOOOOOOOOI
class Course:
    def __init__(self, name, lectures, restricted, points, students):
        self.name = name
        self.lectures = lectures
        self.restricted = restricted
        self.points = points
        self.students = students

    def __str__(self):
        lectures = []
        for lecture in self.lectures:
            lectures.append(lecture.type)

        return f"Naam: {self.name}, Lectures: {lectures}"

class Classroom:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.slots = {"Mo9" : 0, "Mo11" : 0, "Mo13" : 0, "Mo15" : 0, "Tu9" : 0,
            "Tu11" : 0, "Tu13" : 0, "Tu15" : 0, "We9" : 0, "We11" : 0,
            "We13" : 0, "We15" : 0, "Th9" : 0, "Th11" : 0, "Th13" : 0,
            "Th15" : 0, "Fr9" : 0, "Fr11" : 0, "Fr13" : 0, "Fr15" : 0}

    def __str__(self):
        assigned_slots = {}
        for slot in self.slots:
            if self.slots[slot] != 0:
                assigned_slots[slot] = {self.slots[slot][0],
                self.slots[slot][1].type}

        return f"""Naam: {self.name}, Capacity: {self.capacity},
        Assigned slots: {assigned_slots}"""

    def assign_slot(self, slot, course, lecture):
        self.slots[slot] = [course, lecture]
        lecture.assigned = slot

class Lecture:
    def __init__(self, type, max):
        self.type = type
        self.assigned = 0;
        self.max = max

    def __str__(self):
        return f"Type: {self.type}, Max: {self.max}"

## Data

Classrooms = {"A1.04" : Classroom("A1.04", 41),
    "A1.06" : Classroom("A1.06", 22), "A1.08" : Classroom("A1.08", 20),
    "A1.010" : Classroom("A1.10", 56), "B0.201" : Classroom("B0.201", 48),
    "C0.110" : Classroom("C0.110", 117), "C1.112" : Classroom("C1.112", 60)}

Courses = {"Advanced Heuristics" : Course("Advanced Heuristics",
    [Lecture("HC", 0), Lecture("PR", 10)], "Algoritmen en complexiteit", 0, 22),
    "Algoritmen en complexiteit" : Course("Algoritmen en complexiteit",
    [Lecture("HC", 0), Lecture("WC", 25), Lecture("PR", 25)],
    "Advanced Heuristics", 0, 47)}




""" TODO
Als restricted van Course niet leeg is:
Loop over alle lokalen en check huidige tijdsslot
Als restricted vak gevonden wordt, kan niet worden ingepland.
"""
