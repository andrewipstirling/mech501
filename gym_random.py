import gymnasium as gym
import numpy as np

env = gym.make("InvertedPendulum-v4",render_mode = 'human')
observation, info = env.reset(seed=13)


# Observation:
obs_space = env.observation_space
#Array[ Cart Position, Vertical Angle of the Pole, Linear Velocity of Cart, Angular Velocity of Pole ]

# Action:
action_space = env.action_space
# Array [ Force applied to cart ] in range [-3, 3] N

# Rewards
# Reward of +1 every timestep pendulum is upright


for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    # Check angle of pendulum is greater than 90 deg
    # Reset if so
    if (np.abs(observation[1]) > np.pi / 2):
        observation, info = env.reset()

    env.render()

env.close()

print("Succesfully Closed!")