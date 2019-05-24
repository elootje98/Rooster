import sys

from helpers import objective, printer
from algorithms import hillclimber, greedy, randomalg, simulated_annealing
from classes import timetable as tmt
from data import data
from helpers import timetable_helpers as th
import copy

available_algorithms1 = ["random", "greedy"]
available_algorithms2 = ["hillclimber"] # TODO add other algo's
hill_functions = {'hillclimber': th.swap_random, 'greedy_hill': hillclimber.greedy_hill, 'pop': hillclimber.hill_population, 'burst': hillclimber.random_burst}
helper_functions = {"print": printer.make_table} # TODO add writer


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
        print("Correct usage: main.py algorithm 1 [, algorithm 2, *added_functions, *helper_functions]")
        print("Available algorithms #1 : " + ", ".join([str(a) for a in available_algorithms1]))
        print("Available algorithms #2 : " + ", ".join([str(a) for a in available_algorithms2]))
        print("Available added hillclimber functions: " + ", ".join([str(key) for key in hill_functions]))
        print("Available added helper functions: " + ", ".join([str(key) for key in helper_functions]))
        exit()

    algorithm_1 = sys.argv[1]

    timetable = tmt.Timetable()

    if algorithm_1 == "random":
        randomalg.make_table(timetable)

    if algorithm_1 == "greedy":
        greedy.make_table(timetable)

    if algorithm_1 == "multi":
        algorithm = input("Algorithm: ")
        iterations = int(input("Number of iterations: "))
        multi_table(timetable, iterations, algorithm)

    if len(sys.argv) >= 3:
        algorithm_2 = sys.argv[2]
        print("Starting timetable score:", objective.objective_function(timetable))

        if algorithm_2 == "siman":
            simulated_anealing.simulated(timetable, 1000)

        if algorithm_2 == "hillclimber" or algorithm_2 == "greedy_hill":
            iterations = int(input("Number of iterations for hillclimber: "))

            hill_functions_applied = [hill_functions[f] for f in sys.argv if f in hill_functions]
            hillclimber.hillclimber(timetable, iterations, hill_functions_applied)

        # Applies helper functions added to the command line as args
        helper_functions_applied = [helper_functions[f] for f in sys.argv[-len(helper_functions):] if f in helper_functions]
        for function in helper_functions_applied:
            function(timetable)


    print("Timetable score:", objective.objective_function(timetable))

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
                raise ValueError("Invalid algorithm", cooling)

            new_points = objective_function(compare_timetable)
            if new_points > points:
                new_timetable = copy.deepcopy(compare_timetable)
                points = new_points

        # Select the timetable with the hightest points
        return copy.deepcopy(new_timetable)

    # Recheck de score voor de individuele vakken
    # rechecked_score = 0 # TODO: weghalen of netter neerzetten later
    # for classroom in range(7):
    #     for day in range(5):
    #         for slot in range(5):
    #             try:
    #                 rechecked_score += timetable.grid[classroom][day][slot].score
    #             except(AttributeError):
    #                 pass
    #
    # print("Timetable rechecked_score:", rechecked_score)


    # ## Prints out all lectures made in ID order
    #
    # for course in timetable.courses:
    #     print(course.name, '\n')
    #
    #     for lecture in course.lectures:
    #         print(lecture.id, lecture.course, lecture.type, lecture.students, lecture.capacity)
    #
    #     print('\n', "Restrictions:", '\n')
    #
    #     for entry in course.restricted:
    #         print(entry)
    #
    #     print('\n')

    # ## Prints out all lectures in timetable
    #
    # for i in range(0,7):
    #     for j in range(0, 5):
    #         for k in range(0, 5):
    #             print(timetable.grid[i][j][k].course)


main()
