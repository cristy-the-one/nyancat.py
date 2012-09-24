#!/usr/bin/env python

import sys
import random
import pygame
from star import Star

class StarManager:
	#Default value of the horizontal velocity of a star.
	_DEFAULT_VELOCITY_X = -10
	
	def __init__(self, numStars, surface, pixelSize, velocityX=_DEFAULT_VELOCITY_X):
		#Size of pixelated rectangle for the image.
		self._pixelSize = pixelSize
		
		#Vhorizontal velocity of stars (positive right).
		self._velocityX = velocityX
		
		#Star objects to manage.
		self._stars = self._createStars(numStars, surface, pixelSize)
	
	#Return a star object.
	def _createStar(self, surface, pixelSize):
		surfRect = surface.get_rect()
		x = random.randint(surfRect.left, surfRect.width)
		y = random.randint(surfRect.top, surfRect.height)
		star = Star(pixelSize)
		star.rect.topleft = (x, y)
		return star
	
	#Return a list of newly created stars.
	def _createStars(self, numStars, surface, pixelSize):
		stars = []
					
		for i in range(numStars):
			star = self._createStar(surface, pixelSize)
			stars.append(star)
					
		return stars
	
	#Update animation frame of stars.
	def update(self, surface):
		for i in reversed(range(len(self._stars))):
			star = self._stars[i]
			star.rect.left += self._velocityX
			star.update()
			
			#If the star comes to the end of the animation remove it and add a new one.
			if star.animationFinished:
				self._stars.remove(star)
				newStar = self._createStar(surface, self._pixelSize)
				newStar.currentFrame = 0
				self._stars.append(newStar)
	
	#Draw stars on the surface object.
	def draw(self, surface):
		for star in self._stars:
			star.draw(surface)
			
if __name__ == "__main__":
	pygame.init()
	DISPLAY_SURFACE = pygame.display.set_mode((320, 240))
	BACKGROUND_COLOR = pygame.Color(15, 77, 143)
	DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
	FPS = 12
	CLOCK = pygame.time.Clock()
	
	#Create a star manager object.
	starManager = StarManager(10, DISPLAY_SURFACE, (3, 3), -10)	
	while True:
		DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
				
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		#Draw stars.
		starManager.draw(DISPLAY_SURFACE)
		
		#Update the state of the stars.
		starManager.update(DISPLAY_SURFACE)

		pygame.display.update()
		CLOCK.tick(FPS)