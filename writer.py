import sys

import objective
from algorithms import hillclimber, multiplegreedy, random, simulatedan
from classes import timetable as tmt
from data import data


def writer():

    try:
        algorithm_1 = sys.argv[1]
    except(IndexError):
        print("Please prove an algorithm:")
        print("1: random, greedy")
        print("2: hillclimber")
        exit()

    try:
        algorithm_2 = sys.argv[2]
    except(IndexError):
        algorithm_2 = "none"

    population = int(input("Enter population size: "))
    filename = input("Enter destination file (no extension): ")

    if algorithm_2 == "hillclimber":
        iterations = int(input("Enter number of Hillclimber iterations: "))

    f = open("results/" + filename + ".csv", 'w')
    for i in range(population):
        timetable = tmt.Timetable()

        if algorithm_1 == "random":
            random.make_table(timetable)

        elif algorithm_1 == "greedy":
            greedy.make_table(timetable)

        if algorithm_2 == "hillclimber":
            hillclimber.hillclimber(timetable, iterations)

        f.write(str(int(objective.objective_function(timetable))))
        f.write(';')
        f.write('\n')

        if i % 10 == 0:
            print("writing... N =", i)

    print("Finished! N =", population)
    f.close()


writer()
