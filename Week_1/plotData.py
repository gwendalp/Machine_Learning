import matplotlib.pyplot as plt
import numpy as np

def plotData(X,y):
    """
    plots the data points and gives the figure axes labels of
    population and profit.
    """

# ====================== YOUR CODE HERE ======================
# Instructions: Plot the training data into a figure using the
#               "figure" and "plot" commands. Set the axes labels using
#               the "xlabel" and "ylabel" commands. Assume the
#               population and revenue data have been passed in
#               as the x and y arguments of this function.
#
# Hint: You can use the 'ro' option with plt.plot to have the markers
#       appear as red crosses. Furthermore, you can make the
#       markers larger by using plt.plot(..., 'r0', markersize=10);
    
    plt.figure()
    plt.xlabel("population")
    plt.ylabel("revenus")
    plt.plot(X, y, 'ro', markersize=10)
    plt.show()
    
# ============================================================
