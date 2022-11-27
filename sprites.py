import pygame
import random
from config import *


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z=LAYERS['MAIN']):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_rect(center=pos)
        self.z = z
    
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
                        groups=self.cam_group,
                        z=LAYERS['GROUND']
                    )
