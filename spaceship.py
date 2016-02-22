#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
from sprite import Sprite
from settings import LEVEL, MAX_LIFE, SPEED

class Spaceship(Sprite):
    
    score = 0
    life = MAX_LIFE[LEVEL]
    position = {'x': 0, 'y': 0}

    def move(self, side):
        if side == 'left':
            self.position['x'] -= SPEED
        elif side == 'right':
            self.position['x'] += SPEED
        elif side == 'up':
            self.position['y'] -= SPEED
        elif side == 'down':
            self.position['y'] += SPEED

    def __init__(self, x, y):
        self.position['x'] = x
        self.position['y'] = y
        super(Spaceship, self).__init__('sprites/spaceship.png')
