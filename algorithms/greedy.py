import numpy as np
from algorithms import randomalg as rand
from classes import empty
from classes import timetable as t
from data import points as p
from objective import objective_function
import copy

def greedy_table(timetable, iterations):
    """Makes a timetable using greedy multiple times and picks the timetable with the highest score"""

    # Save all the timetables and their points
    points = -10000
    for i in range(iterations):
        compare_timetable = copy.deepcopy(timetable)
        make_table(compare_timetable)
        new_points = objective_function(compare_timetable)
        if new_points > points:
            new_timetable = copy.deepcopy(compare_timetable)
            points = new_points

    # Select the timetable with the hightest points
    return copy.deepcopy(new_timetable)

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
