import numpy as np
from itertools import combinations
import random
from itertools import combinations_with_replacement


# Daily nutrition requirement
dailyNutritionReq = {'protein': '190g', 'fat': '80g', 'carb': '200g', 'energyReq': '3909'}

# Available meals
Meal1 = {'protein': '50g', 'fat': '35g', 'carb': '60g', 'energyReq': '1500'}
Meal2 = {'protein': '55g', 'fat': '30g', 'carb': '75g', 'energyReq': '1460'}
Meal3 = {'protein': '65g', 'fat': '25g', 'carb': '70g', 'energyReq': '1400'}
Meal4 = {'protein': '45g', 'fat': '20g', 'carb': '75g', 'energyReq': '1350'}
Meal5 = {'protein': '75g', 'fat': '25g', 'carb': '65g', 'energyReq': '1750'}
MealNameArr = ['Meal1', 'Meal2', 'Meal3', 'Meal4']


# get all positive daily meal combinations
def get_dailyCombinations(MealNameArr):
    combs = combinations(MealNameArr, 3)
    return list(combs)

dailycombList = get_dailyCombinations(MealNameArr)
print(len(dailycombList))
print(dailycombList)


# get all positive wwekl meal plan combinations
# def get_weeklyCombinations(dailycombList):
#     combs = combinations(dailycombList, 7)
#     return list(combs)

# get all positive weekly meal plan combinations (with repetition)
def get_weeklyCombinations(dailycombList):
    combs = combinations_with_replacement(dailycombList, 7)
    return list(combs)

print(len(get_weeklyCombinations(dailycombList)))
# print((get_weeklyCombinations(dailycombList)))

# print((get_weeklyCombinations(dailycombList)))

# Define the state space
weights = ['low', 'average', 'high']
healthStatus = [1, 2, 3, 4, 5]
emotionalStatus = [1, 2, 3, 4, 5]
fatLevel = [1, 2, 3, 4, 5]

# Define the state space using the weights, health status, emotional status, and fat level
states = []
for weight in weights:
    for health in healthStatus:
        for emotional in emotionalStatus:
            for fat in fatLevel:
                states.append((weight, health, emotional, fat))
            
# get get_weeklyCombinations(dailycombList) as the action space
actions = get_weeklyCombinations(dailycombList)

# Define the Q-table
# q_table = np.zeros((len(states), len(actions)))
q_table = {state: {action: 0 for action in actions} for state in states}


# Set the hyperparameters
alpha = 0.1  # learning rate
gamma = 0.9  # discount factor
epsilon = 0.5  # exploration rate

# create reward function to keep weight average and health status 5 and emotional status 5 and fat level 5
def get_reward(state, action): 
    if state[0] == 'average' and state[1] == 5 and state[2] == 5 and state[3] == 5:
        return 100
    else:
        return 0
    
#method to get state from user input
def get_state():
    weight = input("Enter your weight: ")
    #if weight is -1 then exit the program
    if weight == '-1':
        exit()
    health = input("Enter your health status: ")
    emotional = input("Enter your emotional status: ")
    fat = input("Enter your fat level: ")
    state = (weight, int(health), int(emotional), int(fat))
    return state

#Train the Q-learning model continuously using user input state
def get_meal_plans():
 
    # Initialize the state
    state = get_state()

    while True:

        # print("State: ", state)
        # print("Action: ", actions)
        # Choose an action based on the Q-values
        if np.random.uniform() < epsilon:
            # action = np.random.choice(actions)
            print('random')
            action = random.choice(actions)
        else:
            print('rl')
            action = actions[np.argmax(q_table[state])]

        print(action)

        #get new state from user input
        new_state = get_state()

        # Get the reward for the action
        reward = get_reward(new_state, action)

        # Update the Q-value for the state-action pair
        # q_table[state][actions.index(action)] += alpha * (reward + gamma * np.max(q_table[new_state]) - q_table[state][actions.index(action)])
        q_table[state][action] += alpha * (reward + gamma * np.max(list(q_table[new_state].values())) - q_table[state][action])


        # Update the state
        state = new_state

get_meal_plans()