import numpy as np

# Define the state space
states = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

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


