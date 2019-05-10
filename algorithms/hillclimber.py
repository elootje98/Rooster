import numpy as np
import random

import objective as o
from classes import timetable as t

def hillclimber(timetable, iterations):
    # check points of courses?


    # TODO: is het sneller om meerdere lectures tegelijk te verwisselen als de score heeeel laag is
    points_timetable = o.objective_function(timetable)
    maximum_points = 380
    minimum_points = -1400
    #while (points_timetable < -100):
    for i in range(iterations):

        # number of lectures to be swapped
        to_swap = []

        # use chance to swap multiple lectures
        chance_bound = 0.001 * (maximum_points - points_timetable)
        bound = random.uniform(0, maximum_points - minimum_points)
        # print(chance_bound, bound)

        if (bound < chance_bound):
            for i in range(8):
                to_swap.append(random_lecture(timetable))
        else:
            to_swap.append(random_lecture(timetable))
            to_swap.append(random_lecture(timetable))# exclude empty!


        for j in range(0, len(to_swap), 2):
            # get points before and after iteration
            swap_lectures(timetable, to_swap[j], to_swap[j+1])

        after_points = o.objective_function(timetable)

        # for k in range(len(to_swap)):
        #     print(timetable.grid[to_swap[k][1]][to_swap[k][2]][to_swap[k][3]].course)

        #print(lecture_1[1], lecture_1[2], lecture_1[3], lecture_2[1], lecture_2[2], lecture_2[3])
        # print("Before ",points_timetable, "    After ", after_points)

        if after_points < points_timetable:
            for j in range(0, len(to_swap), 2):
                # get points before and after iteration
                swap_lectures(timetable, to_swap[j], to_swap[j+1])
        after_points = o.objective_function(timetable)

        #print(timetable.grid[lecture_1[1]][lecture_1[2]][lecture_1[3]].course, timetable.grid[lecture_2[1]][lecture_2[2]][lecture_2[3]].course)
        #print(lecture_1[1], lecture_1[2], lecture_1[3], lecture_2[1], lecture_2[2], lecture_2[3])
        # print( "After ", after_points)
        points_timetable = o.objective_function(timetable)


def random_lecture(timetable):
    classroom = np.random.randint(0, 7)
    day = np.random.randint(0, 4)
    slot = np.random.randint(0, 4)
    return timetable.grid[classroom][day][slot], classroom, day, slot

def swap_lectures(timetable, lecture_1, lecture_2):
    c1 = lecture_1[1:4]
    c2 = lecture_2[1:4]
    timetable.grid[c1[0]][c1[1]][c1[2]], timetable.grid[c2[0]][c2[1]][c2[2]] = timetable.grid[c2[0]][c2[1]][c2[2]], timetable.grid[c1[0]][c1[1]][c1[2]]
    # print(c1, c2)
