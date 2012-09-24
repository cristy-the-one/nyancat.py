#!/usr/bin/env python

import sys
import pygame

class Rainbow:
	#Scalers used for calculating the size of the rainbow rectangles according to the cat image size.
	_SCALER_X = 7
	_SCALER_Y = 2
	
	#Rainbow colors
	_RED 	= pygame.Color(255, 0, 0) 		#FF0000
	_ORANGE = pygame.Color(255, 153, 0) 	#FF9900
	_YELLOW = pygame.Color(255, 255, 0)	#FFFF00
	_GREEN	= pygame.Color(51, 255, 0)		#33FF00
	_BLUE	= pygame.Color(0, 153, 255)		#0099FF
	_PURPLE	= pygame.Color(102, 51, 255)	#6633FF
	
	def __init__(self, catRect, pixelSize):
		#Rectangle area of the cat image, not the rainbow!!
		self._catRect = catRect
					
		#Rectangle width of each rainbow component (i.e., red rectangle, orange rectangle, etc.)
		self._tileWidth = self.__class__._SCALER_X * pixelSize[0]
					
		#Rectangle height of each rainbow component
		self._tileHeight = self.__class__._SCALER_Y * pixelSize[1]
					
		#Store the toggled animation state.
		self._animationToggled = False
	
	#Update properties according to the status of the cat image.
	def update(self):
		self._animationToggled = not self._animationToggled
	
	#Draw rainbows according to the status of the cat image.
	def draw(self, surface):
		#Setup initial state.
		x = self._catRect.left
		y = self._catRect.top + 2 * self._tileHeight
		direction = 1
		
		if self._animationToggled:
			y = self._catRect.top + 3 * self._tileHeight
			direction =-1
		
		count = 0
		
		#Draw rainbow rectangles until far enough from the surface bounds. 
		while x > -0.5 * surface.get_rect().width:
			self._draw(surface, (x, y))
			x -= self._tileWidth
			y += 0.5 * self._tileHeight * direction
			count += 1
			
			if count >= 3:
				count = 0
				direction *= -1
	
	#Private method. Draw a set of rainbow components (i.e., red, orange, ..., purple).
	def _draw(self, surface, origins):
		x = int(round(origins[0]))
		y = int(round(origins[1]))
		w = int(round(self._tileWidth))
		h = int(round(self._tileHeight))
		
		#No stroke by default (i.e., fill the rectangle).
		stroke = 0
		
		#If the rectangle is too small to be filled, stroke it.
		if w <= 1 or h <= 1:
			stroke = 1
		
		pygame.draw.rect(surface, self.__class__._RED, pygame.Rect(x, y, w, h), stroke)
		pygame.draw.rect(surface, self.__class__._ORANGE, pygame.Rect(x, y + h, w, h), stroke)
		pygame.draw.rect(surface, self.__class__._YELLOW, pygame.Rect(x, y + 2 * h, w, h), stroke)
		pygame.draw.rect(surface, self.__class__._GREEN, pygame.Rect(x, y + 3 * h, w, h), stroke)
		pygame.draw.rect(surface, self.__class__._BLUE, pygame.Rect(x, y + 4 * h, w, h), stroke)
		pygame.draw.rect(surface, self.__class__._PURPLE, pygame.Rect(x, y + 5 * h, w, h), stroke)
		

if __name__ == "__main__":
	pygame.init()
	DISPLAY_SURFACE = pygame.display.set_mode((320, 240))
	BACKGROUND_COLOR = pygame.Color(15, 77, 143)
	DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
	FPS = 4
	CLOCK = pygame.time.Clock()
	
	#Create a rainbow object.
	rainbow = Rainbow(pygame.Rect(320, 90, 70, 50), (3, 3))
	
	#count = 0
	
	while True:
		DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
			
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
					
		#Draw the rainbow.
		rainbow.draw(DISPLAY_SURFACE)	
		
		#Update the state of the rainbow.
		rainbow.update()
		
		#pygame.image.save(DISPLAY_SURFACE, "rainbow_animation_" + str(count) + ".png")
		#count += 1
					
		pygame.display.update()
		CLOCK.tick(FPS)