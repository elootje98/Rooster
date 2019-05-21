import sys

import objective
import printer
from algorithms import hillclimber, multiplegreedy, randomalg, simulatedan
from classes import timetable as tmt
from data import data


def main():
    """ Main script to generate a timetable using certain algorithms.

    Main creates a timetable with either random or greedy algorithm, which can
    be chosen as the first command-line argument (random / greedy). Both can be
    expanded with hillclimber (number of iterations is prompted to user).
    Use of hillclimber can be switched on with the second command-line argument
    (hillclimber).

    """

    if len(sys.argv) < 2:
        print("Please provide an algorithm.")
        print("Correct usage: main.py algorithm 1 [, algorithm 2, added_function()]")
        print("Available algorithms #1 : random, greedy")
        print("Available algorithms #2 : hillclimber")
        print("Available added functions #3: print_hello")
        exit()

    algorithm_1 = sys.argv[1]

    timetable = tmt.Timetable()

    if algorithm_1 == "random":
        randomalg.make_table(timetable)

    if algorithm_1 == "greedy":
        iterations = 1 # int(input("Number of iterations for greedy: "))
        timetable = multiplegreedy.make_table(timetable, iterations)

    if len(sys.argv) >= 3:
        algorithm_2 = sys.argv[2]

        if algorithm_2 == "siman":
            simulatedan.simulated(timetable)

        if algorithm_2 == "hillclimber":
            print("Starting timetable score:", objective.objective_function(timetable))
            iterations = int(input("Number of iterations for hillclimber: "))
            if len(sys.argv) == 3:
                hillclimber.hillclimber(timetable, iterations)
            elif len(sys.argv) == 4:
                function_1 = sys.argv[3]
                hillclimber.hillclimber(timetable, iterations, function_1)

    print("Timetable score:", objective.objective_function(timetable))
    # printer.make_table(timetable)

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
