import matplotlib.pyplot as plt



def make_plot(label, scores):
    plt.figure()
    plt.plot(range(len(scores)), scores, label=label)
    plt.plot(scores.index(max(scores)), max(scores), 'ro',label="Max: " + str(scores.index(max(scores))) + " iterations.")
    plt.title(label)
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.legend()
    plt.show()


scores = [-1000, -800, -750, -675, -525, -425, -350, -225 , -175, -135, -105, -85, -60, -46, -46 , -46, -46, -46 , -46]
make_plot("Greedy", scores)
