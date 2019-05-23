import numpy as np

from algorithms import greedy as grd
from algorithms import randomalg as ran
from classes import timetable as tmt


def make_table(algorithm):

    timetable = tmt.Timetable()

    if algorithm == "random":
        while not ran.make_table(timetable):
            timetable = tmt.Timetable()

    elif algorithm == "greedy":
        while not grd.make_table(timetable):
            timetable = tmt.Timetable()

    else:
        raise ValueError("Invalid algorithm:", algorithm)

    return timetable


def swap_random(timetable, chance=0):

    c1 = random_coordinates(timetable)
    c2 = random_coordinates(timetable)

    swap_lectures(timetable, c1, c2)


def swap_lectures(timetable, c1, c2, chance=0):

    lecture_1 = timetable.grid[c1[0]][c1[1]][c1[2]]
    lecture_2 = timetable.grid[c2[0]][c2[1]][c2[2]]
    score_old = timetable.score()
    if (timetable.check_restriction(lecture_1, c2[1], c2[2]) and
       timetable.check_restriction(lecture_2, c1[1], c1[2])):

        timetable = swap_coordinates(timetable, c1, c2)
        score_new = timetable.score()
        score_diff = score_new - score_old

        course_1 = timetable.find_course(lecture_1.course)
        course_2 = timetable.find_course(lecture_2.course)

        if (not timetable.check_order([course_1, course_2]) or
           (score_diff < 0 and chance < np.random.rand())):

            timetable = swap_coordinates(timetable, c1, c2)
            timetable.score()
            return timetable

    return timetable


def random_coordinates(timetable):

    while True:
        classroom = np.random.randint(0, 7)
        day = np.random.randint(0, 5)
        slot = np.random.randint(0, 5)

        if not (classroom != 5 and slot == 4):
            break

    return classroom, day, slot


def swap_coordinates(timetable, c1, c2):

    t = timetable.grid
    t[c1[0]][c1[1]][c1[2]], t[c2[0]][c2[1]][c2[2]] = \
        t[c2[0]][c2[1]][c2[2]], t[c1[0]][c1[1]][c1[2]]

    return timetable
