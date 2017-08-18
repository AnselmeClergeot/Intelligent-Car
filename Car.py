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
		self.acceleration = 0.001
		self.sensorsNb = 31
		self.visionAngle = 180
		self.curSpeed = 0
		self.maxSpeed = 0.3
		self.speedLoss = 0.0005
		self.learning = False

		self.environment = environment

		self.sensors = []

		self.lastFrame = 0
		self.elapsed = 0

		for i in range(self.sensorsNb) :
			self.sensors.append(Raycast(self, (i - self.sensorsNb/2) * (self.visionAngle / (self.sensorsNb - 1))))
		
		self.ia = IADriver(self)

	def setLearning(self, learning) :
		self.learning = learning	

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

	def update(self) :
		
		self.elapsed = pygame.time.get_ticks() - self.lastFrame
		self.lastFrame = pygame.time.get_ticks()

		xDir = self.curSpeed * getDirection(self.angle)[0] * self.elapsed
		yDir = self.curSpeed * getDirection(self.angle)[1] * self.elapsed

		self.curSpeed -= self.speedLoss * self.elapsed

		if self.curSpeed < 0 :
			self.curSpeed = 0

		if not(self.environment.collide(self.x + xDir, self.y + yDir)) :
			self.x += xDir
			self.y += yDir

		else :
			self.curSpeed = 0
			self.learning = False

	def learnExample(self) :
		if self.learning :
			self.ia.learnExample()
