#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
from sprite import Sprite
from pygame.transform import scale, rotate
from settings import LEVEL, MAX_LIFE

class Spaceship(Sprite):
    
    score = 0
    life = MAX_LIFE[LEVEL]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(Spaceship, self).__init__('sprites/spaceship.png')
        transColor = self.obj.get_at((0,0))
        self.obj.set_colorkey(transColor)
        self.obj = scale(self.obj, (60, 70))
        self.obj = rotate(self.obj, 270)
