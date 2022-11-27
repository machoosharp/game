import pygame, sys
import pygame
from pygame import Color
import math
from config import *

class ToolSelector(pygame.Surface):
    def __init__(self, tools):
        super().__init__((GUI_LEN,GUI_LEN))

        self.font    = pygame.font.SysFont(None, 24)
        self.rect    = pygame.Rect((ORIGX, ORIGY), (GUI_LEN, GUI_LEN))
        self.screen  = pygame.display.get_surface()
        self.visible = False
        self.tools   = tools
        self.selected_tool = tools[0]

        self.tool_buttons = {}

        self.fill((100,100,100,100))

    def show(self):
        self.visible = True
        self.fill(BGRND)
        grid_wh  = math.ceil(math.sqrt(len(self.tools)))
        btn_size = GUI_LEN/grid_wh
        btn_orig = [( ORIGX + x * btn_size , ORIGY + y * btn_size ) for x in range(grid_wh) for y in range(grid_wh)]

        for idx in range(len(self.tools)):

            x, y = btn_orig[idx]

            rect = pygame.Rect(
                ( x+BORDER_OFFSET, y+BORDER_OFFSET ),
                ( btn_size-BORDER_OFFSET, btn_size-BORDER_OFFSET )
            )

            self.tool_buttons[self.tools[idx]] = rect

    def hide(self):
        self.visible = False
        self.fill(INVIS)
    
    def draw(self):
        pygame.draw.rect(self.screen, (0,100,200,100), self.rect)
        for tool, rect in self.tool_buttons.items():
            text = self.font.render(tool, True, (0,0,0,100))
            pygame.draw.rect(self.screen, (200,255,220,100), rect)
            w, h = text.get_size()
            self.screen.blit(text, (rect.x + (rect.w/2) - (w/2), rect.y + (rect.h/2) - (h/2)))

    def update(self):
        self.input()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e] and not self.visible:
            self.show()

        if keys[pygame.K_ESCAPE] and self.visible:
            self.hide()

        if self.visible:
            self.draw()
            self.get_tool()

        if keys[pygame.K_p]:
            self.tools = ['hand', 'knife', 'penis', 'Big Dong', 'chicken', 'gun']

    def get_tool(self):
        mousx, mousy = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            for tool, rect in self.tool_buttons.items():
                if (mousx > rect.x 
                and mousx < rect.x + rect.w
                and mousy > rect.y
                and mousy < rect.y + rect.h):
                    self.selected_tool = tool
                    self.hide()
                    print(self.selected_tool)
                    return




