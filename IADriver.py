#coding: utf-8

from NetworkInterface import *

class IADriver :
	def __init__(self, car) :
		self.car = car
		self.interface = NetworkInterface(car)
		self.minDecision = 0.1
	
	def learnExample(self) :
		self.interface.learnExample()

	def driveSelf(self) :
		prediction = self.interface.getPrediction().tolist()

		for i in range(2) :
			maxAction = max(prediction)
			index = prediction.index(maxAction)

			if maxAction < self.minDecision :
				return

			if index == 0 :
				self.car.turn("left")
			elif index == 1 :
				self.car.turn("right")
			elif index == 2 :
				self.car.accelerate()

			del prediction[index]
