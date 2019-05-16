import random

import numpy as np
import math
import objective as o
from classes import empty

def simulated(timetable):
    """Simulated annealing algorithm"""

    # Calculate points of current timetable
    points_timetable = o.objective_function(timetable)
    temperature = 10000000000000000000
    alfa = 0.99
    maximum_points = 380
    minimum_points = -1400

    while(temperature > 10):

        # swap two random lectures
        lecture_1 = random_lecture(timetable)
        while lecture_1[0] == empty.Empty:
            print(lecture_1[0])
            lecture_1 = random_lecture(timetable)
        lecture_2 = random_lecture(timetable)
        swap_lectures(timetable, lecture_1, lecture_2)
        after_points = o.objective_function(timetable)
        delta_points = after_points - points_timetable

        # If the timetable is not better, accept with prop.
        if delta_points < 0:
            print("delta", delta_points)
            print("temperature", temperature)
            chance = 1 - math.exp(-delta_points/temperature)
            print(chance)
            bound = random.randrange(1)
            print("CHAAAAAAAAAAAAAAAAAAAAAAAAAANGE")
            if chance < bound:
                # swaps back
                swap_lectures(timetable, lecture_1, lecture_2)
                points_timetable = o.objective_function(timetable)
            else:
                print("BAAAAAAAAAAAAAAAAAD")
        temperature = temperature * alfa

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
