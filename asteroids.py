#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
import pygame
from game_main import GameMain

class Asteroids(GameMain):

    caption = "Asteroids"
    
    def mainLoop(self):
        self.surface = pygame.image.load('backgrounds/space.png').convert()
