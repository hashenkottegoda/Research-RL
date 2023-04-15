import numpy as np
from ppo_torch import Agent
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
    
    def reset(self):
        # get user input for weight, fat, emotion
        weight = input("Enter weight: ")
        fat = input("Enter fat: ")
        emotion = input("Enter emotion: ")
        observation = [weight, fat, emotion]
        return observation
    
    def step(self, old_state, action):
        # get user input for weight, fat, emotion
        weight = input("Enter weight: ")
        fat = input("Enter fat: ")
        emotion = input("Enter emotion: ")
        observation = [weight, fat, emotion]   

        oldWeight = old_state[0]
        oldFat = old_state[1]
        oldEmotion = old_state[2]

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
        if fat > oldFat:
            reward = reward+1
        elif fat < oldFat:
            reward = reward-1
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
            done = False
        else:
            done = True
        info = {}
        return observation, reward, done, info
    
if __name__ == '__main__':
    # env = gym.make('CartPole-v0')
    env = CustomEnv()
    N = 20
    batch_size = 5
    n_epochs = 4
    alpha = 0.0003
    # agent = Agent(n_actions=env.action_space.n, batch_size=batch_size, 
    #                 alpha=alpha, n_epochs=n_epochs, 
    #                 input_dims=env.observation_space.shape)
    agent = Agent(n_actions=len(env.action_space), batch_size=batch_size, 
                    alpha=alpha, n_epochs=n_epochs, 
                    input_dims=env.sample_observation.shape)
    n_games = 100

    figure_file = 'plots/cartpole.png'

    # best_score = env.reward_range[0]
    best_score = -float('inf')
    score_history = []

    learn_iters = 0
    avg_score = 0
    n_steps = 0

    for i in range(n_games):
        observation = env.reset()
        done = False
        score = 0
        while not done:
            action, prob, val = agent.choose_action(observation)
            real_action = env.action_space[action]
            observation_, reward, done, info = env.step(observation, real_action)
            n_steps += 1
            score += reward
            agent.remember(observation, action, prob, val, reward, done)
            if n_steps % N == 0:
                agent.learn()
                learn_iters += 1
            observation = observation_
        score_history.append(score)
        avg_score = np.mean(score_history[-100:])

        if avg_score > best_score:
            best_score = avg_score
            agent.save_models()

        print('episode', i, 'score %.1f' % score, 'avg score %.1f' % avg_score,
                'time_steps', n_steps, 'learning_steps', learn_iters)
    x = [i+1 for i in range(len(score_history))]
    plot_learning_curve(x, score_history, figure_file)