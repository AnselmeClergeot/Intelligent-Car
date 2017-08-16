#coding: utf-8

import pygame

class Environment :
	
	def __init__(self) :
		self.objectWidth = 20
		self.objectColor = pygame.Color("green")

		self.mapWidth = 100

		self.grid = []

		for i in range(self.mapWidth) :
			self.grid.append([0] * self.mapWidth)


	def addObject(self, x, y) :
		self.grid[int(y) // self.objectWidth][int(x) // self.objectWidth] = 1

	def collide(self, x, y) :
		return self.grid[int(y) // self.objectWidth][int(x) // self.objectWidth] == 1

	def draw(self, window) :

		for y in range(self.mapWidth) :
			for x in range(self.mapWidth) :
				if self.grid[y][x] == 1 :
					pygame.draw.rect(window, self.objectColor, (x * self.objectWidth, y * self.objectWidth, self.objectWidth, self.objectWidth))
