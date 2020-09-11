# Part 1: Information we know
#     There are 4 slots and 4 characters
#     Order does matter
#     Order of the symbols matters
#     A+B is considered unique from B+A, even if equivelent
#
# Therefore the problem is permutatuons of P(4 4) * P(3 3) = 144

# For this to work you may need the following imports
#    import random
#    import sklearn.neural_network
#    import numpy.random
#    import ipywidgets


# Note that this Closes plot so the other line isn't there in the
# second png
def learning_curve(Ts, Hs, filename):
    import numpy as numpy
    import matplotlib.pyplot as plt
    max_Iters = numpy.array([])
    scores = numpy.array([])

    # Prep and Plot points
    for i in range(50, 2001, 50):
        score = test_NN(Ts, Hs, i)
        scores = numpy.append(scores, score)
        max_Iters = numpy.append(max_Iters, i)

    # Generate regression as a stright line.
    ## m, b = numpy.polyfit(max_Iters, scores, 1)
    ## xadd = range(2000)
    ## plt.plot(xadd, m * xadd + b)

    plt.plot(max_Iters, scores)

    plt.savefig(filename)
    plt.close()
    return max_Iters, scores
