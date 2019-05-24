import numpy as np

from algorithms import randomalg as rand
from classes import empty
from classes import timetable as t
from data import points as p
from helpers.objective import objective_function
from helpers import timetable_helpers as hlp


def make_table(timetable):
    """Makes timetable using greedy

    First calls gives_points_lectures to sort the courses based on their
    points. The lectures of courses with the highest points, will be planned
    in first. After planning in the lecture, there is checked if the lectures
    of that course are in the right order. If they are not, the lectures will
    be removed and a new attampt will be made. In the case of >1000 attemps
    (which most likely mean that the algorithm is stuck in a loop), a complete
    new timetable will be made.

    Returns:
        timetable.

    """

    # First sort the courses based on points
    give_points_lectures(timetable)
    for course in timetable.courses:

        attempt = 0
        while True:
            completed = rand.plan_lectures(course, timetable)
            attempt += 1

            if timetable.check_order([course]):
                break
            else:
                rand.remove_lectures(course, timetable)

            if attempt > 10000 or not completed:
                make_table(t.Timetable())

    timetable.score()

    return timetable


def give_points_lectures(timetable):
    """Sort the courses based on their 'difficulty' for planning them in.

    Loops over the courses and gives points to the course, based on how
    difficult they are to plan in. For each course that can't be given at the
    same time, 20 points are given. Furthermore, for each HC, 10 points are
    given to the course.

    """

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
