import pygame
from config import *
from player import Player
from sprites import Generic
import random
from overlay import Overlay

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()

        self.player = Player((640,360), self.all_sprites)
        self.overlay = Overlay(self.player)

        self.ground = {}

    def run(self, dt):
        # Background
        self.display_surface.fill((100,100,100))
        
        # Sprites
        # self.all_sprites.draw(self.display_surface)
        self.update_ground()
        self.all_sprites.customize_draw(self.player)
        self.all_sprites.update(dt)

        self.overlay.display()

    def update_ground(self):
        
        x, y = pygame.math.Vector2(self.player.rect.center)/100
        x = int(x)
        y = int(y)

        for bx in range(-6,6):
            for by in range(-6,6):
                if (bx+x,by+y) in self.ground:
                    continue

                elif False:
                    pass
                    #load_from_file
                    #self.ground.update(loaded_object)

                else:
                    self.ground[(bx+x,by+y)] = Generic(
                        pos=((bx+x)*100,(by+y)*100),
                        surf=pygame.image.load(f'./game/graphics/objects/grass_{random.randint(1,10)}.png').convert_alpha(),
                        groups=self.all_sprites,
                        z=LAYERS['GROUND']
                    )

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
    
    def customize_draw(self, player):

        self.offset.x = player.rect.centerx - 1000/2
        self.offset.y = player.rect.centery - 1000/2

        for z in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == z:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
