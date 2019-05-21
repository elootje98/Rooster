class Lecture:
    def __init__(self, _type, course, _id, students, capacity, track):
        """ Creates Lecture object for in the grid.

        Attributes:
        type (str): Type of lecture (HC, WC or PR)
        course (str): Name of the course of the lecture.
        id (int): ID of the lecture (incremental).
        capacity (int): Maximum capacity of the Werkcollege/Practicum
        students (int): Number of students.
        track (int): Track ID, links each Werkcollege to a Practicum.

        """

        self.type = _type
        self.course = course
        self.id = _id
        self.capacity = capacity
        self.students = students
        self.track = track
        self.score = 0
