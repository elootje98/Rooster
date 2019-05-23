import random

import numpy as np

import objective as o
from classes import empty
from helpers import timetable_helpers as th


# def random_lecture(timetable):
#     """Returns a random lecture from the timetable grid"""
#     classroom = np.random.randint(0, 7)
#     day = np.random.randint(0, 4)
#     if classroom == 5:
#         slot = np.random.randint(0, 5)
#     else:
#         slot = np.random.randint(0, 4)
#     return timetable.grid[classroom][day][slot], classroom, day, slot
#
#
# def swap_lectures(timetable, lecture_1, lecture_2):
#     """Swaps the grid locations of the given lectures"""
#     c1 = lecture_1[1:4]
#     c2 = lecture_2[1:4]
#     timetable.grid[c1[0]][c1[1]][c1[2]], timetable.grid[c2[0]][c2[1]][c2[2]] = timetable.grid[c2[0]][c2[1]][c2[2]], timetable.grid[c1[0]][c1[1]][c1[2]]


# def hill_climbing(timetable, points_timetable):
#     # swap two random lectures
#     lecture_1 = random_lecture(timetable)
#     while lecture_1[0] == empty.Empty:
#         lecture_1 = random_lecture(timetable)
#     lecture_2 = random_lecture(timetable)
#     swap_lectures(timetable, lecture_1, lecture_2)
#     after_points = o.objective_function(timetable)
#
#     # swaps back if the number of points decreases
#     if after_points < points_timetable:
#         swap_lectures(timetable, lecture_1, lecture_2)


def hill_population(timetable, samples = 500, chance = 0.02):
    if np.random.random_sample() < chance:
        to_swap = [] # number of lectures to be swapped
        scores = [] # keep track of scores
        for i in range(2*samples):
            c = th.random_coordinates(timetable)
            to_swap.append(c)
        for j in range(0, len(to_swap), 2):
            # swap lectures, check score, swap back
            th.swap_coordinates(timetable, to_swap[j], to_swap[j+1])
            scores.append(timetable.score())
            th.swap_coordinates(timetable, to_swap[j], to_swap[j+1])
        max_score = scores.index(max(scores))
        #print(timetable.grid[to_swap[2*max_score][1]][to_swap[2*max_score][2]][to_swap[2*max_score][3]], timetable.grid[to_swap[2*max_score+1][1]][to_swap[2*max_score+1][2]][to_swap[2*max_score+1][3]])
        if max_score >= timetable.objective_score:
            th.swap_coordinates(timetable, to_swap[2*max_score], to_swap[2*max_score+1])
        #print(timetable.grid[to_swap[2*max_score][1]][to_swap[2*max_score][2]][to_swap[2*max_score][3]], timetable.grid[to_swap[2*max_score+1][1]][to_swap[2*max_score+1][2]][to_swap[2*max_score+1][3]])


def random_burst(timetable, samples = 50):
    maximum_points = 420
    minimum_points = -1400
    current_points = timetable.objective_score
    delta_points = maximum_points - current_points

    # use chance to swap multiple lectures
    chance = 0.1 * delta_points
    bound = random.uniform(0, maximum_points - minimum_points)

    if (bound < chance):
        print("burst ", chance, bound)
        to_swap = []
        for samples in range(2*samples):
            c = th.random_coordinates(timetable)
            to_swap.append(c)


        print("One: ", timetable.grid[to_swap[0][0]][to_swap[0][1]][to_swap[0][2]].course , timetable.grid[to_swap[1][0]][to_swap[1][1]][to_swap[1][2]].course, "\n")
        print("     ", timetable.grid[to_swap[2][0]][to_swap[2][1]][to_swap[2][2]].course , timetable.grid[to_swap[3][0]][to_swap[3][1]][to_swap[3][2]].course, "\n")
        print("     ", to_swap[0][0], to_swap[0][1] , to_swap[0][2], to_swap[1][0], to_swap[1][1] , to_swap[1][2])


        for k in range(0, len(to_swap), 2):
            # get points before and after iteration
            th.swap_coordinates(timetable, to_swap[k], to_swap[k+1])
            to_swap[k], to_swap[k+1] = to_swap[k+1], to_swap[k],


        print(timetable.score())
        print("Two: ", timetable.grid[to_swap[0][0]][to_swap[0][1]][to_swap[0][2]].course , timetable.grid[to_swap[1][0]][to_swap[1][1]][to_swap[1][2]].course, "\n")
        print("     ", timetable.grid[to_swap[2][0]][to_swap[2][1]][to_swap[2][2]].course , timetable.grid[to_swap[3][0]][to_swap[3][1]][to_swap[3][2]].course, "\n")
        print("     ", to_swap[0][0], to_swap[0][1] , to_swap[0][2], to_swap[1][0], to_swap[1][1] , to_swap[1][2])

        if timetable.score() < current_points:
            print(timetable.score(), current_points)


            for l in range(0, len(to_swap), 2):
                # get points before and after iteration
                th.swap_coordinates(timetable, to_swap[l], to_swap[l+1])
                to_swap[k], to_swap[k+1] = to_swap[k+1], to_swap[k]

            print(timetable.score())
            print("Three: ", timetable.grid[to_swap[0][0]][to_swap[0][1]][to_swap[0][2]].course , timetable.grid[to_swap[1][0]][to_swap[1][1]][to_swap[1][2]].course, "\n")
            print("     ", timetable.grid[to_swap[2][0]][to_swap[2][1]][to_swap[2][2]].course , timetable.grid[to_swap[3][0]][to_swap[3][1]][to_swap[3][2]].course, "\n")
            print("     ", to_swap[0][0], to_swap[0][1] , to_swap[0][2], to_swap[1][0], to_swap[1][1] , to_swap[1][2])

        else:
            print("Four: ", timetable.grid[to_swap[0][0]][to_swap[0][1]][to_swap[0][2]].course, timetable.grid[to_swap[1][0]][to_swap[1][1]][to_swap[1][2]].course, "\n")
            print("     ", timetable.grid[to_swap[2][0]][to_swap[2][1]][to_swap[2][2]].course , timetable.grid[to_swap[3][0]][to_swap[3][1]][to_swap[3][2]].course, "\n")
            print("     ", to_swap[0][0], to_swap[0][1] , to_swap[0][2], to_swap[1][0], to_swap[1][1] , to_swap[1][2])



def greedy_hill(timetable):
    current_score = 0
    for course in timetable.courses:
        for lecture in course.lectures:
            if lecture.score < current_score:
                c1 = timetable.find_slot(lecture)[0]
                current_score = timetable.grid[c1[0]][c1[1]][c1[2]].score
    print(c1, timetable.grid[c1[0]][c1[1]][c1[2]].score)
    c2 = th.random_coordinates(timetable)
    th.swap_lectures(timetable, c1, c2)



def hillclimber(timetable, iterations, *args):
    """Algorithm: iterating over a premade timetable, swaps two random lectures"""

    #points_timetable = o.objective_function(timetable)

    # iterates over a range
    for i in range(iterations):
        # apply optional added functions
        if len(args) != 0:
            for function in args[0]:
                function(timetable)
        else:
            "Wrong hillcimber arguments!"
        timetable.score()
        print(timetable.objective_score)
