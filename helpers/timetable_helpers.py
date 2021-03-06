import numpy as np

from algorithms import greedy as grd
from algorithms import randomalg as ran
from classes import timetable as tmt


def make_table(algorithm):
    """ Make an initial table either randomly or using the greedy algorithm.

    The algorithm that is used to build a table is taken from the 2nd command
    line argument (args[1]). Both a random and greedy algorithm are available
    to build the timetable. However, greedy is also based on a random

    Arguments:
        algorithm (String): Algorithm used to build the table

    Returns:
        timetable (Timetable): Timetable to modify.

    """

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
    """ Function used to swap a random lecture.

    A function that generates two random coordinates corresponding to lectures
    in the timetable. Calls swap_lectures to execute the actual swap.

    Arguments:
        timetable (Timetable): Timetable to modify.
        chance (int): Chance to keep the current state of the timetable if a
            swap negatively influences the score.
        sa (bool): Indicates whether simmulated annealing calls the function.
        T (int): Temperature used by simmulated annealing algorithm.
        k (float): Parameter used in cooling process of simmulated annealing
            algoirthm.

    Returns:
        timetable (Timetable): Modified timetable.

    """

    c1 = random_coordinates(timetable)
    c2 = random_coordinates(timetable)

    timetable = swap_lectures(timetable, c1, c2, chance, sa, T, k)

    return timetable


def swap_lectures(timetable, c1, c2, chance=0, sa=False, T=0, k=0.4):
    """ Function used to swap two lectures.

    Function that executes a swap between two lectures in the timetable. Before
    executing the swap, the function checks whether a swap would violite
    constraints concerning restrictions. After swapping, the score is compared
    to the score before the swap. If the function is called by the simmulated
    annealing algorithm, a chance value is determined. The lectures are swapped
    back if the order in which the lectures occur violates order restrictions
    or if the score after the swap is lower than the score before the swap and
    the chance determined for simmulated annealing is lower than a random
    chance on the same scale.

    Arguments:
        timetable (Timetable): Timetable to modify.
        c1 (tuple): Coordinates for the first lecture to swap.
        c2 (tuple): Coordinates for the second lecture to swap.
        chance (int): Chance to keep the current state of the timetable if a
            swap negatively influences the score.
        sa (bool): Indicates whether simmulated annealing calls the function.
        T (int): Temperature used by simmulated annealing algorithm.
        k (float): Parameter used in cooling process of simmulated annealing
            algoirthm.

    Returns:
        timetable (Timetable): Modified timetable.

    """

    # Get lectures from the timetable and gets the current score.
    lecture_1 = timetable.grid[c1[0]][c1[1]][c1[2]]
    lecture_2 = timetable.grid[c2[0]][c2[1]][c2[2]]
    score_old = timetable.score()

    # Checks for restrictions between the two lectures.
    if (timetable.check_restriction(lecture_1, c2[1], c2[2]) and
       timetable.check_restriction(lecture_2, c1[1], c1[2])):

        # Swap coordinates of the lectures and calculates new score.
        timetable = swap_coordinates(timetable, c1, c2)
        score_new = timetable.score()
        score_diff = score_new - score_old

        # Of the lectures, find corresponding course objects.
        course_1 = timetable.find_course(lecture_1.course)
        course_2 = timetable.find_course(lecture_2.course)

        # Check if the function is called by the simmulated annealing algorithm
        if sa:
            chance = np.exp(score_diff / (k * T))

        # Check whether swap is not viable.
        if (not timetable.check_order([course_1, course_2]) or
           (score_diff < 0 and chance < np.random.rand())):

            # Swap back.
            timetable = swap_coordinates(timetable, c1, c2)
            timetable.score()

            return timetable

    return timetable


def random_coordinates(timetable):
    """ Generates random lecture coordinates from the timetable.

    Takes random values for classroom, day and slot, with those, coordinates
    can be generated. The function also checks that only for classroom C0.110
    (classroom with index 5 in the timetable.grid) there is a 5th timeslot.

    Arguments:
        timetable (Timetable): timetable to modify.

    Returns:
        random_coordinates (tuple): Tuple of a random classroom, day and slot.

    """

    # Loops till condition is met.
    while True:
        classroom = np.random.randint(0, 7)
        day = np.random.randint(0, 5)
        slot = np.random.randint(0, 5)

        # Condition stating that only classroom 5 has timeslot 5.
        if not (classroom != 5 and slot == 4):
            break

    return classroom, day, slot


def swap_coordinates(timetable, c1, c2):
    """ Swaps two coordinates in the timetable, by simultaneously swapping them
    for each other.

    Arguments:
        timetable (Timetable): timetable to modify.
        c1: coordinates from the first lecture.
        c2: coordinates from the second lecture.

    Returns:
        timetable (Timetable): Modified timetable.
    """

    t = timetable.grid
    t[c1[0]][c1[1]][c1[2]], t[c2[0]][c2[1]][c2[2]] = \
        t[c2[0]][c2[1]][c2[2]], t[c1[0]][c1[1]][c1[2]]

    return timetable
