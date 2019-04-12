import data as d
import numpy as np


def make_grid(rooster):
    for course in rooster.courses:
        for lecture in course.lectures:
            empty = True
            while empty:
                restricted = False
                classroom = np.random.randint(0, 7)
                slot = np.random.randint(0, 5)
                day = np.random.randint(0, 5)

                # checkt of plek vrij is
                if rooster.grid[classroom][slot][day] == 0:
                    # checkt of er op dat slot restricted colleges zijn
                    for i in range(7):
                        if rooster.grid[i][slot][day] in rooster.lectures[lecture - 1].restricted:
                            restricted = True
                            print("restriced", lecture, rooster.lectures[lecture - 1].restricted)
                            break

                    if not restricted:
                        rooster.grid[classroom][slot][day] = lecture
                        empty = False


rooster = d.Rooster(d.courses, d.lectures, d.classrooms)
make_grid(rooster)
print(rooster.grid)
