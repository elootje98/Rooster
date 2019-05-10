import numpy as np
import timetable as t
from data import points as p

def make_table(timetable):

    # First sort the courses based on points
    give_points_lectures(timetable)
    for course in timetable.courses:
        while True:
            plan_lectures(course, timetable)
            if timetable.check_order([course]):
                break
            else:
                remove_lectures(course, timetable)

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
        while True:
            # Start from first available
            for day in range(5):
                for slot in range(4):
                    for classroom in range(7):
                        if type(timetable.grid[classroom][day][slot]) == t.Empty:
                            timetable.grid[classroom][day][slot] = lecture
                            break

def remove_lectures(course, timetable):
    for lecture in course.lectures:
        (classroom, day, slot) = timetable.find_slot(lecture)[0]
        timetable.grid[classroom][day][slot] = t.Empty()
