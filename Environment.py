#coding: utf-8

import pygame
from trigonometry import *

class Environment :
	
	def __init__(self) :

		self.objectWidth = 5
		self.objectColor = pygame.Color("green")
		self.mapWidth = 180
		self.lastCoord = [0, 0]
		self.drawing = False
		self.paintPrecision = 3
		self.grid = []

		for i in range(self.mapWidth) :
			self.grid.append([0] * self.mapWidth)
	
	def stopDrawing(self) :
		self.drawing = False		

	def mapCoord(self, x, y) :
		return int(x) // self.objectWidth, int(y) // self.objectWidth

	def addObject(self, x, y) :
		if self.drawing == False :
			self.lastCoord[0] = x
			self.lastCoord[1] = y

		self.drawing = True

		direction = getDirectionBetween(self.lastCoord[0], self.lastCoord[1], x, y)		

		curX = self.lastCoord[0]
		curY = self.lastCoord[1]

		while distance(curX, curY, x, y) > self.paintPrecision :
			for i in range(2) :
				for j in range(2) :
					self.grid[self.mapCoord(curX, curY)[1] + i][self.mapCoord(curX, curY)[0] + j] = 1
					
			curX += direction[0]
			curY += direction[1]

		self.lastCoord[0] = curX
		self.lastCoord[1] = curY

	def reset(self) :
		for y in range(self.mapWidth) :
			for x in range(self.mapWidth) :
				self.grid[y][x] = 0

	def collide(self, x, y) :
		yCoord = self.mapCoord(x, y)[1]
		xCoord = self.mapCoord(x, y)[0]
	
		if yCoord >= self.mapWidth or xCoord >= self.mapWidth or xCoord < 0 or yCoord < 0 :
			return False

		return self.grid[yCoord][xCoord] == 1

	def draw(self, window) :
		for y in range(self.mapWidth) :
			for x in range(self.mapWidth) :
				if self.grid[y][x] == 1 :
					pygame.draw.rect(window, self.objectColor, (x * self.objectWidth, y * self.objectWidth, self.objectWidth, self.objectWidth))
