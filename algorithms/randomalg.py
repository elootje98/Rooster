import numpy as np

from classes import empty, timetable


def make_table(timetable):
    """ Makes a timetable using random.

    Shuffles list of courses and plans all lectures of each course randomly
    one by one. Lectures are put in a random unoccupied spot if they are not
    restricted by other lectures on the same timeslot. Correct order of all
    lectures is check after every course. If not ensured, the course is
    rescheduled untill it fits.

    Arguments:
        timetable (Timetable): Empty timetable to start with.

    """

    np.random.shuffle(timetable.courses)
    for course in timetable.courses:

        attempt = 0
        while True:
            completed = plan_lectures(course, timetable)
            attempt += 1

            if timetable.check_order([course]):
                break
            else:
                remove_lectures(course, timetable)

            if attempt > 10000 or not completed:
                return False

    timetable.score()
    return True


def plan_lectures(course, timetable):
    """ Plans all lectures of a course.

    Loops over all lectures of a course and randomy puts them in the grid.
    We check if the slot is empty and if there are no restrictions in the
    timeslot from other lectures. Random selection of slot is repeated untill
    the checks are succesful.

    Arguments:
        course (Course): Course to be scheduled.
        timetable (Timetable): Timetable to modify.

    """

    for lecture in course.lectures:
        attempt = 0
        while True:
            classroom = np.random.randint(0, 7)
            day = np.random.randint(0, 5)
            slot = np.random.randint(0, 5)

            if (type(timetable.grid[classroom][day][slot]) == empty.Empty and
               timetable.check_restriction(lecture, day, slot)):
                timetable.grid[classroom][day][slot] = lecture
                break

            attempt += 1
            if attempt > 10000:
                return False

    return True


def remove_lectures(course, timetable):
    """ Removes all lectures of a course.

    Loops over all lectures of a course and removes them from the grid. This
    method is used to reschedule courses which do not pass the order check.

    Arguments:
        course (Course): Course to be removed.
        timetable (Timetable): Timetable to modify.

    """

    for lecture in course.lectures:
        try:
            (classroom, day, slot) = timetable.find_slot(lecture)[0]
            timetable.grid[classroom][day][slot] = empty.Empty()
        except(IndexError):
            pass
