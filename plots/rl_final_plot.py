import matplotlib.pyplot as plt
import itertools


def plot_learning_curve(x, scores, figure_file):
    # running_avg = np.zeros(len(scores))
    # for i in range(len(running_avg)):
    #     running_avg[i] = np.mean(scores[max(0, i-100):(i+1)])
    plt.plot(x, scores)
    plt.title('Cumilative reward over time')
    plt.savefig(figure_file)

score_history = [-2.5, -0.5, -2.5, -2.5]

x = [i+1 for i in range(133)]
y = [0,1,-1,-1,-1,-2,-3,-4,-4,-4,-3,-2,-2,-3,-1,1,2,2,2,2,2,2,1,1,1,2,1,1,1,2,3,4,5,4,4,3,2,4,3,2,2,2,3,2,2,1,0,0,1,-1,-2,-3,-4,-3,-2,-2,-3,-1,1,2,1,1,1,2,3,4,5,4,4,3,2,4,3,4,4,4,4,5,4,6,6,6,7,7,6,7,6,5,4,5,6,6,7,7,8,9,10,11,11,11,10,10,10,11,12,12,13,14,15,16,17,17,16,17,18,18,19,20,20,21,22,23,24,25,26,27,26,27,28,29,30,31,32]

plot_learning_curve(x, y, 'figure_file.png')