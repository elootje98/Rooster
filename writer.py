import sys

from helpers import objective
from algorithms import hillclimber, greedy, randomalg, ppa
from classes import timetable as tmt
from data import data
from helpers import timetable_helpers as hlp


def writer():

    try:
        algorithm_1 = sys.argv[1]
    except(IndexError):
        print("Please prove an algorithm:")
        print("1: random, greedy, ppa")
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

        if algorithm_1 == "random":
            succesful = False
            while not succesful:
                timetable = tmt.Timetable()
                succesful = randomalg.make_table(timetable)

                if not succesful:
                    print("Not succesful")

        elif algorithm_1 == "greedy":
            succesful = False
            while not succesful:
                timetable = tmt.Timetable()
                succesful = greedy.make_table(timetable)

                if not succesful:
                    print("Not succesful")

        elif algorithm_1 == "ppa":
            timetable = ppa.make_table()

        if algorithm_2 == "hillclimber":
            hillclimber.hillclimber(timetable, iterations, [hlp.swap_random])

        f.write(str(int(objective.objective_function(timetable))))
        f.write(';')
        f.write('\n')

        if i % 10 == 0:
            print("writing... N =", i)

    print("Finished! N =", population)
    f.close()


writer()
