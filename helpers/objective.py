from classes import timetable as t


def objective_function(timetable):
    """ Calculates timetable score from the objective function rules.

    Calls a method for each objective function rule to calculate the score.
    Scores are calculated for each lecture individually as well as the total
    score
    All scores are added and returned by this function.

    Arguments:
        timetable (Timetable): Timetable to calculate score of.

    Returns:
        points (int): Calculated score of all rules combined.

    """

    # Resets lectures' individual score
    reset_points(timetable)

    return (day_check(timetable) + spread_check(timetable) +
            students_check(timetable) + nightslot_check(timetable))


def day_check(timetable):
    """ Calculates timetable score for multiple lectures a day rule.

    Checks whether multiple lectures of the same course are scheduled on the
    same day. Every time this happens, 10 points are deducted from the score.
    Lectures are checked by putting all lectures of a day in a list and
    checking for duplicate courses.

    Arguments:
        timetable (Timetable): Timetable to calculate score of.

    Returns:
        points (int): Calculated score of multiple lectures a day rule.

    """

    points = 0
    for day in range(5):

        # All courses on a given day
        courses_day = []

        for slot in range(4):
            for classroom in range(7):
                courses_day.append(timetable.grid[classroom][day][slot])

        # Sorts list of courses alphabetically
        courses_day.sort(key=lambda lecture: lecture.course)

        for i in range(len(courses_day)):
            if courses_day[i].course == courses_day[i - 1].course and courses_day[i].course != "empty":
                courses_day[i].score -= 5
                courses_day[i - 1].score -= 5
                points -= 10

    return points

def spread_check(timetable):
    """ Calculates timetable score for maximum spread rule.

    Checks if lectures of a course are spread out optimally according to the
    objective function. Multiple instances of the same Werkcollege and
    Practicum are handled in their predetermined tracks. Spread is checked
    through a series of if-statements.

    Arguments:
        timetable (Timetable): Timetable to calculate score of.

    Returns:
        points (int): Calculated score of maximum spread rule.

    """

    points = 0

    for course in timetable.courses:
        count = 0
        list_HC = []
        list_WC = []
        list_PR = []
        found_WC = False
        found_PR = False

        # Loop over all the lectures in a course and put them in different
        # lists according to their type.
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

        # Sort on track and ???
        # Replace the lectures in the lists with their coordinates
        list_WC.sort(key=lambda lecture: lecture.track)
        for i in range(len(list_WC)):
            list_WC[i] = timetable.find_slot(list_WC[i])[0][1]
        list_PR.sort(key=lambda lecture: lecture.track)
        for i in range(len(list_PR)):
            list_PR[i] = timetable.find_slot(list_PR[i])[0][1]

        # Count is 2 + 2 HC ????
        # Give 10 points for the optimal spread of 4 lectures.
        if count == 2:
            if len(list_HC) == 2:
                if list_HC == ([0, 3] or [1, 4]):
                    course.lectures[0].score += 10
                    course.lectures[1].score += 10
                    points += 20

            elif len(list_HC) == 1:
                if list_HC == [0]:
                    checked_score = check_track_one(tracks, list_WC, list_PR, 3)
                    course.lectures[0].score += checked_score / 2.
                    course.lectures[1].score += checked_score / 2.
                    points += checked_score

                if list_HC == [1]:
                    checked_score = check_track_one(tracks, list_WC, list_PR, 4)
                    course.lectures[0].score += checked_score / 2.
                    course.lectures[1].score += checked_score / 2.
                    points += checked_score

        elif count == 3:

            if list_HC == [0, 2]:
                checked_score = check_track_one(tracks, list_WC, list_PR, 4)
                course.lectures[0].score += checked_score / 3.
                course.lectures[1].score += checked_score / 3.
                course.lectures[2].score += checked_score / 3.
                points += checked_score

            if list_HC == [0]:
                checked_score = check_track_two(tracks, list_WC, list_PR, 2, 4)
                course.lectures[0].score += checked_score / 3.
                course.lectures[1].score += checked_score / 3.
                course.lectures[2].score += checked_score / 3.
                points += checked_score

        elif count == 4:

            if list_HC == [0, 1]:
                checked_score = check_track_two(tracks, list_WC, list_PR, 3, 4)
                course.lectures[0].score += checked_score / 4.
                course.lectures[1].score += checked_score / 4.
                course.lectures[2].score += checked_score / 4.
                course.lectures[3].score += checked_score / 4.
                points += checked_score

    return points


def check_track_one(tracks, list_WC, list_PR, day):
    """ Checks if either WC or PR is scheduled on given day and assigns points.

    Arguments:
        tracks (int): Number of tracks.
        list_WC [int]: List of day indices for all Werkcolleges.
        list_PR [int]: List of day indices for all Practicums.
        day (int): Index of day to be checked.

    Returns:
        points (int): Calculated number of points.

    """

    points = 0

    # Loops over the tracks and gives points points if they are planned in
    # on the right day.
    for track in range(tracks):
        try:
            if list_WC[track] == day:
                points += 20 / tracks
        except(IndexError):
            if list_PR[track] == day:
                points += 20 / tracks

    return points

def check_track_two(tracks, list_WC, list_PR, day_1, day_2):
    """ Checks if both WC and PR are scheduled on given day and assigns points.

    Arguments:
        tracks (int): Number of tracks.
        list_WC [int]: List of day indices for all Werkcolleges.
        list_PR [int]: List of day indices for all Practicums.
        day_1 (int): Index of first day to be checked.
        day_2 (int): Index of second day to be checked.

    Returns:
        points (int): Calculated number of points.

    """

    points = 0

    for track in range(tracks):
        if ((list_WC[track] == day_1 and list_PR[track] == day_2) or
           (list_WC[track] == day_2 and list_PR[track] == day_1)):
            points += 20 / tracks

    return points


def students_check(timetable):
    """ Calculates timetable score for maximum students rule.

    Checks if classroom capacity is exceeded by number of students. One point
    is deducted from the total score for each extra student.

    Arguments:
        timetable (Timetable): Timetable to calculate score of.

    Returns:
        points (int): Calculated score of maximum students rule.

    """

    points = 0

    # Loops over the courses in the timetable.
    for course in timetable.courses:
        for lecture in course.lectures:
            room = timetable.find_slot(lecture)[0][0]

            margin = timetable.classrooms[room].capacity - lecture.students

            # If there are more sudents in a room than there is space,
            # points get subtracted.
            if margin < 0:
                lecture.score += margin
                points += margin

    return points


def nightslot_check(timetable):
    """ Calculates timetable score for nightslot rule.

    Checks if the nightslot in classroom C0.110 is used. Twenty points are
    deducted for each use of the nightslot.

    Arguments:
        timetable (Timetable): Timetable to calculate score of.

    Returns:
        points (int): Calculated score of nightslot rule.

    """

    points = 0

    # Loops over the days to check nightslot.
    for day in range(5):

        # When nightslot is used, points get subtracted.
        if timetable.grid[5][day][4].course != ("empty"):
            timetable.grid[5][day][4].score -= 20
            points -= 20

    return points


def reset_points(timetable):
    """ Resets the individual scores of the lectures in the timetable.

    Arguments:
        timetable (Timetable): Timetable to reset score of.

    """
    for classroom in range(7):
        for day in range(5):
            for slot in range(5):
                try:
                    timetable.grid[classroom][day][slot].score = 0
                except(AttributeError):
                    pass
