#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
from sprite import Sprite
from settings import LEVEL, MAX_LIFE

class Spaceship(Sprite):
    
    score = 0
    life = MAX_LIFE[LEVEL]

    def __init__(self):
        super(Spaceship, self).__init__('sprites/spaceship.png')
