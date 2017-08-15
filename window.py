#coding: utf-8

import pygame
from pygame.locals import *
from Car import *

pygame.init()

window = pygame.display.set_mode((800, 700))
pygame.key.set_repeat(1, 1)
opened = True

multiplat = Car()

while opened :
	for event in pygame.event.get() :
		if event.type == QUIT :
			opened = False

	keys = pygame.key.get_pressed()

	if keys[K_LEFT] :
		multiplat.turn("left")
	if keys[K_RIGHT] :
		multiplat.turn("right")
	if keys[K_UP] :
		multiplat.accelerate()
	if keys[K_DOWN] :
		multiplat.decelerate()

	multiplat.update()

	pygame.draw.rect(window, pygame.Color("black"), (0, 0, 800, 700))	

	multiplat.draw(window)

	pygame.display.flip()
