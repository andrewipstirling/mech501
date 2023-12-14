# Reinforcement Learning for Inverted Pendulum Control

### Andrew Stirling

## Introduction

Control theory, is centred around the behaviour of dynamic systems, and how as
engineers we can force it to behave in a certain way. In the context of Mechanical Engineering, these systems could vary from robotics, to automotive systems, to aerospace and HVAC applications. A large portion of Control design is spent modelling the system or "plant". This requires a good grasp of the system's mechanics, understanding all variables that may influence its behaviour. For complex systems, these dynamics are highly non-linear, while exhibiting large degrees of freedom. In such applications, traditional control techniques may struggle to produce reliable and accurate behaviour. Moreover, we may not even be able to model the system, making any form of controller design impossible. 

In these cases, we can make use of Reinforcement Learning (RL) for controlling such complex systems. RL operates in a model-free fashion, meaning we are not required to have an explicit model of a system's behaviour given various inputs. Using RL, we can effectively sidestep all the disadvantages of model-based controller design. RL generally consists of an agent who, through interacting with an environment, can learn to map various situations to actions. Specifically, the environment provides responses to each a agent's action, using these responses and rewards dependent on various states of the agent, we can condition the agent's decisions towards optimal states. In class, the problems we solved required the action and/or the state to be discretizable. However, for continuous systems, this may not be possible or if it is, it raises the question to what resolution we look to discretize the space or actions. The Soft Actor-Critic architecture is a form of RL that looks to solve this problem. 

In this project, we look to investigate RL's applications and performance in control settings. Specifically, we look to investigate the Soft Actor-Critic (SAC) architecture's ability to control a continuous system, consisting of an inverted pendulum on a cart. 

### The Inverted Pendulum

The inverted problem is a "classic" problem in Control Theory. In this experiment, we have a pendulum or pole on top of a cart, which can move side to side. The goal is to keep the pendulum upright, by applying varied forces to the cart. The Farama-Foundation provides the "gymnasium" environment (formerly maintained by OpenAI), which allows us to test various RL architectures applied to this problem. Pre-defined in this environment is a continuous action space in the range [-3, 3] N, which represents the amount of force we can apply to the cart. Similarly, the observations space consists of 4 states represented as an ndarry with shape 4 holding the position of the cart along the slider, vertical angle of the pole on the cart, linear velocity of the cart, and angular velocity of the pole on the cart, respectively. All values can be in the range of [-Inf, Inf]. The reward is +1 for every timestep that the pole is upright. To get a sense of how the pendulum acts, we can start with random actions to see how it responds. The episode ends when either the episode duration reaches 1000 timesteps, any of the state space values are no longer finite, or the vertical angle of the pendulum drops to below 90 degrees, equivalent to below the cart.

### Project

This project implements the SAC framework from https://github.com/openai/spinningup, for the inverted pendulum in the gymnasium environment found at https://github.com/Farama-Foundation/Gymnasium. The final presentation can be found in the *soft_actor_critic.ipynb* notebook, and all code in the relevant files.