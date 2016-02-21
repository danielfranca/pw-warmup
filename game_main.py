#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
import pygame, sys
from pygame.locals import *
from settings import FPS

class GameMain(object):
    
    def init(self):
        pass

    def mainLoop(self):
        pass

    def run(self):
        pygame.init()

        self.fpsClock = pygame.time.Clock()

        self.DISPLAYSURF = pygame.display.set_mode((800, 600)).convert()
        pygame.display.set_caption(self.caption)

        self.init()
        
        while(True):
            self.mainLoop()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.fpsClock.tick(FPS)
