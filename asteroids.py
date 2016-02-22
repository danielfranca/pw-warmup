#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
import pygame
from game_main import GameMain
from spaceship import Spaceship
from sprite import Sprite

class Asteroids(GameMain):

    caption = "Asteroids"

    def init(self):
        self.background = Sprite('backgrounds/space.png')
        self.spaceship = Spaceship(10, 50)
    
    def mainLoop(self):
        self.background.obj = pygame.transform.scale(self.background.obj, self.DISPLAYSURF.get_size())
        self.DISPLAYSURF.blit(self.background.obj, (0, 0))

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.spaceship.move('up')
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.spaceship.move('down')
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.spaceship.move('left')
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.spaceship.move('right')

        self.DISPLAYSURF.blit(self.spaceship.obj, (self.spaceship.position['x'], self.spaceship.position['y']))

