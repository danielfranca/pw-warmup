#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
import pygame

class Sprite(object):

    x = 0
    y = 0
    obj = None
    
    def __init__(self, filename):
        self.obj = pygame.image.load(filename)

