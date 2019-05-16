from algorithms import greedy
from objective import objective_function
import copy

def make_table(timetable, iterations):

    # Save all the timetables and their points
    points = -10000
    for i in range(iterations):
        compare_timetable = copy.deepcopy(timetable)
        greedy.make_table(compare_timetable)
        new_points = objective_function(compare_timetable)
        if new_points > points:
            new_timetable = copy.deepcopy(compare_timetable)
            points = new_points

    # Select the timetable with the hightest points
    return copy.deepcopy(new_timetable)
