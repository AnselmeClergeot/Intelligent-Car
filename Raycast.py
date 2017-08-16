#coding: utf-8

from trigonometry import *
import pygame

class Raycast :
	
	def __init__(self, car, relativeAngle) :

		self.car = car
		self.relativeAngle = relativeAngle
		self.maxLength = 500
		self.increment = 5

		self.length = 0

	def updateAndDraw(self, window) :
		
		dirX, dirY = getDirection(self.car.angle + self.relativeAngle)

		self.x = self.car.x + getDirection(self.car.angle)[0] * self.car.radius
		self.y = self.car.y + getDirection(self.car.angle)[1] * self.car.radius

		curX, curY = self.x, self.y
	
		while distance(self.x, self.y, curX, curY) < self.maxLength :

			curX += dirX * self.increment
			curY += dirY * self.increment

			if self.car.environment.collide(curX, curY) :
				self.length = distance(self.x, self.y, curX, curY)
				return

			pygame.draw.rect(window, pygame.Color("blue"), (curX, curY, 2, 2))
