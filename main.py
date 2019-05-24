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

    points = -10000 # Arbitrary low value as initial value.

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
    print_function = input("Execute print function (yes / no): ")

    if print_function != "yes" and print_function != "no":
        print("No vallid input.")
        print_function = "no"

    return print_function


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
            print("Wrong input, run: $ main.py to refer to correct input.")
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
        print_function = to_print_question()
        visual_function = "no"


    if algorithm_1 == "greedy":
        grd.make_table(timetable)
        print_function = to_print_question()
        visual_function = "no"

    if algorithm_1 == "multi":
        algorithm = input("Algorithm: ")
        iterations = int(input("Number of iterations: "))
        timetable = multi_table(timetable, iterations, algorithm)
        print_function = print_function = to_print_question()
        visual_function = "no"


    if len(sys.argv) >= 3:
        algorithm_2 = sys.argv[2]
        print("Starting timetable score:", objective.objective_function(timetable))

        if algorithm_2 == "sa":
            iterations = int(input("Number of iterations: "))
            cooling = input("Cooling scheme (linear, exponential, sigmoidal) ")
            reheat_option = input("Reheating? (yes / no): ")
            if reheat_option == "yes":
                reheating = int(input("Reheating at temperature (int): "))
                scores = sa.make_table(timetable, iterations, cooling, reheating)
            else:
                scores = sa.make_table(timetable, iterations, cooling)
            labels = ["Simmulated Annealing"]

        if algorithm_2 == "hillclimber":
            function = input("Choose hillclimber type (regular, greedyhill, combined): ")
            optional = input("Choose optional (none, pop, burst, combined): ")
            iterations = int(input("Number of iterations for hillclimber: "))
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
            if visual_function != "yes" and visual_function != "no":
                    print("No vallid input.")
                    visual_function = "no"


    if print_function == "yes":
        printer.make_table(timetable)
    if visual_function == "yes":
        visualize.make_plot(labels, scores)

    print("Timetable score:", objective.objective_function(timetable))



main()
