from data import data as d
import numpy as np
import objective as o
import timetable as t
import printer as p
from algorithms import random as a
from algorithms import greedy as g

timetable = t.Timetable(d.courses, d.lectures, d.classrooms)
timetable.make_children()
timetable.assign_children()
timetable.sort()

#a.make_grid(timetable)

g.give_points_lectures()
# print(timetable.grid)
# o.objective_function(timetable)



#p.make_table(timetable)
