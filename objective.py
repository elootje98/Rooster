from classes import timetable as t
from data import data as d

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
                list_WC.append(lecture)
            elif lecture.type == "PR":
                found_PR = True
                list_PR.append(lecture)

        if found_WC:
            count += 1
        if found_PR:
            count += 1

        list_HC.sort()
        tracks = max(len(list_WC), len(list_PR))

        list_WC.sort(key=lambda lecture: lecture.track)
        for i in range(len(list_WC)):
            list_WC[i] = timetable.find_slot(list_WC[i])[0][1]
        list_PR.sort(key=lambda lecture: lecture.track)
        for i in range(len(list_PR)):
            list_PR[i] = timetable.find_slot(list_PR[i])[0][1]

        if count == 2:

            if len(list_HC) == 2:
                if list_HC == ([0, 3] or [1, 4]):
                    points += 20

            elif len(list_HC) == 1:
                if list_HC == [0]:
                    points += check_track_one(tracks, list_WC, list_PR, 3)

                if list_HC == [1]:
                    points += check_track_one(tracks, list_WC, list_PR, 4)

        elif count == 3:

            if list_HC == [0, 2]:
                points += check_track_one(tracks, list_WC, list_PR, 4)

            if list_HC == [0]:
                points += check_track_two(tracks, list_WC, list_PR, 2, 4)

        elif count == 4:

            if list_HC == [0, 1]:
                points += check_track_two(tracks, list_WC, list_PR, 3, 4)

    return points


def check_track_one(tracks, list_WC, list_PR, day):
    points = 0

    for track in range(tracks):
        try:
            if list_WC[track] == day:
                points += 20 / tracks
        except(IndexError):
            if list_PR[track] == day:
                points += 20 / tracks

    return points


def check_track_two(tracks, list_WC, list_PR, day_1, day_2):
    points = 0

    for track in range(tracks):
        if ((list_WC[track] == day_1 and list_PR[track] == day_2) or
           (list_WC[track] == day_2 and list_PR[track] == day_1)):
            points += 20 / tracks

    return points


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
