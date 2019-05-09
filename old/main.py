from data import data as d
import numpy as np
import objective as o
import timetable_test as t
import printer as p
from algorithms import random as a
from algorithms import hillclimber as hill
from algorithms import greedy as g

timetable = t.Timetable()

#a.make_grid(timetable)

#g.give_points_lectures()
# print(timetable.grid)
# o.objective_function(timetable)

a.make_grid(timetable)

p.make_table(timetable)
hill.hillclimber(timetable)
#p.make_table(timetable)
