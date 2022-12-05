import pygame, sys
from config import *
from player import Player
from level import Level
from random import randint

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0,0), flags=pygame.RESIZABLE)
        pygame.display.set_caption('Something')
        self.clock = pygame.time.Clock()
        self.level = Level(randint(1,10000))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()

