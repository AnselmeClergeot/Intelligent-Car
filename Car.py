#coding: utf-8

import pygame
from trigonometry import *
from Raycast import *
from IADriver import *

class Car :
	
	def __init__(self, environment) :
		
		self.x, self.y = 400, 350
		self.radius = 5
		self.angle = 0
		self.turnSpeed = 2.5
		self.speed = 7
		self.sensorsNb = 5
		self.visionAngle = 150

		self.environment = environment

		self.sensors = []

		for angle in xrange(-self.visionAngle/2, self.visionAngle/2 + 1, self.visionAngle / (self.sensorsNb - 1)) :
			self.sensors.append(Raycast(self, angle))
		
		self.ia = IADriver(self)

	def driveSelf(self) :
		self.ia.driveSelf()

	def draw(self, window) :
		pygame.draw.circle(window, pygame.Color("white"), (int(self.x), int(self.y)), self.radius)
		
		for ray in self.sensors :
			ray.updateAndDraw(window)

	def turn(self, direction) :
		if direction == "left" :
			self.angle -= self.turnSpeed
		else :
			self.angle += self.turnSpeed

		self.angle %= 360

	def go(self, direction) :

		xDir = self.speed * getDirection(self.angle)[0] * direction
		yDir = self.speed * getDirection(self.angle)[1] * direction

		colliding = False
	
		for square in self.environment.objects :
			if inSquare(self.x + xDir, self.y + yDir, square[0], square[1], self.environment.objectWidth) :
				colliding = True

		if not(colliding) :
			self.x += xDir
			self.y += yDir

	def learn(self) :
		self.ia.learn()
