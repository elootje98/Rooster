from data import data as d
import numpy as np
import objective as o
import timetable as t
import printer as p
from algorithms import random as a
<<<<<<< HEAD
from algorithms import hillclimber as hill
=======
from algorithms import greedy as g
>>>>>>> 8e6fcca98c84c3ae042f6bd25c28e780155bcc7b

timetable = t.Timetable(d.courses, d.lectures, d.classrooms)
timetable.make_children()
timetable.assign_children()
timetable.sort()

#a.make_grid(timetable)

g.give_points_lectures()
# print(timetable.grid)
# o.objective_function(timetable)



<<<<<<< HEAD
p.make_table(timetable)
hill.hillclimber(timetable)
=======
#p.make_table(timetable)
>>>>>>> 8e6fcca98c84c3ae042f6bd25c28e780155bcc7b
