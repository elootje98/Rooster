import random
import matplotlib.pyplot as plt

import numpy as np
import math
import objective as o
from classes import empty
import copy

def linear(temperature):
    alfa = 1
    temperature = temperature - alfa
    return temperature

def exponent(temperature):
    alfa = 0.999
    temperature = temperature * alfa
    return temperature

def logarithmic(temperature):
    alfa = 2.5
    temperature = math.log(temperature, alfa)
    return temperature

def many(timetable, iterations):

    points_all = []
    temperatures = [1000]

    #for different temperatures
    for temperature in temperatures:
        print(temperature)
        # Save all the timetables and chancetheir points
        points_max = []
        for i in range(iterations):
            compare_timetable = copy.deepcopy(timetable)
            points_max.append(simulated(compare_timetable, temperature))
        points_all.append(max(points_max))

    print("max", max(points_all))
    plt.bar(range(0, len(points_all)), points_all)
    plt.show()

def simulated(timetable, temperature):
    """Simulated annealing algorithm"""
    change_list = []
    points_list = []
    chance_list = []
    # Calculate points of current timetable
    points_timetable = o.objective_function(timetable)
    k = 0.028

    while(temperature > 0):

        # swap two random lectures
        lecture_1 = random_lecture(timetable)
        while lecture_1[0] == empty.Empty:
            #print(lecture_1[0])
            lecture_1 = random_lecture(timetable)
        lecture_2 = random_lecture(timetable)
        swap_lectures(timetable, lecture_1, lecture_2)
        after_points = o.objective_function(timetable)
        delta_points = after_points - points_timetable

        # If the timetable is not better, accept with prop.
        if delta_points < 0:

            chance = 1 - math.exp(delta_points/(k * temperature))
            chance_list.append(math.exp(-10/(k * temperature)))
            bound = random.randrange(1)
            print(delta_points)
            print("chance", chance)

            if chance < bound:
                swap_lectures(timetable, lecture_1, lecture_2)

        points_timetable = o.objective_function(timetable)
        points_list.append(points_timetable)
        temperature = exponent(temperature)

    print(points_timetable)

    plt.plot(range(0, len(chance_list)), chance_list)
    plt.show()
    return points_timetable


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
