import pygame
from config import *
from player import Player
from gui import ToolSelector

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        self.player = Player((640,360), self.all_sprites)
        self.tool_selector = ToolSelector(['hand', 'bow', 'sword', 'pickaxe'])

    def run(self, dt):
        # Background
        self.display_surface.fill((100,100,100))
        
        # Sprites
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        
        # Gui
        self.tool_selector.update()
