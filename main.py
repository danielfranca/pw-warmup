#!/usr/bin/env python
# -*- coding: UTF-8 -*-#

#TODO
#Add asteroids
#Show life
#Show score
#Check screen limits
#Clear arrays with bullets/asteroids
#del asteroid when hit asteroid
#del you when asteroid hits you
#Decrement life when asteroid hits you
#Increment score when you hit asteroid

from asteroids import Asteroids

if __name__ == '__main__':
    gm = Asteroids()
    gm.run()
