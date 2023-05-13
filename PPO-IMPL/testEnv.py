import random
import math
import numpy as np
from ppo_torch import Agent
from utils2 import plot_learning_curve

class MazeGame:
    def __init__(self):
        # Define the state space
        self.state_space = [(i, j) for i in range(9) for j in range(9) if (i, j) not in [(2,2),(3,4),(4,7),(5,1),(6,5),(8,3)]] # removed 6 grids at random
        self.num_states = len(self.state_space)
        
        # Define the action space
        self.action_space = ['left', 'right', 'up']
        self.num_actions = len(self.action_space)
        
        # Define the goal destination
        self.goal = random.choice(self.state_space)
        
        # Define the starting state (random)
        self.current_state = random.choice(self.state_space)
        
        # Define the maximum number of steps per episode
        self.max_steps = 100
        
        # Define the distance function (Euclidean distance)
        self.distance = lambda s1, s2: math.sqrt((s1[0]-s2[0])**2 + (s1[1]-s2[1])**2)
        
    def reset(self):
        # Reset the current state to a random state
        self.current_state = random.choice(self.state_space)
        
        # Reset the goal destination to a random state
        self.goal = random.choice(self.state_space)
        
        return self.current_state
    
    def step(self, action):
        # Move the agent according to the action
        if action == 'left':
            next_state = (self.current_state[0], max(self.current_state[1]-1, 0))
        elif action == 'right':
            next_state = (self.current_state[0], min(self.current_state[1]+1, 8))
        elif action == 'up':
            next_state = (max(self.current_state[0]-1, 0), self.current_state[1])
        
        # Compute the reward based on the distance to the goal
        dist_to_goal = self.distance(next_state, self.goal)
        prev_dist_to_goal = self.distance(self.current_state, self.goal)
        if dist_to_goal < prev_dist_to_goal:
            reward = 1
        elif dist_to_goal > prev_dist_to_goal:
            reward = -1
        else:
            reward = 0
        
        # Update the current state
        self.current_state = next_state
        
        # Check if the goal has been reached
        done = (next_state == self.goal)
        
        # Check if the maximum number of steps has been reached
        if self.max_steps <= 0:
            done = True
        
        # Decrement the maximum number of steps
        self.max_steps -= 1
        
        return next_state, reward, done
    
if __name__ == '__main__':
    env = MazeGame()
    N = 12
    batch_size = 4
    n_epochs = 10
    alpha = 0.0003

    agent = Agent(n_actions=3, batch_size=batch_size, 
                    alpha=alpha, n_epochs=n_epochs, 
                    input_dims=env.observation_space.shape)
    n_games = 200

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
            observation_, reward, done, info = env.step(action)
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