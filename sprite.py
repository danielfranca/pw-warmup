#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
import pygame

class Sprite(object):

    x = 0
    y = 0
    obj = None

    def __init__(self, filename):
        self.obj = pygame.image.load(filename).convert()

    def move(self, side, speed):
        if side == 'left':
            self.x -= speed
        elif side == 'right':
            self.x += speed
        elif side == 'up':
            self.y -= speed
        elif side == 'down':
            self.y += speed
