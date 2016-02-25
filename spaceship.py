#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
from sprite import MySprite
from pygame.transform import scale, rotate
from settings import LEVEL, MAX_LIFE

class Spaceship(MySprite):
    
    score = 0
    life = MAX_LIFE[LEVEL]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(Spaceship, self).__init__('sprites/spaceship.png')
        transColor = self.image.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.image = scale(self.image, (60, 70))
        self.image = rotate(self.image, 270)
