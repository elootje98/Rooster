import matplotlib.pyplot as plt
from data import data as d
import numpy as np
import pandas as pd
import matplotlib.gridspec as gridspec

def make_table(timetable):
    # fig = plt.figure()
    #gs = gridspec.GridSpec(nrows=4, ncols=2)
    f = open('timetable.txt' ,'w')
    for classroom in range(len(d.classrooms)):
        ### test with matplotlib
        #ax = fig.add_subplot(gs[int(classroom/2) , classroom%2])
        #ax.set_title(d.classrooms[classroom])
        #plt.imshow(np.transpose(timetable.grid[classroom]))


        # using dataframes for a simple output
        print("\n\n----- " + d.classrooms[classroom] + " -----")
        f.write("\n\n----- " + d.classrooms[classroom] + " -----\n")
        df = pd.DataFrame(np.transpose(timetable.grid[classroom]),
        columns=['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
        index=['9:00', '11:00', '13:00' , '15:00'])

        # change values in the dataframe to the course and type
        for child in timetable.child_lectures:
            df = df.replace(child, child.type + ": " + child.course)
        #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        #    print(df)
        print(df.to_string())
        f.write(df.to_string())
    f.close()
    #fig.tight_layout()
    #plt.show()
