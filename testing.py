import numpy as np
import matplotlib.pyplot as plt
import itertools

def getActionSpace(self):
    # Protein, fat, carbohydrate, energy requirement
    proteinP = [-0.1, 0, 0.1]
    fatP = [-0.1, 0, 0.1]
    carbohydrateP = [-0.1, 0, 0.1]
    energyP = [-0.1, 0, 0.1]

    # create a list of lists and put the elements to the list
    listOflist = []
    for a in proteinP:
        for b in fatP:
            for c in carbohydrateP:
                for d in energyP:
                    element=[a,b,c,d]
                    listOflist.append(element)
    return listOflist
    
# returns state/observation space of the environment
def getObservationSpace(self):
    weightArr = [1, 2, 3]
    fatArr = [1,2,3,4,5]
    emotionArr = [1,2,3,4,5]

    # create a list of lists and put the elements to the list
    listOflist = []
    for a in weightArr:
        for b in fatArr:
            for c in emotionArr:
                element=[a,b,c]
                listOflist.append(element)
    # convert the list of lists to a numpy array
    arr = np.array(listOflist)
    return arr

def plot_learning_curve(x, scores, figure_file):
    # running_avg = np.zeros(len(scores))
    # for i in range(len(running_avg)):
    #     running_avg[i] = np.mean(scores[max(0, i-100):(i+1)])
    plt.plot(x, scores)
    plt.title('Scores of each iteration')
    plt.savefig(figure_file)

def get_combinations():

    vars = ['left', 'right', 'up']
    combinations = list(itertools.product(vars, repeat=4))
    print(combinations)
    return  len(combinations)

score_history = [-2.5, -0.5, -2.5, -2.5]

x = [i+1 for i in range(len(score_history))]
plot_learning_curve(x, score_history, 'figure_file.png')


print('testing.py')
print('getActionSpace: ', len(getActionSpace(1)))
print('getObservationSpace: ', len(getObservationSpace(1)))
print('get_combinations: ', get_combinations() )