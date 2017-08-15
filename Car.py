#coding: utf-8

import pygame
from trigonometry import *
from Raycast import *

class Car :
	
	def __init__(self, environment) :
		
		self.x, self.y = 400, 350
		self.radius = 10
		self.angle = 0
		self.turnSpeed = 2
		self.curSpeed = 0
		self.acceleration = 0.1
		self.deceleration = 0.05
		self.speedLoss = 0.005
		self.maxSpeed = 5
		self.sensorsNb = 3
		self.visionAngle = 100

		self.lastFrame = 0
		self.elapsed = 0
		self.timeCoeff = 0.1 #Updating movements in respect to elapsed time since last frame. Coefficient is to adjust movement speeds without having to change them.

		self.environment = environment

		self.sensors = []

		for angle in xrange(-self.visionAngle/2, self.visionAngle/2 + 1, self.visionAngle / (self.sensorsNb - 1)) :
			self.sensors.append(Raycast(self, angle))

	def draw(self, window) :
		pygame.draw.circle(window, pygame.Color("white"), (int(self.x), int(self.y)), self.radius)
		
		for ray in self.sensors :
			ray.updateAndDraw(window)

	def turn(self, direction) :
		
		epsilon = 0.1

		if math.fabs(self.curSpeed) < epsilon :
			return

		if self.curSpeed == 0 :
			return

		if direction == "left" :
			self.angle -= self.turnSpeed * self.elapsed * self.timeCoeff
		else :
			self.angle += self.turnSpeed * self.elapsed * self.timeCoeff

		self.angle %= 360

	def accelerate(self) :
		self.curSpeed += self.acceleration * self.elapsed * self.timeCoeff
		self.checkSpeed()

	def decelerate(self) :
		self.curSpeed -= self.deceleration * self.elapsed * self.timeCoeff
		
		self.checkSpeed()	

	def checkSpeed(self) :
		if self.curSpeed < -self.maxSpeed :
			self.curSpeed = -self.maxSpeed
		elif self.curSpeed > self.maxSpeed :
			self.curSpeed = self.maxSpeed

	def loseSpeed(self) :
		zeroSpeedDir = 0

		if self.curSpeed > 0 :
			zeroSpeedDir = -1
		else :
			zeroSpeedDir = 1

		self.curSpeed += zeroSpeedDir * self.speedLoss * self.elapsed * self.timeCoeff

		epsilon = 0.01

		if math.fabs(self.curSpeed) < epsilon :
			self.curSpeed = 0

	def update(self) :

		self.elapsed = pygame.time.get_ticks() - self.lastFrame
		self.lastFrame = pygame.time.get_ticks()

		xSpeed = getDirection(self.angle)[0] * self.curSpeed * self.elapsed * self.timeCoeff
		ySpeed = getDirection(self.angle)[1] * self.curSpeed * self.elapsed * self.timeCoeff
		
		collide = False

		for obstacle in self.environment.objects :
			if distance(self.x + xSpeed, self.y + ySpeed, obstacle[0], obstacle[1]) < self.environment.objectWidth/2 + self.radius :
				collide = True
				break

		if collide :
			self.curSpeed = 0

		else :
			self.x += xSpeed
			self.y += ySpeed
			self.loseSpeed()
