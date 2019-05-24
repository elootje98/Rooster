import copy
import sys

from algorithms import greedy as grd
from algorithms import hillclimber as hc
from algorithms import randomalg as rnd
from algorithms import simulated_annealing as sa
from algorithms import ppa
from classes import timetable as tmt
from helpers import objective, printer
from helpers import timetable_helpers as th
from helpers import visualize

available_algorithms1 = ["random", "greedy, multi"]
available_algorithms2 = ["hillclimber", "sa", "ppa"]


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
            arg not in available_algorithms2 and
            arg not in hill_functions and arg not in helper_functions):
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

    if algorithm_1 == "greedy":
        grd.make_table(timetable)

    # if algorithm_1 == "multi":
    #     algorithm = input("Algorithm: ")
    #     iterations = int(input("Number of iterations: "))
    #     multi_table(timetable, iterations, algorithm)

    if len(sys.argv) >= 3:
        algorithm_2 = sys.argv[2]
        print("Starting timetable score:", objective.objective_function(timetable))

        if algorithm_2 == "sa":
            iterations = int(input("Number of iterations: "))
            cooling = input("Cooling scheme (linear, exponential, sigmoidal) ")
            scores = sa.simulated(timetable, iterations, cooling)
            labels = ["Simmulated Annealing"]

        if algorithm_2 == "hillclimber":
            function = input("Choose hillclimber type (regular, greedyhill, combined): ")
            optional = input("Choose optional (none, pop, burst, combined): ")
            iterations = int(input("Number of iterations for hillclimber: "))
            labels = []

            hill_functions_applied = []
            if function == "regular":
                hill_functions_applied.append(th.swap_random(timetable))
                labels.append("Hillclimber")
            elif function == "greedyhill":
                hill_functions_applied.append(hc.greedy_hill(timetable))
                labels.append("GreedyHill")
            elif function == "combined":
                hill_functions_applied.append(th.swap_random(timetable))
                hill_functions_applied.append(hc.greedy_hill(timetable))
                labels.append("Hillclimber")
                labels.append("GreedyHill")
            else:
                print("Wrong input")
                return

            if optional == "none":
                pass
            elif optional == "pop":
                hill_functions_applied.append(hc.hill_population(timetable))
                labels.append("Pop")
            elif optional == "burst":
                hill_functions_applied.append(hc.random_burst(timetable))
                labels.append("Burst")
            elif optional == "combined":
                hill_functions_applied.append(hc.hill_population(timetable))
                hill_functions_applied.append(hc.random_burst(timetable))
                labels.append("Pop")
                labels.append("Burst")
            else:
                print("Wrong input")
                return

            scores = hc.hillclimber(timetable, iterations,
                                    hill_functions_applied)

        if algorithm_2 == "ppa":
            ppa.make_table()

        print("Timetable score:", objective.objective_function(timetable))
        if algorithm_2 == "ppa":
            print_function = input("Execute print function (yes / no): ")
            visual_function == "no"
        else:
            print_function = input("Execute print function (yes / no)")
            visual_function = input("Execute visual function (yes / no)")

        if print_function == "yes":
            printer.make_table(timetable)
        if visual_function == "yes":
            visualize.make_plot(labels, scores)




        # # Applies helper functions added to the command line as args
        # helper_functions_applied = [helper_functions[f] for f in sys.argv[-len(helper_functions):] if f in helper_functions]
        # for function in helper_functions_applied:
        #     if "print" in sys.argv:
        #         function(timetable)
        #     if "visual" in sys.argv:
        #         function(sys.argv[2:len(helper_functions)+1], scores)




    def multi_table(timetable, iterations, algorithm):

        # Save all the timetables and their points
        points = -10000
        for i in range(iterations):
            compare_timetable = copy.deepcopy(timetable)
            if algorithm == "random":
                randomalg.make_talbe(compare_timetable)
            elif algorithm == "greedy":
                greedy.make_table(compare_timetable)
            elif algorithm == "hillclimber":
                hillclimber.make_table(compare_timetable)
            elif algorithm == "simulated_annealing":
                simulated_annealing.make_table(compare_timetable)
            else:
                raise ValueError("Invalid algorithm", algorithm)

            new_points = objective_function(compare_timetable)
            if new_points > points:
                new_timetable = copy.deepcopy(compare_timetable)
                points = new_points

        # Select the timetable with the hightest points
        return copy.deepcopy(new_timetable)



main()
