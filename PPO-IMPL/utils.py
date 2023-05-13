import numpy as np
import matplotlib.pyplot as plt

def plot_learning_curve(x, scores, figure_file):
    print(scores)
    scores.pop()
    # running_avg = np.zeros(len(scores))
    # for i in range(len(running_avg)):
    #     running_avg[i] = np.mean(scores[max(0, i-100):(i+1)])
    plt.plot(x, scores)
    plt.title('Rewards from average to bad')
    plt.savefig(figure_file)