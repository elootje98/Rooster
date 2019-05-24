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


def swap_random(timetable, chance=0, sa=False, T=0, k=0.4):
    """Swaps two random lectures.

    It takes the coordinates from two lectures and swaps place of the two
    lectures."""

    c1 = random_coordinates(timetable)
    c2 = random_coordinates(timetable)

    timetable = swap_lectures(timetable, c1, c2, chance, sa, T, k)

    return timetable


def swap_lectures(timetable, c1, c2, chance=0, sa=False, T=0, k=0.4):

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

        if sa:
            chance = np.exp(score_diff / (k * T))

        if (not timetable.check_order([course_1, course_2]) or
           (score_diff < 0 and chance < np.random.rand())):

            timetable = swap_coordinates(timetable, c1, c2)
            timetable.score()
            return timetable

    return timetable


def random_coordinates(timetable):
    """Generates random coordinates in the timetable.

    Takes random values for classroom, day and slot, with those, coordinates
    can be generated.

    Returns: classroom, day and slot.
    """

    while True:
        classroom = np.random.randint(0, 7)
        day = np.random.randint(0, 5)
        slot = np.random.randint(0, 5)

        if not (classroom != 5 and slot == 4):
            break

    return classroom, day, slot


def swap_coordinates(timetable, c1, c2):
    """Swaps two coordinates in the timetable.

    Takes two coordinates and swaps them.
    
    Arguements:
        timetable (Timetable): timetable to modify.
        c1: coordinates from the first lecture.
        c2: coordinates from the second lecture.

    Returns:
        timetable
    """

    t = timetable.grid
    t[c1[0]][c1[1]][c1[2]], t[c2[0]][c2[1]][c2[2]] = \
        t[c2[0]][c2[1]][c2[2]], t[c1[0]][c1[1]][c1[2]]

    return timetable
