class Empty:
    def __init__(self):
        """ Creates placeholder object to sybolize empty spots in the grid. """

        self.course = "empty"
        self.restricted = []
        self.lectures = []

    def __str__(self):
        """ Prints ' - ' when object is printed. """

        return " - "
