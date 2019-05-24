import numpy as np
import pandas as pd


def make_table(timetable):
    """ Function to print the timetable to readable output and write it to a
    file.

    The function uses pandas to create dataframes that, converted from the
    numpy NDarray, are easy to print as well as write to a file. The resulting
    file will be stored in the "Rooster/results" as a .txt file.

    Arguments:
        timetable (Timetable): The timetable to be printed.

    """

    f = open('./results/timetable.txt' ,'w')
    i = 0

    # Iterate over classrooms to print and write timetables.
    for classroom in timetable.classrooms:
        print("\n\n----- " + classroom.name + " -----")
        f.write("\n\n----- " + classroom.name + " -----\n")

        # Using pandas dataframes for a simple output.
        columns = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
        index = ['9:00', '11:00', '13:00' , '15:00', '17:00']
        df = pd.DataFrame(np.transpose(timetable.grid[i]), columns, index)

        # Change values in the dataframe to the course and type.
        for courses in timetable.courses:
            for lecture in courses.lectures:
                df = df.replace(lecture, lecture.type + ": " + lecture.course)

        print(df.to_string())
        f.write(df.to_string())
        i += 1
    f.close()
