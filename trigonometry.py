#coding: utf-8

import math

def getDirection(deg) :
	return math.cos(degToRad(deg)), math.sin(degToRad(deg))

def getDirectionBetween(startX, startY, endX, endY) :
	dist = distance(startX, startY, endX, endY)
	if dist == 0 :
		return (0, 0)

	return (endX - startX) / dist, (endY - startY) / dist

def degToRad(deg) :
	return 2 * math.pi / 360 * deg
	
def distance(xStart, yStart, xEnd, yEnd) :
	return math.sqrt(math.pow(xStart - xEnd, 2) + math.pow(yStart - yEnd, 2))

def inSquare(x, y, squareX, squareY, squareWidth) :
	return x > squareX - squareWidth/2 and x < squareX + squareWidth/2 and y > squareY - squareWidth/2 and y < squareY + squareWidth/2
