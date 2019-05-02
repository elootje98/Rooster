from data import data as d
import numpy as np
import objective as o
import timetable as t
import printer as p
from algorithms import random as a

timetable = t.Timetable(d.courses, d.lectures, d.classrooms)

#timetable.sort()
a.make_grid(timetable)


print(timetable.grid)
o.objective_function(timetable)

timetable.make_children()

p.make_table(timetable)
