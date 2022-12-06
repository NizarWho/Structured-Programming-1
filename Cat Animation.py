# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 12:12:18 2022

@author: nza7
"""

import sys, pygame
from pygame.locals import +
pygame.init()
fps = 30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400,300), 0,32)
pygame.display.set_caption('Cat Animation')
WHITE = (255,255,255)
catImg = pygame.image.load('17_cat.png')
catx = 10
caty = 10
direction = 'right'
while true:
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
            DISPLAYSURF.blit(carImg, (catx, caty))
            for event in pygame.event.get():
                if event.type == Quit:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            fpsClock.tick(FPS)
            