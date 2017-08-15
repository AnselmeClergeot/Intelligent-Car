#coding: utf-8

import pygame
from pygame.locals import *
from Car import *
from Environment import *

pygame.init()

window = pygame.display.set_mode((800, 700))
pygame.key.set_repeat(1, 1)
opened = True

environment = Environment()
multiplat = Car(environment)
tutorial = pygame.image.load("tutorial.png").convert()

while opened :
	for event in pygame.event.get() :
		if event.type == QUIT :
			opened = False
		elif event.type == KEYDOWN :
			if event.key == K_r :
				environment.reset()	

	keys = pygame.key.get_pressed()

	if keys[K_LEFT] :
		multiplat.turn("left")
	if keys[K_RIGHT] :
		multiplat.turn("right")
	if keys[K_UP] :
		multiplat.accelerate()
	if keys[K_DOWN] :
		multiplat.decelerate()

	if pygame.mouse.get_pressed()[0] :
		environment.addObject(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

	multiplat.update()

	pygame.draw.rect(window, pygame.Color("black"), (0, 0, 800, 700))	

	environment.draw(window)
	multiplat.draw(window)
	window.blit(tutorial, (0, 0))

	pygame.display.flip()
