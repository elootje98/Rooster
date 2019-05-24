import numpy as np

from helpers import timetable_helpers as th

""" Parameters for Simulated Annealing. """

TEMP_HIGH = 100
TEMP_LOW = 1
SIGMOIDAL_PAR = 0.01
TEMP_PAR = 0.4


def make_table(iterations, cooling):
    """ Main function for Simulated Annealing.

    Simulated Annealing tries swapping a given number of lectures, always
    accepting improvements while only accepting lower scoring timetables with
    a certain chance. The chance is an exponential function depending on the
    decrease, TEMP_PAR and temperature. The temperature decreases with the
    number of iterations, lowering the chance of accepting a decrease in
    points. The exact temperature behaviour is given by the cooling functions.

    Arguments:
        iterations (int): Total number of swaps to try.
        cooling (string): Name of cooling function to use. Possible values are
            hillclimber, linear, exponential and sigmoidal.

    Returns:
        timetable (Timetable): Final timetable.

    """

    # Sets starting temperature and generates random timetable
    temp = TEMP_HIGH
    timetable = th.make_table("random")

    for i in range(iterations):

        # Handles special hillclimber cooling scheme
        if cooling == "hillclimber":
            timetable = th.swap_random(timetable)
        else:
            timetable = th.swap_random(timetable, sa=True, T=temp, k=TEMP_PAR)

            # Adjusts temperature based of chosen cooling scheme
            if cooling == "linear":
                temp = linear(iterations, i)
            elif cooling == "exponential":
                temp = exponential(iterations, i)
            elif cooling == "sigmoidal":
                temp = sigmoidal(iterations, i)
            else:
                raise ValueError("Invalid cooling function:", cooling)

    return timetable


def linear(iterations, i):
    """ Linear cooling scheme for SA. """

    temp = TEMP_HIGH - i * ((TEMP_HIGH - TEMP_LOW) / iterations)

    return temp


def exponential(iterations, i):
    """ Exponential cooling scheme for SA. """

    temp = TEMP_HIGH * np.float_power((TEMP_LOW / TEMP_HIGH), (i / iterations))

    return temp


def sigmoidal(iterations, i):
    """ Sigmoidal cooling scheme for SA. """

    temp = (TEMP_LOW + (TEMP_HIGH - TEMP_LOW) /
            (1 + np.exp(SIGMOIDAL_PAR * (i - iterations / 2))))

    return temp
