import pygame


class Timer:
    def __init__(self, duration, func=None):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False
    
    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        # Gets current time (cur_time > 0)
        cur_time = pygame.time.get_ticks()

        # If we activated, then 
        if cur_time - self.start_time <= self.duration:

            if self.func:
                self.func()

            self.deactivate()
