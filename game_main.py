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

        #import ipdb; ipdb.set_trace()
        self.DISPLAYSURF = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption(self.caption)

        self.init()
        
        while(True):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.mainLoop()

            pygame.display.flip()
            self.fpsClock.tick(FPS)
