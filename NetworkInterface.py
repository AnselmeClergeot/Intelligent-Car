#coding: utf-8

from neural_network.Neural_Network import *
import pygame
from pygame.locals import *

class NetworkInterface :

	def __init__(self, car) :

		self.car = car
		self.NN = Neural_Network(car.sensorsNb, 50, 3)
		self.trainingSet = []

	def learnExample(self) :
		self.NN.backward(self.getInputs(), self.getOutputs(), 0.2)

	def getPrediction(self) :
		return self.NN.forward(self.getInputs())

	def getInputs(self) :
		inputs = []
	
		for ray in self.car.sensors :
		 	inputs.append(1 - (ray.length/ray.maxLength))

		return inputs

	def getOutputs(self) :
		outputs = [0] * 3

		keys = pygame.key.get_pressed()
	
		if keys[K_LEFT] :
			outputs[0] = 1
		if keys[K_RIGHT] :
			outputs[1] = 1
		if keys[K_UP] :
			outputs[2] = 1

		return outputs

