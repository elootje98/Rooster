import matplotlib.pyplot as plt



def make_plot(labels, scores):

    seperator = " + "
    title = seperator.join([x.capitalize() for x in labels])
    title += " - " + str(len(scores)) + " iterations"

    plt.figure()
    plt.plot(range(len(scores)), scores, label=labels[0].capitalize())
    plt.plot(scores.index(max(scores)), max(scores), 'ro',label="Max: " + str(scores.index(max(scores)) + 1) + " iterations.")
    plt.title(title)
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.legend()
    plt.show()
