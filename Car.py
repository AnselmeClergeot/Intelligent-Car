#coding: utf-8

import pygame
from trigonometry import *
from Raycast import *

class Car :
	
	def __init__(self) :
		
		self.x, self.y = 400, 350
		self.radius = 10
		self.angle = 0
		self.turnSpeed = 1.5
		self.curSpeed = 0
		self.acceleration = 0.2
		self.deceleration = 0.1
		self.speedLoss = 0.05
		self.maxSpeed = 5

		self.ray1 = Raycast(self, -30)
		self.ray2 = Raycast(self, 0)
		self.ray3 = Raycast(self, 30)

	def draw(self, window) :
		pygame.draw.circle(window, pygame.Color("white"), (int(self.x), int(self.y)), self.radius)
		
		self.ray1.draw(window)
		self.ray2.draw(window)
		self.ray3.draw(window)

	def turn(self, direction) :
		
		epsilon = 0.1

		if math.fabs(self.curSpeed) < epsilon :
			return

		if self.curSpeed == 0 :
			return

		if direction == "left" :
			self.angle -= self.turnSpeed
		else :
			self.angle += self.turnSpeed

		self.angle %= 360

	def accelerate(self) :
		self.curSpeed += self.acceleration
		self.checkSpeed()

	def decelerate(self) :
		self.curSpeed -= self.deceleration
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

		self.curSpeed += zeroSpeedDir * self.speedLoss

	def update(self) :
		self.x += getDirection(self.angle)[0] * self.curSpeed
		self.y += getDirection(self.angle)[1] * self.curSpeed

		self.loseSpeed()
