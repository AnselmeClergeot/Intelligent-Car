#coding: utf-8

import pygame
from pygame.locals import *
from Car import *
from Environment import *

pygame.init()

window = pygame.display.set_mode((800, 700))
opened = True

environment = Environment()
multiplat = Car(environment)
tutorial = pygame.image.load("tutorial.png").convert()

learning = False
iaActive = False

while opened :
	for event in pygame.event.get() :
		if event.type == QUIT :
			opened = False
		elif event.type == KEYDOWN :
			if event.key == K_s :
				learning = not(learning)
				iaActive = False
				print(learning)
			elif event.key == K_d :
				iaActive = not(iaActive)
				learning= False


	keys = pygame.key.get_pressed()

	if keys[K_UP] :
		multiplat.accelerate()
	if keys[K_DOWN] :
		multiplat.decelerate()
	if keys[K_LEFT] :
		multiplat.turn("left")
	if keys[K_RIGHT] :
		multiplat.turn("right")

	if pygame.mouse.get_pressed()[0] :
		environment.addObject(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

	multiplat.update()

	if learning :
		multiplat.learn()
	
	if iaActive :
		multiplat.driveSelf()

	pygame.draw.rect(window, pygame.Color("black"), (0, 0, 800, 700))	

	environment.draw(window)
	multiplat.draw(window)
	window.blit(tutorial, (0, 0))

	pygame.display.flip()
