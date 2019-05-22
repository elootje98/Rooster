import numpy as np

from classes import empty
from classes import timetable as t
from data import points as p


def make_table(timetable):

    # First sort the courses based on points
    give_points_lectures(timetable)
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


# Gives points to the lecture for planning in for greedy.
def give_points_lectures(timetable):

    # Loop over the courses and lectures
    for course in timetable.courses:
        points = 0

        # Check if the course is restricted
        number_restricted = len(course.restricted)
        points = points + (number_restricted * 20)

        # Loop over the lectures
        for lecture in course.lectures:
            # If it is an HC, it gets priority and extra points.
            if lecture.type == "HC":
                points = points + 10

        # Give the course his points
        course.points = points

    # Sort the courses on the points
    timetable.sort_courses()


def plan_lectures(course, timetable):
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
    for lecture in course.lectures:
        (classroom, day, slot) = timetable.find_slot(lecture)[0]
        timetable.grid[classroom][day][slot] = empty.Empty()
