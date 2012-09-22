#!/usr/bin/env python

import pygame
from data import frame1
from data import frame2
from data import frame3
from data import frame4
from data import frame5
from data import frame6

class Nyancat:
	#Pixel wide for the original image.
	_PIXEL_WIDE = 35
	
	#Pixel high for the original image.
	_PIXEL_HIGH = 25
	
	_WHITE = pygame.Color(255, 255, 255)	#FFFFFF
	_BLACK = pygame.Color(0, 0, 0)			#000000
	_GRAY = pygame.Color(153, 153, 153)	#999999
	_PINK1 = pygame.Color(255, 204, 153)	#FFCC99
	_PINK2 = pygame.Color(255, 153, 255)	#FF99FF
	_PINK3 = pygame.Color(255, 51, 153)	#FF3399
	_PINK4 = pygame.Color(255, 153, 153)	#FF9999
	
	def __init__(self, rect=pygame.Rect(0, 0, _PIXEL_WIDE, _PIXEL_HIGH)):
		self._rect = rect
		self._imageWidth = 0.0
		self._imageHeight = 0.0
		self._frames = []
		self._currentFrame = 0
		
		self._configureImageSize()
		self._configureFrames()
	
	#Calculate the maximum image size in a given rectangle area without breaking the image's aspect ratio.
	def _configureImageSize(self):
		w = self._rect.width
		h = self._rect.height
		
		if (w <= h):
			self._imageWidth = w
			self._imageHeight = w * self.__class__._PIXEL_HIGH / float(self.__class__._PIXEL_WIDE)
		else:
			self._imageWidth = h * self.__class__._PIXEL_WIDE / float(self.__class__._PIXEL_HIGH)
			self._imageHeight = h
			
		self._imageWidth = float(self._imageWidth)
		self._imageHeight = float(self._imageHeight)
		
		#Make sure the image size is always smaller than the rectangle.
		if self._imageWidth > self._rect.width or self._imageHeight > self._rect.height:
			raise ArithmeticError
	
	#Setup pixels' data.
	def _configureFrames(self):
				self._frames = (
					frame1.pixeldata,
					frame2.pixeldata,
					frame3.pixeldata,
					frame4.pixeldata,
					frame5.pixeldata,
					frame6.pixeldata)		
	
	#Set the next animation frame.
	def update(self):
		self._currentFrame += 1

		if (self._currentFrame > len(self._frames) - 1):
			self._currentFrame = 0
	
	#Draw pixel data on the surface.
	def draw(self, surface):
		self._draw(surface, self._frames[self._currentFrame][0], self.__class__._WHITE)
		self._draw(surface, self._frames[self._currentFrame][1], self.__class__._BLACK)
		self._draw(surface, self._frames[self._currentFrame][2], self.__class__._GRAY)
		self._draw(surface, self._frames[self._currentFrame][3], self.__class__._PINK1)
		self._draw(surface, self._frames[self._currentFrame][4], self.__class__._PINK2)
		self._draw(surface, self._frames[self._currentFrame][5], self.__class__._PINK3)
		self._draw(surface, self._frames[self._currentFrame][6], self.__class__._PINK4)
		
	#Fill rectangles with a given color.
	def _draw(self, surface, indices, color):
			offsetX = self._rect.left;
			offsetY = self._rect.top;
			dx = self._imageWidth / float(self.__class__._PIXEL_WIDE)
			dy = self._imageHeight / float(self.__class__._PIXEL_HIGH)
			
			for index in indices:
				#No stroke by default.
				stroke = 0
				
				x = round(offsetX + index[0] * dx)
				y = round(offsetY + index[1] * dy)
				w = round(dx)
				h = round(dy)
				
				#If the rect is too small to be filled, stroke it.
				if w <= 1 or h <= 1:
					stroke = 1
					
				rect = pygame.Rect(int(x), int(y), int(w), int(h))
				pygame.draw.rect(surface, color, rect, stroke)
	
def test1():
	Nyancat(pygame.Rect(0, 0, 200, 100))
	Nyancat(pygame.Rect(0, 0, 100, 10))
	Nyancat(pygame.Rect(0, 0, 100, 100))
	Nyancat(pygame.Rect(0, 0, 10, 100))
	Nyancat()

if __name__ == "__main__":
	test1()
	