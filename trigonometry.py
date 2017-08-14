#coding: utf-8

import math

def getDirection(deg) :
	return math.cos(degToRad(deg)), math.sin(degToRad(deg))

def degToRad(deg) :
	return 2 * math.pi / 360 * deg
	
def distance(xStart, yStart, xEnd, yEnd) :
	return math.sqrt(math.pow(xStart - xEnd, 2) + math.pow(yStart - yEnd, 2))
