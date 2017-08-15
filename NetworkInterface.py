#coding: utf-8

from neural_network.Neural_Network import *
import pygame
from pygame.locals import *

class NetworkInterface :
	def __init__(self, car) :
		self.car = car
		self.NN = Neural_Network(car.sensorsNb, 10, 4)

	def learn(self) :
	
		inputs = self.getInputs()

		outputs = [0] * 4

		keys = pygame.key.get_pressed()
	
		if keys[K_LEFT] :
			outputs[0] = 1
		if keys[K_RIGHT] :
			outputs[1] = 1
		if keys[K_UP] :
			outputs[2] = 1
		if keys[K_DOWN] :
			outputs[3] = 1

		for i in range(100) :
			self.NN.backward(inputs, outputs, 0.2)

	def getPrediction(self) :
		return self.NN.forward(self.getInputs())

	def getInputs(self) :
		inputs = []
	
		for ray in self.car.sensors :
			inputs.append(ray.length/ray.maxLength)
		
		return inputs
