#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
import pygame, sys
from pygame.locals import *

class GameMain(object):
    
    def mainLoop(self):
        pass

    def run(self):
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((800, 600)).convert()
        pygame.display.set_caption(self.caption)
        
        while(True):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.mainLoop()
            pygame.display.update()
