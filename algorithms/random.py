import numpy as np
import timetable as t


# Constructs a valid timetable from empty timetable object
def make_grid(timetable):

    # Test is a temporary timetable object to validate changes before committing
    test = timetable
    for course in timetable.courses:
        test = plan_lectures(course, test)
        while not test.check_order([course]):
            test = plan_lectures(course, test)
        timetable = test


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
                # checks if there are restricted lectures on that timeslot
                for i in range(7):
                    if test.grid[i][slot][day] in t.get_lecture(lecture).restricted:
                        restricted = True
                        break

                if not restricted:
                    test.grid[classroom][slot][day] = lecture
                    empty = False

    return test
