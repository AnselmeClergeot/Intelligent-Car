#coding: utf-8

import pygame

class Environment :
	
	def __init__(self) :
		self.objectWidth = 10
		self.objectColor = pygame.Color("green")

		self.mapWidth = 90

		self.grid = []

		for i in range(self.mapWidth) :
			self.grid.append([0] * self.mapWidth)


	def addObject(self, x, y) :

		for i in range(2) :
			for j in range(2) :
				self.grid[int(y) // self.objectWidth + i][int(x) // self.objectWidth + j] = 1

	def reset(self) :
		for y in range(self.mapWidth) :
			for x in range(self.mapWidth) :
				self.grid[y][x] = 0

	def collide(self, x, y) :
		yCoord = int(y) // self.objectWidth
		xCoord = int(x) // self.objectWidth
	
		if yCoord >= self.mapWidth or xCoord >= self.mapWidth or xCoord < 0 or yCoord < 0 :
			return False

		return self.grid[yCoord][xCoord] == 1

	def draw(self, window) :

		for y in range(self.mapWidth) :
			for x in range(self.mapWidth) :
				if self.grid[y][x] == 1 :
					pygame.draw.rect(window, self.objectColor, (x * self.objectWidth, y * self.objectWidth, self.objectWidth, self.objectWidth))
