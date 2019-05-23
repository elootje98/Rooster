import numpy as np
from algorithms import randomalg as rand
from classes import empty
from classes import timetable as t
from data import points as p


def make_table(timetable):
    """Makes the timetable, with the course sorted on their points"""

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
                return False

    timetable.score()
    return True

def give_points_lectures(timetable):
    """Sort the courses based on their 'difficulty' for planning them in."""

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
