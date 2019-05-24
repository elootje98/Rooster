import colorsys

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import seaborn as sns

cm = sns.light_palette("red", as_cmap=True)

def make_table(timetable):
    """ UNDER CONSTRUCTION """
    # fig = plt.figure()
    #gs = gridspec.GridSpec(nrows=4, ncols=2)
    f = open('./results/timetable.txt' ,'w')
    i = 0
    for classroom in timetable.classrooms:
     #classroom in range(len(d.classrooms)):
        ### test with matplotlib
        #ax = fig.add_subplot(gs[int(classroom/2) , classroom%2])
        #ax.set_title(d.classrooms[classroom])
        #plt.imshow(np.transpose(timetable.grid[classroom]))

        min_score = 100
        max_score = -100

        current_scores = np.zeros((5,5), dtype=float)
        for days in range(5):
            for slots in range(5):
                current_scores[days][slots] = timetable.grid[i][days][slots].score
                if timetable.grid[i][days][slots].course != "empty":
                    if timetable.grid[i][days][slots].score < min_score:
                        min_score = timetable.grid[i][days][slots].score
                    elif timetable.grid[i][days][slots].score > max_score:
                        max_score =  timetable.grid[i][days][slots].score
        score_range = float(max_score - min_score)

        rgb = colorsys.hsv_to_rgb(i / score_range, 1.0, 1.0)


        # using dataframes for a simple output
        print("\n\n----- " + classroom.name + " -----")
        f.write("\n\n----- " + classroom.name + " -----\n")


        columns = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
        index = ['9:00', '11:00', '13:00' , '15:00', '17:00']
        df = pd.DataFrame(np.transpose(timetable.grid[i]), columns, index)

        # change values in the dataframe to the course and type
        for courses in timetable.courses:
            for lecture in courses.lectures:
                df = df.replace(lecture, lecture.type + ": " + lecture.course)
                #df = df.replace(lecture, lecture.score)
        #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        #    print(df)


        fig, ax = plt.subplots()
        im = ax.imshow(current_scores)
        # We want to show all ticks...
        ax.set_xticks(np.arange(len(columns)))
        ax.set_yticks(np.arange(len(index)))
        # ... and label them with the respective list entries
        ax.set_xticklabels(columns)
        ax.set_yticklabels(index)


        # Loop over data dimensions and create text annotations.
        for days in range(5):
            for slots in range(5):
                text = ax.text(days, slots, timetable.grid[i][days][slots].course,
                               ha="center", va="center", color="w")


        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            print(df)
        f.write(df.to_string())
        i += 1
    f.close()
    #fig.tight_layout()
    plt.show()
