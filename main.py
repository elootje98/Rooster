import sys

import objective
import printer
from algorithms import random, hillclimber, multiplegreedy
from classes import timetable
from data import data
import sys

if len(sys.argv) < 2:
    print("Please provide an algorithm.")
    print("Correct usage: main.py algorithm 1 [, algorithm 2, added_function()]")
    print("Available algorithms #1 : random, greedy")
    print("Available algorithms #2 : hillclimber")
    print("Available added functions #3: print_hello")
    exit()

timetable = timetable.Timetable()
algorithm_1 = sys.argv[1]

if algorithm_1 == "random":
    random.make_table(timetable)

elif algorithm_1 == "greedy":
    iterations = int(input("Number of iterations for greedy: "))
    timetable = multiplegreedy.make_table(timetable, iterations)

if len(sys.argv) >= 3:
    algorithm_2 = sys.argv[2]

    if algorithm_2 == "hillclimber":
        print("Starting timetable score:", objective.objective_function(timetable))
        iterations = int(input("Number of iterations for hillclimber: "))
        if len(sys.argv) == 3:
            hillclimber.hillclimber(timetable, iterations)
        elif len(sys.argv) == 4:
            function_1 = sys.argv[3]
            hillclimber.hillclimber(timetable, iterations, function_1)

print("Timetable score:", objective.objective_function(timetable))
printer.make_table(timetable)

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
