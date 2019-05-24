from algorithms import ppa
from algorithms import randomalg as ra
from algorithms import simulated_annealing as sa
from helpers import timetable_helpers as th

timetable_1 = th.make_table("random")



timetable_2 = sa.make_table(timetable_1, 500, "linear", reheating=10)

print(timetable_2.objective_score)
