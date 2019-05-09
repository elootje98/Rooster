import numpy as np
import objective_test as o
import timetable_test as t

def hillclimber (timetable):
    # check points of courses?


    # random hillclimber
    lecture = random_lecture(timetable)
    while  lecture == t.Empty:
        lecture_1 = lecture
        lecture = random_lecture(timetable)
    lecture = random_lecture(timetable)
    while lecture == t.Empty:
        lecture_2 = lecture
        lecture = random_lecture(timetable)

    # get points before and after iteration
    before_points = o.objective_function(timetable)
    swap_lectures()
    after_points = o.objective_function(timetable)
    print(before_points, after_points)



def random_lecture(timetable):
    classroom = np.random.randint(0, 7)
    day = np.random.randint(0, 4)
    slot = np.random.randint(0, 4)
    return type(timetable.grid[classroom][day][slot])

def swap_lectures(lecture_1, lecture_2):
    lecture_1, lecture_2 = lecture_2, lecture_1
