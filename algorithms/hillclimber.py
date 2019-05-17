import random

import numpy as np

import objective as o
from classes import empty

def print_hello():
    print("Hello World!")

def random_lecture(timetable):
    """Returns a random lecture from the timetable grid"""
    classroom = np.random.randint(0, 7)
    day = np.random.randint(0, 4)
    if classroom == 5:
        slot = np.random.randint(0, 5)
    else:
        slot = np.random.randint(0, 4)
    return timetable.grid[classroom][day][slot], classroom, day, slot


def swap_lectures(timetable, lecture_1, lecture_2):
    """Swaps the grid locations of the given lectures"""
    c1 = lecture_1[1:4]
    c2 = lecture_2[1:4]
    timetable.grid[c1[0]][c1[1]][c1[2]], timetable.grid[c2[0]][c2[1]][c2[2]] = timetable.grid[c2[0]][c2[1]][c2[2]], timetable.grid[c1[0]][c1[1]][c1[2]]


def hill_climbing(timetable, points_timetable):
    # swap two random lectures
    lecture_1 = random_lecture(timetable)
    while lecture_1[0] == empty.Empty:
        lecture_1 = random_lecture(timetable)
    lecture_2 = random_lecture(timetable)
    swap_lectures(timetable, lecture_1, lecture_2)
    after_points = o.objective_function(timetable)

    # swaps back if the number of points decreases
    if after_points < points_timetable:
        swap_lectures(timetable, lecture_1, lecture_2)


def greedy_hill(timetable, points_timetable, samples = 50, chance = 0.1):
    if np.random.random_sample() < chance:
        to_swap = [] # number of lectures to be swapped
        scores = [] # keep track of scores
        for i in range(2*samples):
            to_swap.append(random_lecture(timetable))
        for j in range(0, len(to_swap), 2):
            # swap lectures, check score, swap back
            swap_lectures(timetable, to_swap[j], to_swap[j+1])
            scores.append(o.objective_function(timetable))
            swap_lectures(timetable, to_swap[j], to_swap[j+1])
        max_score = scores.index(max(scores))
        print(timetable.grid[to_swap[2*max_score][1]][to_swap[2*max_score][2]][to_swap[2*max_score][3]], timetable.grid[to_swap[2*max_score+1][1]][to_swap[2*max_score+1][2]][to_swap[2*max_score+1][3]])
        swap_lectures(timetable, to_swap[2*max_score], to_swap[2*max_score+1])
        print(timetable.grid[to_swap[2*max_score][1]][to_swap[2*max_score][2]][to_swap[2*max_score][3]], timetable.grid[to_swap[2*max_score+1][1]][to_swap[2*max_score+1][2]][to_swap[2*max_score+1][3]])


def random_burst(timetable, points_timetable, samples = 50):
    maximum_points = 380
    minimum_points = -1400
    delta_points = maximum_points - points_timetable

    # use chance to swap multiple lectures
    chance = 0.1 * delta_points
    bound = random.uniform(0, maximum_points - minimum_points)

    if (bound < chance):
        print("burst ", chance, bound)
        to_swap = []
        for samples in range(2*samples):
            to_swap.append(random_lecture(timetable))
        print("One: ", timetable.grid[to_swap[0][1]][to_swap[0][2]][to_swap[0][3]], timetable.grid[to_swap[1][1]][to_swap[1][2]][to_swap[1][3]], "\n")
        for k in range(0, len(to_swap), 2):
            # get points before and after iteration
            swap_lectures(timetable, to_swap[k], to_swap[k+1])
        print("Two: ", timetable.grid[to_swap[0][1]][to_swap[0][2]][to_swap[0][3]], timetable.grid[to_swap[1][1]][to_swap[1][2]][to_swap[1][3]], "\n")
        if o.objective_function(timetable) < points_timetable:
            print(o.objective_function(timetable), points_timetable)
            for l in range(0, len(to_swap), 2):
                # get points before and after iteration
                swap_lectures(timetable, to_swap[l], to_swap[l+1])
            print(o.objective_function(timetable))
            print("Three: ", timetable.grid[to_swap[0][1]][to_swap[0][2]][to_swap[0][3]], timetable.grid[to_swap[1][1]][to_swap[1][2]][to_swap[1][3]], "\n")
        else:
            print("Four: ", timetable.grid[to_swap[0][1]][to_swap[0][2]][to_swap[0][3]], timetable.grid[to_swap[1][1]][to_swap[1][2]][to_swap[1][3]], "\n")



def hillclimber(timetable, iterations, *args):
    """Algorithm: iterating over a premade timetable, swaps two random lectures"""

    points_timetable = o.objective_function(timetable)
    functions = {'print_hello': print_hello, 'greedy_hill': greedy_hill, 'burst': random_burst}

    # iterates over a range
    for i in range(iterations):
    # while (points_timetable < -100): # use if you want to iterate to a score
        hill_climbing(timetable, points_timetable)

        # apply optional added functions
        for function in args:
            try:
                try:
                    functions[function]()
                except TypeError:
                    functions[function](timetable, points_timetable)
            except KeyError:
                print(function + " is not a valid function.")
                return
        points_timetable = o.objective_function(timetable)
        # print(points_timetable)
