import pygame
from config import *
from player import Player
from gui import ToolSelector
from overlay import Overlay

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()

        self.player = Player((640,360), self.all_sprites)
        self.overlay = Overlay(self.player)

    def run(self, dt):
        # Background
        self.display_surface.fill((100,100,100))
        
        # Sprites
        # self.all_sprites.draw(self.display_surface)
        self.all_sprites.customize_draw()
        self.all_sprites.update(dt)

        self.overlay.display()

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
    
    def customize_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)
