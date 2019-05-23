import copy
import math
import random

from algorithms import randomalg as ran
from classes import timetable as tmt
from helpers import timetable_helpers as hlp

POPULATION = 20
GENERATIONS = 30
LOWER_BOUND = -1400
UPPER_BOUND = 500
NUMBER_PARAMETER = 3
RUN_PARAMETER = 500


def make_table():
    timetable_list = []

    for i in range(POPULATION):
        timetable = hlp.make_table("random")
        timetable_list.append(timetable)
        print("Population:", i)

    for j in range(GENERATIONS):
        offspring_list = []
        print("Generation", j)
        print("Lenght:", len(timetable_list))

        for timetable in timetable_list:
            score = timetable.objective_score

            for k in range(offspring_number(score)):
                offspring = copy.deepcopy(timetable)
                swap_lectures(offspring, offspring_iterations(score))
                offspring.score()
                offspring_list.append(offspring)

        print("\nTimetable list:\n")
        for i in range(len(timetable_list)):
            print(timetable_list[i].objective_score)
        print("\nOffspring list:\n")
        for j in range(len(offspring_list)):
            print(offspring_list[j].objective_score)

        timetable_list = timetable_list + offspring_list
        timetable_list.sort(key=lambda table: table.objective_score,
                            reverse=True)

        timetable_list = timetable_list[0:POPULATION]

    return timetable_list[0]


def offspring_number(score):

    number = NUMBER_PARAMETER * adapted_fitness(score) * random.random()

    return math.ceil(number)


def offspring_iterations(score):

    iterations = RUN_PARAMETER * (1 - adapted_fitness(score)) * random.random()

    return math.ceil(iterations)


def adapted_fitness(score):

    normalized_fitness = (UPPER_BOUND - score) / (UPPER_BOUND - LOWER_BOUND)
    adapted_fitness = (math.tanh(4 * (normalized_fitness - 2)) + 1) / 2

    return adapted_fitness


def swap_lectures(timetable, swaps):

    for i in range(swaps):
        timetable = hlp.swap_random(timetable)
