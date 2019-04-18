import numpy as np
import rooster as r


# Constructs a valid rooster from empty rooster object
def make_grid(rooster):

    # Test is a temporary rooster object to validate changes before committing
    test = rooster
    for course in rooster.courses:
        test = plan_lectures(course, test)
        while not test.check_order([course]):
            test = plan_lectures(course, test)
        rooster = test


def plan_lectures(course, test):

    for lecture in course.lectures:
        empty = True
        while empty:
            restricted = False
            classroom = np.random.randint(0, 7)
            slot = np.random.randint(0, 5)
            day = np.random.randint(0, 4)

            # Checks if slot is available
            if test.grid[classroom][slot][day] == 0:
                # checkt of er op dat slot restricted colleges zijn
                for i in range(7):
                    if test.grid[i][slot][day] in r.get_lecture(lecture).restricted:
                        restricted = True
                        break

                if not restricted:
                    test.grid[classroom][slot][day] = lecture
                    empty = False

    return test
