import numpy as np
import matplotlib.pyplot as plt

def plot_learning_curve(x, scores, figure_file):
    plt.plot(x, scores)
    plt.title('Scores of each iteration')
    plt.savefig(figure_file)