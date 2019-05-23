from helpers import timetable_helpers as x
from algorithms import simulated_annealing as sa
import printer
import matplotlib.pyplot as plt

plot, temp, chance = sa.make_table(50000, "hillclimber")

plt.figure()
plt.plot(plot)

# plt.figure()
# plt.plot(temp)
#
# plt.figure()
# plt.plot(chance)

plt.show()
