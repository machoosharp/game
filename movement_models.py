import numpy as np
import math
import pygame
from pygame import freetype
import random
from display import Display
from config import *
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

U=0
D=1
L=2
R=3

def orbit(loc_profile, vel_profile, accel:float=0.2, friction=1):

        keys = pygame.key.get_pressed()
        mous_x, mous_y = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]

        x, y = loc_profile
        xvel, yvel = vel_profile

        # if clicked:
        #     xvel += accel * (1 if (mous_x - x) > 0 else -1)
        #     yvel += accel * (1 if (mous_y - y) > 0 else -1)
        # else:
        #     xvel += accel * (-1 if xvel > 0 else 1)
        #     yvel += accel * (-1 if yvel > 0 else 1)

        if clicked:

            xadder = accel * ((mous_x - x) * friction)
            
            if xvel < 0 and (mous_x - x) > 0:
                xadder += 1*xadder
            if xvel > 0 and (mous_x - x) < 0:
                xadder += 1*xadder
            xvel += xadder

            yadder = accel * ((mous_y - y) * friction)
            
            if yvel < 0 and (mous_y - y) > 0:
                yadder += 1*yadder
            if yvel > 0 and (mous_y - y) < 0:
                yadder += 1*yadder
            yvel += yadder

        else:
            xvel += accel * (-1 if xvel > 0 else 1)
            yvel += accel * (-1 if yvel > 0 else 1)

        if not abs(xvel) > accel and not clicked:
            xvel = 0
        if not abs(yvel) > accel and not clicked:
            yvel = 0

        xvel = round(xvel,3)
        yvel = round(yvel,3)

        return xvel, yvel

def keyboard_control(loc_profile, vel_profile, accel=0.2, max_vel=5):

    keys = pygame.key.get_pressed()
    mous_x, mous_y = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()[0]

    x, y = loc_profile
    xvel, yvel = vel_profile

    if keys[K_UP]:
        direction = U
        if yvel > -max_vel:
            yvel -= accel
    elif keys[K_DOWN]:
        direction = D
        if yvel < max_vel:
            yvel += accel
    else:
        if yvel > accel:
            yvel -= accel * 2
        elif yvel < -accel:
            yvel += accel * 2
        else:
            yvel = 0

    if keys[K_RIGHT]:
        direction = R
        if xvel < max_vel:
            xvel += accel
    elif keys[K_LEFT]:
        direction = L
        if xvel > -max_vel:
            xvel -= accel
    else:
        if xvel > accel:
            xvel -= accel * 2
        elif xvel < -accel:
            xvel += accel * 2
        else:
            xvel = 0

    return xvel, yvel

def cubic_control(loc_profile, speed, direction):
    x, y = loc_profile

def cubic_auto(loc_profile, speed, destination):
    x, y = loc_profile
