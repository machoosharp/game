import pygame
from config import *
from enum import Enum


class Overlay:
    def __init__(self, player):

        self.display_surface = pygame.display.get_surface()
        self.player = player

        overlay_path = './game/graphics/overlay/'
        self.tools_surf = {tool:pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in self.player.tools}
        self.seeds_surf = {seed:pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in self.player.seeds}

        print(self.tools_surf)
        print(self.seeds_surf)

