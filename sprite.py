#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
import pygame
from pygame.sprite import Sprite

class MySprite(Sprite):

    image = None

    def __init__(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()

    def move(self, side, speed):
        if side == 'left':
            self.rect.x -= speed
        elif side == 'right':
            self.rect.x += speed
        elif side == 'up':
            self.rect.y -= speed
        elif side == 'down':
            self.rect.y += speed
