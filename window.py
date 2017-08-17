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

iaActive = False

while opened :
	for event in pygame.event.get() :
		if event.type == QUIT :
			opened = False
		elif event.type == KEYDOWN :
			if event.key == K_s :
				multiplat.setLearning(not(multiplat.learning))
				iaActive = False
			elif event.key == K_d :
				iaActive = not(iaActive)
				multiplat.setLearning(False)
			elif event.key == K_r :
				environment.reset()

	keys = pygame.key.get_pressed()

	if keys[K_UP] :
		multiplat.accelerate()
	if keys[K_LEFT] :
		multiplat.turn("left")
	if keys[K_RIGHT] :
		multiplat.turn("right")

	if pygame.mouse.get_pressed()[0] :
		environment.addObject(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

	multiplat.update()

	multiplat.learnExample()

	if iaActive :
		multiplat.driveSelf()

	pygame.draw.rect(window, pygame.Color("black"), (0, 0, 800, 700))

	environment.draw(window)
	multiplat.draw(window)
	window.blit(tutorial, (0, 0))

	pygame.display.flip()
