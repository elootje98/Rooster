from algorithms import ppa
from algorithms import randomalg as ra
from algorithms import simulated_annealing as sa
from helpers import timetable_helpers as th

timetable = th.make_table("random")
timetable = sa.make_table(timetable, 500, "linear")
print(timetable.objective_score)
