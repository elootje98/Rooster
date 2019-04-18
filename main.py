from data import data as d
import numpy as np
import objective as o
import rooster as r
from algorithms import random as a

rooster = r.Rooster(d.courses, d.lectures, d.classrooms)

rooster.sort()
a.make_grid(rooster)


print(rooster.grid)
o.objective_function(rooster)
