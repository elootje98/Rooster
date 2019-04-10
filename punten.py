# Dictionary containing the points allocated to the lectures, is used to determine the lectures most difficult to schedule
lecture_points{"restricted" : 20, "HC" : 10, "WC" : 5}

# Dictionary containing the points allocated to the timetable, this is used to rate the quality of the timetable
# max_spread = 2 activities: ma-do/di-vr, 3 lectures: ma-wo-vr, 4 vakken: ma-di-do-vr
# same_# is number of activities of the same course in one day
# (no_)conflict is optional, students with(out) conflicting timeschedules get points
timetable_points = {"overfull" : -1, "evening": -20,
"max_spread" : 20, "same_1" : -10, "same_2" : -20, "same_3": -30,
"no_conflict" : 1, "conflict" : 1}
