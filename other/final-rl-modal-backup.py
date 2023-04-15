import numpy as np
from itertools import combinations


# Daily nutrition requirement
dailyNutritionReq = {'protein': '190g', 'fat': '80g', 'carb': '200g', 'energyReq': '3909'}

# Available meals
Meal1 = {'protein': '50g', 'fat': '35g', 'carb': '60g', 'energyReq': '1500'}
Meal2 = {'protein': '55g', 'fat': '30g', 'carb': '75g', 'energyReq': '1460'}
Meal3 = {'protein': '65g', 'fat': '25g', 'carb': '70g', 'energyReq': '1400'}
Meal4 = {'protein': '45g', 'fat': '20g', 'carb': '75g', 'energyReq': '1350'}
Meal5 = {'protein': '75g', 'fat': '25g', 'carb': '65g', 'energyReq': '1750'}
Meal6 = {'protein': '80g', 'fat': '40g', 'carb': '70g', 'energyReq': '1640'}
MealArr = ['Meal1', 'Meal2', 'Meal3', 'Meal4', 'Meal5', 'Meal6']
MealNameArr = ['Meal1', 'Meal2', 'Meal3', 'Meal4', 'Meal5']


# get all positive daily meal combinations
def get_dailyCombinations(MealNameArr):
    combs = combinations(MealNameArr, 3)
    return list(combs)

dailycombList = get_dailyCombinations(MealNameArr)

# get all positive wwekl meal plan combinations
def get_weeklyCombinations(dailycombList):
    combs = combinations(dailycombList, 7)
    return list(combs)

print(len(get_weeklyCombinations(dailycombList)))
print((get_weeklyCombinations(dailycombList)))

# Define the state space
weights = ['low', 'average', 'high']
healthStatus = [1, 2, 3, 4, 5]
emotionalStatus = [1, 2, 3, 4, 5]
fatLevel = [1, 2, 3, 4, 5]

states = [{'weight': 'low', 'healthStatus': 1}]

# Define the action space
actions = ['chicken','beef', 'lamb', 'fish']

# Define the Q-table
q_table = np.zeros((len(states), len(actions)))

# Set the hyperparameters
alpha = 0.1  # learning rate
gamma = 0.9  # discount factor
epsilon = 0.1  # exploration rate

def get_reward(state, action):
    nutrition_values = {
        'chicken': [20, 15, 10],  # protein, fat, carbs
        'beef': [25, 20, 5],
        'lamb': [30, 10, 5],
        'fish': [15, 5, 20]
    }
    
    required_nutrition = [300, 200, 100]  # protein, fat, carbs
    
    nutrition = nutrition_values[action]
    reward = 0
    
    for i in range(3):
        if nutrition[i] >= required_nutrition[i]:
            reward += 1
        else:
            reward -= 1
    
    return reward

# Train the Q-learning model
for episode in range(1000):
    # Initialize the state
    state = 0  # Monday
    
    for day in range(len(states)):
        # Choose an action based on the Q-values
        if np.random.uniform() < epsilon:
            action = np.random.choice(actions)
        else:
            action = actions[np.argmax(q_table[state])]
        
        # Get the reward for the action
        reward = get_reward(state, action)
        
        # Get the new state (next day)
        new_state = state + 1 if state < len(states) - 1 else 0
        
        # Update the Q-value for the state-action pair
        q_table[state][actions.index(action)] += alpha * (reward + gamma * np.max(q_table[new_state]) - q_table[state][actions.index(action)])
        
        # Update the state
        state = new_state

def gen_meal_paln():
    # Generate the weekly meal plan
    meal_plan = []

    for state in range(len(states)):
        action = actions[np.argmax(q_table[state])]
        meal_plan.append(action)

    print(meal_plan)

gen_meal_paln()
gen_meal_paln()
gen_meal_paln()
gen_meal_paln()
gen_meal_paln()
gen_meal_paln()
gen_meal_paln()


