import matplotlib.pyplot as plt
import numpy as np

from helpers import timetable_helpers as hlp

TEMPERATURE = 100


def make_table(iterations, cooling):

    temp = TEMPERATURE
    timetable = hlp.make_table("random")
    plot_list = []
    temp_list = []
    chance_list = []

    for i in range(iterations):
        if cooling == "hillclimber":
            timetable = hlp.swap_random(timetable)
        else:
            timetable = hlp.swap_random(timetable, sa=True, T=temp)

        if cooling == "linear":
            temp = linear(iterations, i)

        elif cooling == "exponential":
            temp = exponential(iterations, i)

        elif cooling == "sigmoidal":
            temp = sigmoidal(iterations, i)

        plot_list.append(timetable.objective_score)
        temp_list.append(temp)
        chance_list.append(np.exp(-10 / (0.4 * temp)))

    return plot_list, temp_list, chance_list


def linear(iterations, i):

    temp = TEMPERATURE - i * ((TEMPERATURE - 1) / iterations)

    return temp


def exponential(iterations, i):

    temp = TEMPERATURE * np.float_power((1 / TEMPERATURE), (i / iterations))

    return temp


def sigmoidal(iterations, i):

    temp = 1 + (100 - 1) / (1 + np.exp(0.1 * (i - iterations / 2)))

    return temp
