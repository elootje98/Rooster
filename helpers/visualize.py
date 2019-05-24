import matplotlib.pyplot as plt

def make_plot(labels, scores):
    """ Function to create a plot out of a list of scores for (an) algorithm(s).

    Arguments:
        labels [string]: List of strings containing the names of the algorithms
            used.
        scores [int]: List of score per iteration.
        
    """

    # Create plot title out of labels.
    seperator = " + "
    title = seperator.join([x.capitalize() for x in labels])
    title += " - " + str(len(scores)) + " iterations"

    # Create a plot, also demonstrating where the maximum is reached.
    plt.figure()
    plt.plot(range(len(scores)), scores, label=labels[0].capitalize())
    plt.plot(scores.index(max(scores)), max(scores), 'ro',label="Score = "
            + str(max(scores))+"\nIterations: "+str(scores.index(max(scores)) + 1))
    plt.title(title)
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.legend()
    plt.show()
