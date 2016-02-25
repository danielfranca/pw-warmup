#!/usr/bin/env python
# -*- coding: UTF-8 -*-#
import pygame
from game_main import GameMain
from spaceship import Spaceship
from asteroid import Asteroid
from sprite import MySprite
from settings import SPEED, NUMBER_ASTEROIDS, LEVEL
import random

class Asteroids(GameMain):

    caption = "Asteroids"
    spaceship_bullets = []
    asteroids = []
    cur_asteroid_speed = SPEED + 2
    increased = False

    def init(self):
        self.background = MySprite('backgrounds/space.png')
        self.spaceship = Spaceship(10, 50)

    def manage_asteroids(self):
        
        for asteroid in self.asteroids:
            asteroid.move('left', asteroid.speed)
            self.DISPLAYSURF.blit(asteroid.image, (asteroid.rect.x, asteroid.rect.y))
            
        self.asteroids = [ast for ast in self.asteroids if asteroid.rect.x >= -10]

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

    def objects_collide(self, a, b):

        if isinstance(a, pygame.Rect):
            rectA = a
        else:
            rectA = a.rect #pygame.Rect(a.obj.x, a.obj.y, a.obj.width, a.obj.height)
        
        if isinstance(b, pygame.Rect):
            rectB = b
        else:
            rectB = b.rect #pygame.Rect(b.obj.x, b.obj.y, b.obj.width, b.obj.height)

        if rectA.colliderect(rectB):
            return True
        return False

    def check_hit_asteroid(self, bullet):
        self.asteroids = [ast for ast in self.asteroids if not self.objects_collide(bullet, ast)]
    
    def did_i_die(self):
        for asteroid in self.asteroids:
            if self.objects_collide(asteroid, self.spaceship):
                return True

        return False

    def mainLoop(self):

        self.background.image = pygame.transform.scale(self.background.image, self.DISPLAYSURF.get_size())
        self.DISPLAYSURF.blit(self.background.image, (0, 0))

        for bullet in self.spaceship_bullets:
            bullet.x += SPEED * 3
            pygame.draw.rect(self.DISPLAYSURF, (200, 0, 0), (bullet.x, bullet.y, 4, 4))
            #Check if the bullet hits any asteroid
            self.check_hit_asteroid(bullet)

        self.manage_asteroids()

        #if self.did_i_die():
        #    del self.spaceship
        #    pygame.time.wait(2000)
        #    exit(0)

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.spaceship.move('up', SPEED)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.spaceship.move('down', SPEED)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.spaceship.move('left', SPEED)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.spaceship.move('right', SPEED)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            left = self.spaceship.rect.x + self.spaceship.image.get_size()[0]
            top = self.spaceship.rect.y + self.spaceship.image.get_size()[1]/2 - 1

            bullet = pygame.draw.rect(self.DISPLAYSURF, (200, 0, 0), (left, top, 4, 4))
            self.spaceship_bullets.append(bullet)

        self.DISPLAYSURF.blit(self.spaceship.image, (self.spaceship.rect.x, self.spaceship.rect.y))

