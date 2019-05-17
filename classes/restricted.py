class Restricted:
    def __init__(self):
        """ Creates placeholder object to fill unavailable nightslots.  """

        self.course = "restricted"

    def __str__(self):
        """ Prints 'Restricted' when object is printed. """

        return "Restricted"
