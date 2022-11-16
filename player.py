import numpy as np
import os
import math
import pygame
from pygame.font import SysFont
from pygame import freetype
import random
from display import Display
from movement_models import orbit
from config import *
from support import import_folder
from pygame import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_r,
    K_LSHIFT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()

        self.status = 'down'
        self.frame_index = 0

        self.direction = pygame.math.Vector2(0,0)
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)

        self.speed = 200

    def import_assets(self):
        self.animations = {
            'up':    [],
            'down':  [],
            'left':  [],
            'right': [],
        }

        for animation in self.animations.keys():
            full_path = 'game/graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 4 * dt
        self.image = self.animations[self.status][int(self.frame_index) % 4]

    def input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def move(self, dt):

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)

U=0
D=1
L=2
R=3

class PlayerB(pygame.sprite.Sprite):

    def __init__(self, shape='circle',):

        super(Player, self).__init__()

        self.x, self.y = (SCREENWIDTH/2, SCREENHIGHT/2)
        self.w, self.h = (5, 60)
        self.max_vel   = 5

        self.accel     = 0.2
        self.xvel      = 0
        self.yvel      = 0
        self.direction = 0 # 0=N 1=S 2=E 3=W

        self.isJump = False
        self.jumpCount = 10

        self.surf = pygame.Surface((100,50))
        self.surf.fill((255,255,255))

        freetype.init()
        self.text = freetype.SysFont('debug', size=10)

        self.display = Display()

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[K_r]:
            self.max_vel = (random.randint(0,9))
        elif keys[K_LSHIFT]:
            self.max_vel = 2
        elif keys[K_SPACE]:
            self.max_vel = 10
        else:
            self.max_vel = 5

        self.xvel, self.yvel = orbit((self.x,self.y),(self.xvel,self.yvel),self.accel)

        self.x += self.xvel
        self.y += self.yvel

        self.display.screen.blit(
            SysFont(None,24).render(
                str((self.xvel, self.yvel)), True, (0,255,255)
            ),
            (20,20)
        )

        pygame.draw.circle(self.display.screen, (255, 0, 255), (int(self.x),  int(self.y)), int(self.w))

class NPC(pygame.sprite.Sprite):

    def __init__(self, loc, shape, vel):

        super(Player, self).__init__()

        self.x, self.y = loc
        self.w, self.h = shape
        self.vel       = vel
    

