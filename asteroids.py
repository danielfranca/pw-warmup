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
        self.spaceship = Spaceship()
    
    def mainLoop(self):
        self.DISPLAYSURF.blit(self.background.obj, (0, 0))
