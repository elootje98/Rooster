class Empty:
    def __init__(self):
        """ Creates placeholder object to sybolize empty spots in the grid. """

        self.course = "empty"

    def __str__(self):
        """ Prints 'Empty' when object is printed. """

        return " - "
