import gymnasium as gym
import tensorflow as tf

import sac

def make_env():
    return gym.make("InvertedPendulum-v4")

if __name__ == '__main__':
    save_path = './model_out'
    
    ac_kwargs = dict(hidden_sizes=[16, 16],
                     activation=tf.nn.relu)
    
    logger_kwargs = dict(output_dir = './logger_out',
                        exp_name='Watch out, Pendulum!')

    sac.sac(make_env, 
        ac_kwargs = ac_kwargs,
        total_steps = 200000,
        log_every = 2000,
        replay_size=10_000,
        start_steps=1_000,
        update_after=1_000,
        max_ep_len=200,
        logger_kwargs=logger_kwargs,
        save_freq=200_000,
        save_path=save_path)
