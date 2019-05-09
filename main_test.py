import sys

import timetable_test as t
from data import data_test as d
from algorithms import random_test as random


if len(sys.argv) != 2:
    print("Please provide an algorithm. Correct usage: main.py random.")
    print("Available algorithms: random.")
    exit()

algorithm = sys.argv[1]
timetable = t.Timetable()

if algorithm == "random":
    random.make_table(timetable)

# for course in timetable.courses:
#     print(course.name, '\n')
#
#     for lecture in course.lectures:
#         print(lecture.id, lecture.course, lecture.type, lecture.students, lecture.capacity)
#
#     print('\n', "Restrictions:", '\n')
#
#     for entry in course.restricted:
#         print(entry)
#
#     print('\n')

for i in range(0,7):
    for j in range(0, 5):
        for k in range(0, 4):
            print(timetable.grid[i][j][k].course)