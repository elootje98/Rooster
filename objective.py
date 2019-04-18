import data as d
import rooster as r
"""
All function that calculate the rooster score are in this file.
"""


# Main function that calculates total score of schedule
def objective_function(rooster):

    points = day_check(rooster) + spread_check(rooster)
    print("points ", points)

    return points


#
def day_check(rooster):

    points = 0
    for day in range(5):

        # All courses on a given day
        courses_day = []

        for slot in range(4):
            for classroom in range(7):
                courses_day.append(r.get_lecture(rooster.grid[classroom][day][slot]).course)

        # Sorts list of courses alphabetically
        sorted(courses_day)

        for i in range(len(courses_day)):
            if courses_day[i] == courses_day[i - 1]:
                points -= 10

    return points


#
def spread_check(rooster):

    points = 0
    for course in rooster.courses:

        length = len(course.lectures)
        day_list = []

        for lecture in course.lectures:
            day_list.append(rooster.find_lecture(lecture)[0][1])

        sorted(day_list)

        if length == 2 and (day_list == [0, 3] or day_list == [1, 4]):
            points += 20
        elif length == 3 and day_list == [0, 2, 4]:
            points += 20
        elif length == 4 and day_list == [0, 1, 3, 4]:
            points += 20

    return points
