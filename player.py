import numpy as np
import os
from pygame import math as pmath
import pygame
from pygame.font import SysFont
from pygame import freetype
import random
from movement_models import orbit, UDLR, WASD, shift_run
from config import *
from timer import Timer
from support import import_folder
from pygame import K_r, K_LSHIFT, K_SPACE
from gui import ToolSelector


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()

        self.action         = 'down'
        self.status         = 'idle'
        self.frame_index    = 0.9
        self.gui            = ''

        self.direction  = pmath.Vector2(0,0)
        self.image      = self.animations[self.action][int(self.frame_index)]
        self.rect       = self.image.get_rect(center=pos)
        self.pos        = pmath.Vector2(self.rect.center)
        self.speed = 200

        self.timers = {
            'tool use': Timer(350, self.use_tool)
        }

        self.seeds          = ['car', 'butter']
        self.tools          = ['hand', 'hoe', 'axe']

        self.tool_selection = ToolSelector(self.tools)
    
    def use_tool(self):
        print(self.status)

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
        if self.status == 'idle':
            self.frame_index = 0.9
        self.image = self.animations[self.action][int(self.frame_index) % 4]

    def input(self):

        # Run WASD control profile
        WASD(self)

        # Run Shift Run profile
        shift_run(self)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.timers['tool use'].activate()
            self.direction = pygame.math.Vector2()
            self.frame_index = 0

    def get_tool(self):
        self.tool_selection.update()

    def get_status(self):
        if self.timers['tool use'].active:
            self.status = self.tool_selection.selected_tool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def move(self, dt):

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.tool_selection.update()
        self.get_status()
        self.move(dt)
        self.animate(dt)
        self.update_timers()

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


