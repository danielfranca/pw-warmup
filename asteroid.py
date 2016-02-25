#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
from sprite import MySprite
from pygame.transform import scale, rotate

class Asteroid(MySprite):
    
    def __init__(self, x, y, speed):
        super(Asteroid, self).__init__('sprites/asteroid.png')
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        transColor = self.image.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.image = scale(self.image, (60, 70))
