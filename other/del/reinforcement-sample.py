import numpy as np

# Define the action space
actions = ['up', 'down', 'left', 'right']

# Initialize the Q-table with zeros
q_table = np.zeros((10, 10, len(actions)))

# Set the hyperparameters
alpha = 0.1  # learning rate
gamma = 0.9  # discount factor
epsilon = 0.1  # exploration rate

# Define the reward function
def get_reward(state, action):
    # Calculate the new state based on the action
    new_state = state.copy()
    if action == 'up':
        new_state[0] -= 1
    elif action == 'down':
        new_state[0] += 1
    elif action == 'left':
        new_state[1] -= 1
    elif action == 'right':
        new_state[1] += 1
    
    # Check if the dog has fetched the ball
    if tuple(new_state) == (5, 5):
        reward = 1
        done = True
    else:
        reward = -0.1
        done = False
    
    return reward, new_state, done

# Train the Q-learning model
for episode in range(1000):
    # Initialize the state
    state = np.array([0, 0])
    done = False
    
    while not done:
        # Choose an action based on the Q-values
        if np.random.uniform() < epsilon:
            action = np.random.choice(actions)
        else:
            action = actions[np.argmax(q_table[tuple(state)][0])]
        
        # Get the reward and new state from the environment
        reward, new_state, done = get_reward(state, action)

        # print(reward)
        
        # Update the Q-value for the state-action pair
        q_table[tuple(state)][actions.index(action)] += alpha * (reward + gamma * np.max(q_table[tuple(new_state)]) - q_table[tuple(state)][actions.index(action)])

        # print(q_table[tuple(state)][0][0])
        # Update the state
        state = new_state.copy()
