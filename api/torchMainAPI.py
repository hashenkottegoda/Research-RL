import numpy as np
from ppotorchAPI import Agent
from utils import plot_learning_curve

class CustomEnv:
    def __init__(self):
        self.action_space = self.getActionSpace()
        self.observation_space = self.getObservationSpace()
        self.sample_observation = self.observation_space[0]
        self.reward_range = (-float('inf'), float('inf'))

    def getActionSpace(self):
        # Protein, fat, carbohydrate, energy requirement
        proteinP = [ -0.1, 0, 0.1]
        fatP = [ -0.1, 0, 0.1]
        carbohydrateP = [ -0.1, 0, 0.1]
        energyP = [ -0.1, 0, 0.1]

        # create a list of lists and put the elements to the list
        listOflist = []
        for a in proteinP:
            for b in fatP:
                for c in carbohydrateP:
                    for d in energyP:
                        element=[a,b,c,d]
                        listOflist.append(element)
        return listOflist
    
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
    
    
    def step(self, oldObservation, newObservation):
        oldWeight = oldObservation[0]
        oldFat = oldObservation[1]
        oldEmotion = oldObservation[2]

        weight = newObservation[0]
        fat = newObservation[1]
        emotion = newObservation[2]

        reward = 0
        # Weight reward
        if weight == 2:
            if oldWeight == 2:
                reward = reward
            elif oldWeight != 2:
                reward = reward+1
        elif weight != 2:
            if oldWeight == 2:
                reward = reward-1
            elif oldWeight != 2:
                reward = reward

        # Fat reward
        if fat == 3:
            if oldFat == 3:
                reward = reward
            elif oldFat != 3:
                reward = reward+1
        elif fat != 3:
            if oldFat == 3:
                reward = reward-1
            elif oldFat != 3:
                if fat < 3:
                    if fat > oldFat:
                        reward = reward+0.5
                    elif fat < oldFat:
                        reward = reward-0.5
                    elif fat == oldFat:
                        reward = reward
                elif fat > 3:
                    if fat < oldFat:
                        reward = reward+0.5
                    elif fat > oldFat:
                        reward = reward-0.5
                    elif fat == oldFat:
                        reward = reward
        # Emotion reward
        if emotion > oldEmotion:
            reward = reward+1
        elif emotion < oldEmotion:
            reward = reward-1
        elif emotion == oldEmotion:
            reward = reward

        if weight == -1:    
            done = True
        else:
            done = False
        info = {}
        return  reward, done, info
    
def getPPOAgent():
    env = CustomEnv()
    batch_size = 4
    n_epochs = 10
    alpha = 0.0003

    agent = Agent(n_actions=len(env.action_space), batch_size=batch_size, 
                    alpha=alpha, n_epochs=n_epochs, 
                    input_dims=env.sample_observation.shape)

    # figure_file = 'plots/cartpole.png'
    # best_score = -float('inf')
    # score_history = []

    learn_iters = 0
    # avg_score = 0
    n_steps = 0

    # check if the model is already trained and load it
    try:
        agent.load_models()
        print('...loaded saved models...')
    except:
        print('...no saved models, starting training from scratch...')
        pass

    score = 0

    return env, agent, learn_iters, n_steps, score

    # score_history.append(score)
    # x = [i+1 for i in range(len(score_history))]
    # plot_learning_curve(x, score_history, figure_file)

def get_action(env, agent, learn_iters, n_steps, score, oldObservation , newObservation):
    N = 12
    action, prob, val = agent.choose_action(newObservation)
    real_action = env.action_space[action]
    if(oldObservation):
        reward, done, info = env.step(oldObservation, newObservation)
        n_steps += 1
        score += reward
        done = False
        agent.remember(newObservation, action, prob, val, reward, done)

        if n_steps % N == 0:
            agent.learn()
            learn_iters += 1

        print('step', n_steps, 'score %.1f' % score,
        'time_steps', n_steps, 'learning_steps', learn_iters)
      
    return real_action , learn_iters, n_steps, score, newObservation
