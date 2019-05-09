import timetable_test as t
from data import data_test as d

"""
All function that calculate the timetable score are in this file.
"""


# Main function that calculates total score of schedule
def objective_function(timetable):

    return (day_check(timetable) + spread_check(timetable) +
            students_check(timetable) + nightslot_check(timetable))


# Checks if lectures of the same course are planned on the same day
def day_check(timetable):

    points = 0
    for day in range(5):

        # All courses on a given day
        courses_day = []

        for slot in range(4):
            for classroom in range(7):
                courses_day.append(timetable.grid[classroom][day][slot].course)

        # Sorts list of courses alphabetically
        courses_day.sort()

        for i in range(len(courses_day)):
            if courses_day[i] == courses_day[i - 1]:
                points -= 10

    return points

# Cheks optimal spread, uses 'tracks' to divide points
def spread_check(timetable):

    points = 0

    for course in timetable.courses:
        count = 0
        list_HC = []
        list_WC = []
        list_PR = []
        found_WC = False
        found_PR = False

        for lecture in course.lectures:
            if lecture.type == "HC":
                count += 1
                list_HC.append(timetable.find_slot(lecture)[0][1])
            elif lecture.type == "WC":
                found_WC = True
                list_WC.append(timetable.find_slot(lecture)[0][1])
            elif lecture.type == "PR":
                found_PR = True
                list_PR.append(timetable.find_slot(lecture)[0][1])

        list_HC.sort()
        list_WC.sort()
        list_PR.sort()
        l1 = len(list_WC + list_PR)
        l2 = l1 / 2

        if found_WC:
            count += 1
        if found_PR:
            count += 1

        if count == 2:

            if len(list_HC) == 2:
                if list_HC == ([0, 3] or [1, 4]):
                    points += 20

            elif len(list_HC) == 1:
                if 0 in list_HC:
                    points += 20.0 * (list_WC + list_PR).count(3) / l1
                elif 1 in list_HC:
                    points += 20.0 * (list_WC + list_PR).count(4) / l1
                elif 3 in list_HC:
                    points += 20.0 * (list_WC + list_PR).count(0) / l1
                elif 4 in list_HC:
                    points += 20.0 * (list_WC + list_PR).count(1) / l1

        elif count == 3:

            if len(list_HC) == 2:
                if list_HC == [0, 2]:
                    points += 20.0 * (list_WC + list_PR).count(4) / l1
                elif list_HC == [0, 4]:
                    points += 20.0 * (list_WC + list_PR).count(2) / l1
                elif list_HC == [2, 4]:
                    points += 20.0 * (list_WC + list_PR).count(0) / l1

            elif len(list_HC) == 1:
                if list_HC == [0]:
                    points += 20.0 * counter(list_PR, list_WC, 2, 4) / l2
                elif list_HC == [2]:
                    points += 20.0 * counter(list_PR, list_WC, 0, 4) / l2
                elif list_HC == [4]:
                    points += 20.0 * counter(list_PR, list_WC, 0, 2) / l2

        elif count == 4:
            if list_HC == [0, 1]:
                points += 20.0 * counter(list_PR, list_WC, 3, 4) / l2
            elif list_HC == [1, 3]:
                points += 20.0 * counter(list_PR, list_WC, 0, 4) / l2
            elif list_HC == [3, 4]:
                points += 20.0 * counter(list_PR, list_WC, 0, 1) / l2

        # print(course.name, list_HC, list_WC, list_PR, points)

    return points


# Helper function for spread_check
def counter(list_PR, list_WC, spot_1, spot_2):

    return (min(list_WC.count(spot_1), list_PR.count(spot_2)) +
            min(list_WC.count(spot_2), list_PR.count(spot_1)))


# Checks surplus of students for all lectures
def students_check(timetable):

    points = 0
    for course in timetable.courses:
        for lecture in course.lectures:
            room = timetable.find_slot(lecture)[0][0]

            margin = timetable.classrooms[room].capacity - lecture.students

            if margin < 0:
                points += margin

    return points


# Checks use of night slot
def nightslot_check(timetable):

    points = 0
    for day in range(5):
        if timetable.grid[5][day][4].course != ("empty"):
            points -= 20

    return points
