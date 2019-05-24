import random

import numpy as np

import helpers.objective as o
from classes import empty
from helpers import timetable_helpers as th


def hill_population(timetable):
    """ Genetic algorithm, finds the best swap for a population.

    An additional function to the hillclimber. Generates a population of
    samples, of which in turn two lectures are swapped and the score of the
    timetable after the swap is compared to the score before the swap. Scores
    are saved before swapping the lectures back. The swap resulting in the
    highest score is executed again.

    Arguments:
        timetable (Timetable): Timetable to modify.

    """
    # State the number of swaps to be made and chance to swap
    samples = 500
    chance = 0.02
    if np.random.random_sample() < chance:
        to_swap = []
        scores = []

        # Number of lectures is twice as large as the number of swaps.
        for i in range(2*samples):
            c = th.random_coordinates(timetable)
            to_swap.append(c)

        # Iterate in steps of 2 in order to swap only two lectures
        for j in range(0, len(to_swap), 2):
            th.swap_coordinates(timetable, to_swap[j], to_swap[j+1])
            scores.append(timetable.score())
            th.swap_coordinates(timetable, to_swap[j], to_swap[j+1])
        max_score = scores.index(max(scores))

        # Re-execute swap with the highest score
        if max_score >= timetable.objective_score:
            th.swap_coordinates(timetable, to_swap[2*max_score], to_swap[2*max_score+1])


def random_burst(timetable, samples = 50):
    """ Takes a list of sample lectures that randomly swaps, also if the score
    is influenced negatively.

    Uses a chance that is proportionate to the difference between the current
    timetable score and  the maximum score on the total range of scores.

    Arguments:
        timetable (Timetable): Timetable to modify.

    """

    maximum_points = 420
    minimum_points = -1400
    current_points = timetable.objective_score
    delta_points = maximum_points - current_points

    # Use chance to swap multiple lectures
    chance = 0.005 * delta_points
    bound = random.uniform(0, maximum_points - minimum_points)
    if (bound < chance):
        to_swap = []
        for samples in range(2*samples):
            c = th.random_coordinates(timetable)
            to_swap.append(c)

        for k in range(0, len(to_swap), 2):
            th.swap_coordinates(timetable, to_swap[k], to_swap[k+1])


def greedy_hill(timetable):
    """ Use greedy to swap lecture with the lowest score.

    A version of the hillclimber algorithm that swaps the lecture with the
    lowest score with a random other lecture.

    Arguments:
        timetable (Timetable): Timetable to modify.

    """

    # Variable to compare lecture score with current lowest lecture found
    current_score = 100

    # Iterate over all lectures to find the lecture with the lowest score
    for course in timetable.courses:
        for lecture in course.lectures:
            if lecture.score < current_score:
                c1 = timetable.find_slot(lecture)[0]
                current_score = timetable.grid[c1[0]][c1[1]][c1[2]].score
    #print(c1, timetable.grid[c1[0]][c1[1]][c1[2]].score) #TODO weghalen later
    # Get random second lecture and swap the two lectures
    c2 = th.random_coordinates(timetable)
    th.swap_lectures(timetable, c1, c2)



def hillclimber(timetable, iterations, *args):
    """ Use hillclimber algorithm to iterate over a timetable.

    A list of functions specifies how this hillclimber will run. The hillclimber
    can be a random hillclimber, a greedy hillclimber or a combination of both.
    Functions - of which the function names can be added as command line -
    arguments will be applied during the iteration process of the hillclimber.

    Arguments:
        timetable (Timetable): Timetable to modify.
        iterations (int): Number of iterations the hillclimber will do.
        *args (list):

    """

    # Iterates over a specified range
    for i in range(iterations):

        # Apply optional added functions.
        for function in args[0]:
            function(timetable)
        timetable.score()
        #print(timetable.objective_score) TODO weghalen
