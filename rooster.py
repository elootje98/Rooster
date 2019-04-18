import data as d
import numpy as np
import objective as obj

def make_grid(rooster):
    testrooster = rooster
    for course in rooster.courses:
        testrooster = plan_lectures(course, testrooster)
        while not testrooster.check_order([course]):
            testrooster = plan_lectures(course, testrooster)
        rooster = testrooster


def plan_lectures(course, testrooster):
    for lecture in course.lectures:
        empty = True
        while empty:
            restricted = False
            classroom = np.random.randint(0, 7)
            slot = np.random.randint(0, 5)
            day = np.random.randint(0, 4)

            # checkt of plek vrij is
            if testrooster.grid[classroom][slot][day] == 0:
                # checkt of er op dat slot restricted colleges zijn
                for i in range(7):
                    if testrooster.grid[i][slot][day] in d.get_lecture(lecture).restricted:
                        restricted = True
                        break

                if not restricted:
                    testrooster.grid[classroom][slot][day] = lecture
                    empty = False

    return testrooster

rooster = d.Rooster(d.courses, d.lectures, d.classrooms)

rooster.sort()
make_grid(rooster)


print(rooster.grid)
obj.objective_function(rooster)
