import copy
import math
import random

from algorithms import randomalg as ran
from classes import timetable as tmt
from helpers import timetable_helpers as hlp

""" Parameters for Plant Propagation Algorithm. """

POPULATION = 20
GENERATIONS = 30
LOWER_BOUND = -1400
UPPER_BOUND = 500
NUMBER_PARAMETER = 3
RUN_PARAMETER = 500


def make_table():
    """ Main function for Plant Propagation Algorithm.

    Plant propagation initializes a population of timetables for a given size.
    The timetables are assigned an 'adapted fitness' based on their score. The
    adapted fitness is used to calcule the number of child timetables to be
    made with a certain amount of hillclimber iterations. The number of
    iterations also depends on the adapted fitness of the timetables. After
    creating the child tables, the tables with the highest score are grouped
    into another population with the original size. This cycle is one
    generation and repeated a number of times. Finally the highest scoring
    table of the final generation is returned.

    Returns:
        timetable (Timetable): The final timetable.

    """

    # Generates initial population
    timetable_list = []
    for i in range(POPULATION):
        timetable = hlp.make_table("random")
        timetable_list.append(timetable)

    for j in range(GENERATIONS):
        offspring_list = []
        print("Calculating...  Generation:", j)

        for timetable in timetable_list:
            score = timetable.objective_score

            # Creates child tables with varying amount of iterations
            for k in range(offspring_number(score)):
                offspring = copy.deepcopy(timetable)
                swap_lectures(offspring, offspring_iterations(score))
                offspring.score()
                offspring_list.append(offspring)

        # Join initial and new timetables and sort
        timetable_list = timetable_list + offspring_list
        timetable_list.sort(key=lambda table: table.objective_score,
                            reverse=True)

        # Select the best tables and set new initial population
        timetable_list = timetable_list[0:POPULATION]

    return timetable_list[0]


def offspring_number(score):
    """ Calculates the number of child tables to be made. """

    number = NUMBER_PARAMETER * adapted_fitness(score) * random.random()

    return math.ceil(number)


def offspring_iterations(score):
    """ Calculates the number of hillclimber iterations to be made. """

    iterations = RUN_PARAMETER * (1 - adapted_fitness(score)) * random.random()

    return math.ceil(iterations)


def adapted_fitness(score):
    """ Calculates the adapted fitness of a table based on its score. """

    normalized_fitness = (UPPER_BOUND - score) / (UPPER_BOUND - LOWER_BOUND)
    adapted_fitness = (math.tanh(4 * (normalized_fitness - 2)) + 1) / 2

    return adapted_fitness


def swap_lectures(timetable, swaps):
    """ Calls the random swap method a number of times. """

    for i in range(swaps):
        timetable = hlp.swap_random(timetable)
