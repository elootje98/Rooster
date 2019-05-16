import random

import numpy as np

import objective as o
from classes import empty

<<<<<<< HEAD
=======

def print_hello():
    print("Hello World!")

def greedy_hill(timetable, samples):
    # number of lectures to be swapped
    to_swap = []
    for i in range(2 * samples):
        to_swap.append(random_lecture(timetable))
    for j in range(0, len(to_swap), 2):
        # get points before and after iteration
        swap_lectures(timetable, to_swap[j], to_swap[j+1])

def hillclimber(timetable, iterations, *args):
    """Algorithm: iterating over a premade timetable, swaps two random lectures"""

    points_timetable = o.objective_function(timetable)
    functions = {'print_hello': print_hello, 'greedy': greedy_hill}

    # iterates over a range
    for i in range(iterations):
    # while (points_timetable < -100): # use if you want to iterate to a score
>>>>>>> af1aa9a254db9eee200bab3edcc3e161cc7d92d1

def print_hello():
    print("Hello World!")


def greedy_hill(timetable, samples = 200, chance = 0.1):
    if np.random.random_sample() < chance:
        # number of lectures to be swapped
        to_swap = []
        for i in range(2 * samples):
            to_swap.append(random_lecture(timetable))
        for j in range(0, len(to_swap), 2):
            # get points before and after iteration
            swap_lectures(timetable, to_swap[j], to_swap[j+1])

<<<<<<< HEAD
=======
        # execute additional functions, TODO: does not work
        for function in args:
            functions[function]()


>>>>>>> af1aa9a254db9eee200bab3edcc3e161cc7d92d1

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
<<<<<<< HEAD

def hill_climbing(timetable):
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
    after_points = o.objective_function(timetable)
    points_timetable = o.objective_function(timetable)


def hillclimber(timetable, iterations, *args):
    """Algorithm: iterating over a premade timetable, swaps two random lectures"""

    points_timetable = o.objective_function(timetable)
    functions = {'print_hello': print_hello, 'greedy': greedy_hill}

    # iterates over a range
    for i in range(iterations):
    # while (points_timetable < -100): # use if you want to iterate to a score
        hill_climbing(timetable)
        # execute additional functions, TODO: does not work
        for function in args:
            functions[function]()
=======
>>>>>>> af1aa9a254db9eee200bab3edcc3e161cc7d92d1
