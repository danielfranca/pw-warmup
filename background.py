#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
from sprite import MySprite
from pygame.transform import scale, rotate
from settings import LEVEL, MAX_LIFE, SPEED

class Background(MySprite):
    
    def __init__(self, x, y):
        super(Background, self).__init__('backgrounds/space.png')
