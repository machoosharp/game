import numpy as np
import pygame
from pygame import display
import random
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

class Display:

    def __new__(cls):
        if not hasattr(cls, '_ints_'):
            cls._inst_ = super(Display, cls).__new__(cls)
        return cls._inst_

    def __init__(self, name=None, w=None, h=None):

        if name:
            display.set_caption(name)
        if w is None and h is None:
            disp_data = display.Info()
            w = disp_data.current_w
            h = disp_data.current_h

        self.screen = display.set_mode((w, h) )

    def update(self):
        display.flip()
        self.screen.fill((30,30,30))
