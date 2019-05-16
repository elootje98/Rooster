class Course:
    def __init__(self, name):
        """ Creates course object with a give name.

        Arguments:
            name (str): String with the name of the courseself.

        Attributes:
            name (str): Name of the course.
            lectures [Lecture]: List of Lecture objects.
            restricted [str]: List of restricted course names.
            points (int): Points used in greedy algorithm to express difficulty
                          when planning, determine the order in greedy.

        """
        self.name = name
        self.lectures = []
        self.restricted = []
        self.points = 0
