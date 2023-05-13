import numpy as np
import matplotlib.pyplot as plt

def plot_learning_curve(x, scores, figure_file):
    # running_avg = np.zeros(len(scores))
    # for i in range(len(running_avg)):
    #     running_avg[i] = np.mean(scores[max(0, i-100):(i+1)])
    plt.plot(x, scores)
    plt.title('Scores of each iteration')
    plt.savefig(figure_file)

score_history = [-2.5, -0.5, -2.5, -2.5]

x = [i+1 for i in range(len(score_history))]
plot_learning_curve(x, score_history, 'figure_file.png')


print('testing.py')