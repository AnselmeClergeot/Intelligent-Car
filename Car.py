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
		self.turnSpeed = 0.2
		self.acceleration = 0.0005
		self.sensorsNb = 7
		self.visionAngle = 130
		self.curSpeed = 0
		self.maxSpeed = 0.8

		self.environment = environment

		self.sensors = []

		self.lastFrame = 0
		self.elapsed = 0

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
			self.angle -= self.turnSpeed * self.elapsed
		else :
			self.angle += self.turnSpeed * self.elapsed

		self.angle %= 360

	def accelerate(self) :
		self.curSpeed += self.acceleration * self.elapsed
		if self.curSpeed > self.maxSpeed :
			self.curSpeed = self.maxSpeed

	def decelerate(self) :
		self.curSpeed -= self.acceleration * self.elapsed
		if self.curSpeed < -self.maxSpeed :
			self.curSpeed = -self.maxSpeed

		
	def update(self) :
		self.elapsed = pygame.time.get_ticks() - self.lastFrame
		self.lastFrame = pygame.time.get_ticks()

		xDir = self.curSpeed * getDirection(self.angle)[0] * self.elapsed
		yDir = self.curSpeed * getDirection(self.angle)[1] * self.elapsed

		if not(self.environment.collide(self.x + xDir, self.y + yDir)) :
			self.x += xDir
			self.y += yDir

	def learn(self) :
		self.ia.learn()
