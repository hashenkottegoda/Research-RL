import gym
from ppo_torch import Agent
import numpy as np
from mlxtend.plotting import plot_learning_curves

class CustomEnv:
    def __init__(self):
        self.action_space = [0, 1, 2]
        self.observation_space = np.zeros((4,))
        self.reward_range = (-float('inf'), float('inf'))

    def reset(self):
        return np.zeros((4,))

    def step(self, action):
        observation = np.zeros((4,))
        reward = 0.0
        done = False
        info = {}
        return observation, reward, done, info

env = gym.make('CartPole-v1')
# env = CustomEnv()
N = 20
batch_size = 5
n_epochs = 4
alpha = 0.0003
n_games = 300

observation = env.reset()
observation0 = observation[0]
observation1 = observation[1]

# print(env.observation_space)
# print(env.observation_space.shape)
# print(type(observation))
# print(observation)
print(type(observation0))
print(observation0)
print(type(observation1))
print(observation1)
# print(env.action_space.n)

simple_list = [1,2,3,4]
simple_touple = (1,2,3,4)
arr = np.array(simple_list)
arr2 = np.array(simple_touple)
arr0 = np.array(1)
arr3 = np.array([[1,2], [3,4], [5,6]])
arr4 = np.array([[[1,2], [3,4], [5,6]], [[1,2], [3,4], [5,6]]])


# print(type(arr))
# print(arr)
# print(arr.shape)
# print(arr.ndim)

# print(type(arr2))
# print(arr2)
# print(arr2.shape)
# print(arr2.ndim)

# print(type(arr0))
# print(arr0)
# print(arr0.shape)
# print(arr0.ndim)

# print(type(arr3))
# print(arr3)
# print(arr3.shape)
# print(arr3.ndim)

# print(type(arr4))
# print(arr4)
# print(arr4.shape)
# print(arr4.ndim)

print("env.observation_space: ", env.observation_space)
print("env.observation_space.shape: ", env.observation_space.shape)
print("env.action_space: ", type(env.action_space))
print("env.action_space.n: ", env.action_space.n)