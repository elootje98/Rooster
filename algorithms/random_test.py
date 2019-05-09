import numpy as np

import timetable_test as t


def make_table(timetable):
    for course in timetable.courses:
        while True:
            plan_lectures(course, timetable)
            if timetable.check_order([course]):
                break
            else:
                remove_lectures(course, timetable)


def plan_lectures(course, timetable):
    for lecture in course.lectures:
        while True:
            classroom = np.random.randint(0, 7)
            day = np.random.randint(0, 5)
            slot = np.random.randint(0, 4)

            if type(timetable.grid[classroom][day][slot]) == t.Empty:
                timetable.grid[classroom][day][slot] = lecture
                break


def remove_lectures(course, timetable):
    for lecture in course.lectures:
        (classroom, day, slot) = timetable.find_slot(lecture)[0]
        timetable.grid[classroom][day][slot] = t.Empty()
