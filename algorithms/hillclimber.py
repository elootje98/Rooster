import random

import numpy as np

import objective as o
from classes import empty

def hillclimber(timetable, iterations, *args):
    """Algorithm: iterating over a premade timetable, swaps two random lectures"""

    points_timetable = o.objective_function(timetable)

    # iterates over a range
    for i in range(iterations):
    # while (points_timetable < -100): # use if you want to iterate to a score

        # swap two random lectures
        lecture_1 = random_lecture(timetable)
        while lecture_1[0] == empty.Empty:
            print(lecture_1[0])
            lecture_1 = random_lecture(timetable)
        lecture_2 = random_lecture(timetable)
        swap_lectures(timetable, lecture_1, lecture_2)
        after_points = o.objective_function(timetable)

        # swaps back if the number of points decreases
        if after_points < points_timetable:
            swap_lectures(timetable, lecture_1, lecture_2)
        after_points = o.objective_function(timetable)
        points_timetable = o.objective_function(timetable)

        # execute additional functions
        for functions in args:
            functions

def random_lecture(timetable):
    """Returns a random lecture from the timetable grid"""
    classroom = np.random.randint(0, 7)
    day = np.random.randint(0, 4)
    slot = np.random.randint(0, 4)
    return timetable.grid[classroom][day][slot], classroom, day, slot

def swap_lectures(timetable, lecture_1, lecture_2):
    """Swaps the grid locations of the given lectures"""
    c1 = lecture_1[1:4]
    c2 = lecture_2[1:4]
    timetable.grid[c1[0]][c1[1]][c1[2]], timetable.grid[c2[0]][c2[1]][c2[2]] = timetable.grid[c2[0]][c2[1]][c2[2]], timetable.grid[c1[0]][c1[1]][c1[2]]
