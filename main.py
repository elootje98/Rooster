import copy
import sys

from algorithms import greedy as grd
from algorithms import hillclimber as hc
from algorithms import ppa
from algorithms import randomalg as rnd
from algorithms import simulated_annealing as sa
from classes import timetable as tmt
from helpers import objective, printer
from helpers import timetable_helpers as th
from helpers import visualize

available_algorithms1 = ["random", "greedy", "multi"]
available_algorithms2 = ["hillclimber", "sa", "ppa"]


def multi_table(timetable, iterations, algorithm):
    """ Function that runs algorithm_1 multiple times returns timetable with
    the highest score.

    Arguments:
        timetable (Timetable): Timetable to fill in.
        iterations (int): Total number of initial timetables to compare.
        algorithm (string): Algorithm used to create initial timetables.

    Returns:
        timetable (Timetable): Filled in timetable.

    """

    points = -10000  # Arbitrary low value as initial value.

    for i in range(iterations):

        # Copy initial timetable for comparison.
        compare_timetable = copy.deepcopy(timetable)

        if algorithm == "random":
            rnd.make_table(compare_timetable)
        elif algorithm == "greedy":
            grd.make_table(compare_timetable)
        else:
            raise ValueError("Invalid algorithm ", algorithm)

        # Set new_timetable if compare_timetable has a higher score.
        new_points = objective.objective_function(compare_timetable)
        if new_points > points:
            new_timetable = copy.deepcopy(compare_timetable)
            points = new_points

    # Return the timetable with the hightest points.
    return copy.deepcopy(new_timetable)


def to_print_question():

    while True:
        print_function = input("Execute print function (yes / no): ")

        if print_function != "yes" and print_function != "no":
            print("You can only pick yes and no.")
            continue
        else:
            break

    return print_function


def is_it_int():

    while True:
        try:
            iterations = int(input("Number of iterations: "))
        except(Exception):
            iterations = 0.0

        if not isinstance(iterations, int):
            print("You must provide an int.")
            continue
        else:
            break

    return iterations


def main():
    """ Main script to generate a timetable using certain algorithms.

    Main creates a timetable with either random or greedy algorithm, which can
    be chosen as the first command-line argument (random / greedy). Both can be
    expanded with hillclimber (number of iterations is prompted to user).
    Use of hillclimber can be switched on with the second command-line argument
    (hillclimber).

    """
    # Check if arguments given are valid
    for arg in sys.argv[1:]:
        if (arg not in available_algorithms1 and
           arg not in available_algorithms2):
            print("Invalid input, run: $ main.py to refer to correct input.")
            return

    if len(sys.argv) < 2:
        print("Please provide an algorithm.")
        print("Correct usage: main.py algorithm 1 (algorithm 2)")
        print("Available algorithms #1 : " + ", ".join([str(a) for a in available_algorithms1]))
        print("Available algorithms #2 : " + ", ".join([str(a) for a in available_algorithms2]))
        exit()

    algorithm_1 = sys.argv[1]

    timetable = tmt.Timetable()

    if algorithm_1 == "random":
        rnd.make_table(timetable)

    elif algorithm_1 == "greedy":
        grd.make_table(timetable)

    elif algorithm_1 == "multi":
        while True:
            algorithm = input("Choose between greedy and random: ")

            if algorithm != "greedy" and algorithm != "random":
                print("You can only choose between 'greedy' and 'random'.")
                continue
            else:
                break

        iterations = is_it_int()
        timetable = multi_table(timetable, iterations, algorithm)

    if len(sys.argv) == 2:
        print_function = to_print_question()
        visual_function = "no"

    if len(sys.argv) >= 3:
        algorithm_2 = sys.argv[2]
        print("Starting timetable score:", objective.objective_function(timetable))

        if algorithm_2 == "sa":
            iterations = int(is_it_int())

            while True:
                cooling = input("Cooling scheme (linear, exponential, sigmoidal): ")

                if cooling not in ["linear", "exponential", "sigmoidal"]:
                    print("You can only choose: linear, exponential and sigmoidal")
                    continue
                else:
                    break

            while True:
                reheat_option = input("Reheating? (yes / no): ")

                if reheat_option != "yes" and reheat_option != "no":
                    print("You can only choose: yes or no.")
                    continue
                else:
                    break

            if reheat_option == "yes":

                while True:
                    try:
                        reheating = int(input("Reheating at temperature (int): "))
                    except(Exception):
                        reheating = 0.0

                    if not isinstance(reheating, int):
                        print("You must provide an int.")
                        continue
                    else:
                        break

                scores = sa.make_table(timetable, iterations, cooling, reheating)
            else:
                scores = sa.make_table(timetable, iterations, cooling)
            labels = ["Simmulated Annealing"]

        if algorithm_2 == "hillclimber":

            while True:
                function = input("Choose hillclimber type (regular, greedyhill, combined): ")

                if function not in ["regular", "greedyhill", "combined"]:
                    print("You must choose between regular, greedyhill or combined.")
                    continue
                else:
                    break

            while True:
                optional = input("Choose optional (none, pop, burst, combined): ")

                if optional not in ["none", "pop", "burst", "combined"]:
                    print("You can only choose between none, pop, burst or combined.")
                    continue
                else:
                    break

            while True:
                iterations = int(input("Number of iterations for hillclimber: "))

                if not isinstance(iterations, int):
                    print("You must provide an int.")
                    continue
                else:
                    break

            labels = []

            hill_functions_applied = []
            if function == "regular":
                hill_functions_applied.append(th.swap_random)
                labels.append("Hillclimber")
            elif function == "greedyhill":
                hill_functions_applied.append(hc.greedy_hill)
                labels.append("GreedyHill")
            elif function == "combined":
                hill_functions_applied.append(th.swap_random)
                hill_functions_applied.append(hc.greedy_hill)
                labels.append("Hillclimber")
                labels.append("GreedyHill")
            else:
                print("Invalid input.")
                return

            if optional == "none":
                pass
            elif optional == "pop":
                hill_functions_applied.append(hc.hill_population)
                labels.append("Pop")
            elif optional == "burst":
                hill_functions_applied.append(hc.random_burst)
                labels.append("Burst")
            elif optional == "combined":
                hill_functions_applied.append(hc.hill_population)
                hill_functions_applied.append(hc.random_burst)
                labels.append("Pop")
                labels.append("Burst")
            else:
                print("Invalid input.")
                return

            scores = hc.hillclimber(timetable, iterations,
                                    hill_functions_applied)

        if algorithm_2 == "ppa":
            ppa.make_table()

            print_function = print_function = to_print_question()
            visual_function == "no"
        else:
            print_function = print_function = to_print_question()
            visual_function = input("Execute visual function (yes / no): ")

            while visual_function not in ["yes", "no"]:
                print("No valid input.")
                visual_function = input("Execute visual function (yes / no): ")

    if print_function == "yes":
        printer.make_table(timetable)

    if visual_function == "yes":
        visualize.make_plot(labels, scores)

    print("Timetable score:", objective.objective_function(timetable))


main()
