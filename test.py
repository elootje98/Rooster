from algorithms import simulated_annealing as sa
from algorithms import randomalg as ra
from algorithms import ppa
from helpers import timetable_helpers as th

timetable = ppa.make_table()
print(timetable.objective_score)
