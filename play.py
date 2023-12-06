import gymnasium as gym
from gymnasium.utils.play import play
import pygame

mapping = {(pygame.K_LEFT,): -1, (pygame.K_RIGHT,): 1}
play(gym.make("InvertedPendulum-v4",render_mode = 'rgb_array'), keys_to_action=mapping)

