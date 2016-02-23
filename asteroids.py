#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
import pygame
from game_main import GameMain
from spaceship import Spaceship
from asteroid import Asteroid
from sprite import Sprite
from settings import SPEED, NUMBER_ASTEROIDS, LEVEL
import random

class Asteroids(GameMain):

    caption = "Asteroids"
    spaceship_bullets = []
    asteroids = []
    cur_asteroid_speed = SPEED + 2
    increased = False

    def init(self):
        self.background = Sprite('backgrounds/space.png')
        self.spaceship = Spaceship(10, 50)

    def manage_asteroids(self):
        
        for asteroid in self.asteroids:
            asteroid.move('left', asteroid.speed)
            self.DISPLAYSURF.blit(asteroid.obj, (asteroid.x, asteroid.y))
            
        self.asteroids = [ast for ast in self.asteroids if asteroid.x >= -10]

        if len(self.asteroids) < NUMBER_ASTEROIDS[LEVEL]:
            x = self.DISPLAYSURF.get_size()[0] - 30
            y = random.randint(0, self.DISPLAYSURF.get_size()[1] - 50)

            asteroid = Asteroid(x, y, self.cur_asteroid_speed)
            self.asteroids.append(asteroid)
            self.increased = False
        else:
            if not self.increased:
                self.cur_asteroid_speed += 1
                self.increased = True
    
    def mainLoop(self):
        self.background.obj = pygame.transform.scale(self.background.obj, self.DISPLAYSURF.get_size())
        self.DISPLAYSURF.blit(self.background.obj, (0, 0))

        for bullet in self.spaceship_bullets:
            bullet.x += SPEED * 3
            pygame.draw.rect(self.DISPLAYSURF, (200, 0, 0), (bullet.x, bullet.y, 4, 4))

        self.manage_asteroids()

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.spaceship.move('up', SPEED)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.spaceship.move('down', SPEED)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.spaceship.move('left', SPEED)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.spaceship.move('right', SPEED)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            left = self.spaceship.x + self.spaceship.obj.get_size()[0]
            top = self.spaceship.y + self.spaceship.obj.get_size()[1]/2 - 1

            bullet = pygame.draw.rect(self.DISPLAYSURF, (200, 0, 0), (left, top, 4, 4))
            self.spaceship_bullets.append(bullet)

        self.DISPLAYSURF.blit(self.spaceship.obj, (self.spaceship.x, self.spaceship.y))

