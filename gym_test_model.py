import gymnasium as gym
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def run_model(model, env, episodes, print_reward):
    """Runs the given model on the provided Gym environment."""
    act_limit = env.action_space.high[0]
    reward_arr = np.zeros(1001)
    reward_sum_arr = np.zeros(1001)
    
    for i_episode in range(episodes):
        observation = env.reset()[0]
        done = False
        step_num = 0
        reward_sum = 0

        print(f'Starting episode #{i_episode}')

        while not done:
            env.render()

            if print_reward:
                print(f'timestep: {step_num}, reward = {reward_sum}')

            action = model(tf.expand_dims(observation, 0))[0][0]
            action = tf.clip_by_value(action, -act_limit, act_limit)

            observation, reward, done, trunc, _ = env.step(action)
            done = done or trunc
            step_num += 1
            reward_sum += reward
            reward_arr[step_num] = reward
            reward_sum_arr[step_num] = reward_sum

        print(f'Episode finished after {step_num} timesteps')

    env.close()
    return reward_arr, reward_sum_arr

if __name__ == '__main__':
    print_reward = False

    agent = tf.keras.models.load_model('./model_out')
    agent.summary()

    env = gym.make("InvertedPendulum-v4",render_mode = 'human')

    rewards,reward_sum = run_model(agent, env, 1, print_reward)

    # Create subplots with two rows and one column
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))

    # Plot on the first row
    axs[0].plot(rewards, label='Reward', color='blue')
    axs[0].set_title('Reward each Time Step')
    axs[0].legend()

    # Plot on the second row
    axs[1].plot(reward_sum, label='Sum of Rewards', color='orange')
    axs[1].set_title('Sum of Rewards over time')
    axs[1].legend()

    # Adjust layout to prevent clipping of titles
    plt.tight_layout()
    plt.savefig('figs/trained_model.pdf')
    # Show the plot
    plt.show()


