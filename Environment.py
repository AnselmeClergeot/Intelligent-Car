#coding: utf-8

import pygame

class Environment :
	
	def __init__(self) :
		self.objectWidth = 25
		self.objectColor = pygame.Color("green")

		self.objects = []

	def addObject(self, x, y) :
		self.objects.append((x, y))

	def reset(self) :
		self.objects = []

	def draw(self, window) :
		for coord in self.objects :
			pygame.draw.rect(window, self.objectColor, (coord[0] - self.objectWidth/2, coord[1] - self.objectWidth/2, self.objectWidth, self.objectWidth))
