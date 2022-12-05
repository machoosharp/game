import pygame
from config import *
from player import Player
from sprites import Generic
import random
from overlay import Overlay
from perlin_noise import PerlinNoise
import math

class Level:
    def __init__(self, seed):

        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()

        self.player = Player((0,0), self.all_sprites)
        self.overlay = Overlay(self.player)

        print('ground seed is ' + str(seed))
        self.ground_seed = PerlinNoise(16, seed=seed)
        print('ground seed is ' + str(seed))
        self.ground_seed_2 = PerlinNoise(3, seed=seed)

        self.biome_seed = PerlinNoise(3,seed=seed)

        self.rendered_ground = {}

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

        # Exact player location devided by pixels per unit is concidered the coordinates.
        x, y = pygame.math.Vector2(self.player.rect.center)/PPU

        # Need to be intergers so we aren't updating on decimal coordinates
        player_x = int(x)
        player_y = int(y)

        for coords in self.generate_render_coords(player_x, player_y):

            if coords in self.rendered_ground:
                continue

            elif False:
                pass
                #load_from_file
                #self.ground.update(loaded_object)

            else:
                g_val = self.ground_seed((pygame.math.Vector2(coords)/100))
                scaling = self.ground_seed_2((pygame.math.Vector2(coords)/100)) * 4

                b_val = self.biome_seed((pygame.math.Vector2(coords[0]/2,coords[1]/2)/100))

                g = self.scale(( g_val + 1 ) / 2, scaling)
                b = self.scale(( b_val + 1 ) / 2, 2)

                surf = pygame.Surface((PPU,PPU))
                if g < 0.3:
                    surf.fill((50,100,255))
                elif g > 0.8:
                    surf.fill((200,200,200))
                else:
                    if b > 0.3:
                        surf.fill(self.green(g))
                    else:
                        surf.fill(self.tan(g))

                self.rendered_ground[coords] = Generic(
                    pos=self.coord_to_pixel(coords),
                    surf=surf,
                    groups=self.all_sprites,
                    z=LAYERS['GROUND']
                )
                
                # self.rendered_ground[coords] = Generic(
                #     pos=self.coords_to_pixel(coords),
                #     surf=pygame.image.load(f'./game/graphics/objects/grass_{random.randint(1,10)}.png').convert_alpha(),
                #     groups=self.all_sprites,
                #     z=LAYERS['GROUND']
                # )
        

    def green(self, g):
        return [ 0, int( g * 255 ), 0 ]
    
    def tan(self, g):
        return [ int( g * 255 ), int( g * 208 ), int( g * 150 ) ]
    
    def scale(self, val, scale):
        return max(min(scale * val - (0.5 * scale - 0.5), 1.0),0)

    def generate_render_coords(self, x: int, y: int):
        # Getting a map of all the coordinates in Render distance relative to the player
        return [
            ( xr + x, yr + y ) 
            for xr in range( -RENDER_DISTANCE, RENDER_DISTANCE ) 
            for yr in range( -RENDER_DISTANCE, RENDER_DISTANCE )
        ]
    
    @staticmethod
    def coord_to_pixel(coords):
        return (coords[0]*PPU, coords[1]*PPU)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
    
    def customize_draw(self, player):

        self.offset.x = player.rect.centerx - pygame.display.Info().current_w/2
        self.offset.y = player.rect.centery - pygame.display.Info().current_h/2

        for z in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == z:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
