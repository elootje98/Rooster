from algorithms import greedy
from objective import objective_function
import copy

def make_table(timetable, iterations):

    # Save all the timetables and their points
    points = -10000
    new_timetable = 0
    for i in range(iterations - 1):
        compare_timetable = copy.deepcopy(timetable)
        greedy.make_table(compare_timetable)
        new_points = objective_function(compare_timetable)
        print(new_points)
        if new_points > points:
            print("better: ", new_points)
            new_timetable = compare_timetable
            points = new_points

    # Select the timetable with the hightest points
    timetable = new_timetable
    print(timetable.grid)
