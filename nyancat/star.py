#!/usr/bin/env python

import pygame
import sys
import random
from data import star_frames

class Star:
	_PIXEL_WIDE = 9
	_PIXEL_HIGH = 9
	_WHITE = pygame.Color(255, 255, 255)
	
	def __init__(self, pixelSize):
		#Rectangle area of the star image.
		self._rect = pygame.Rect(0, 0, self.__class__._PIXEL_WIDE * pixelSize[0], self.__class__._PIXEL_HIGH * pixelSize[1])
			
		#Rectangle width of each star component (i.e., white dots)
		self._tileWidth = 0.0
			
		#Rectangle height of each star component (i.e., white dots)
		self._tileHight = 0.0
			
		#Animation frames.
		self._frames = star_frames.frames
			
		#Current animation frame number rondomly chosen from the list.
		self._currentFrame = random.randint(0,len(self._frames) - 1)
			
		self._configureSize()
	
	def _configureSize(self):
		self._tileWidth = self._rect.width / float(self.__class__._PIXEL_WIDE)
		self._tileHight = self._rect.height / float(self.__class__._PIXEL_HIGH)
	
	def update(self):
		self._currentFrame += 1

		if (self._currentFrame > len(self._frames) - 1):
			self._currentFrame = 0
	
	def draw(self, surface):
		offsetX = self._rect.left
		offsetY = self._rect.top
		w = round(self._tileWidth)
		h = round(self._tileHight)
		
		stroke = 0
		
		if w <= 1 or h <= 1:
			stroke = 1
		
		for pos in self._frames[self._currentFrame]:
			x = round(offsetX + self._tileWidth * pos[0])
			y = round(offsetY + self._tileHight * pos[1])
			pygame.draw.rect(surface, self.__class__._WHITE, pygame.Rect(int(x), int(y), int(w), int(h)), stroke)
			
	#Return the rectangle area.
	def rect(self):
		return self._rect
	rect = property(rect, None, None, None)
	
	#Return true if the current animation frame is in the last.
	def animationFinished(self):
		return self._currentFrame >= len(self._frames) - 1
	animationFinished = property(animationFinished)
	
	def getCurrentFrame(self):
		return self._currentFrame
		
	def setCurrentFrame(self, value):
			self._currentFrame = value
	currentFrame = property(getCurrentFrame, setCurrentFrame, None, None)

def __createStars(numStars, surface):
	stars = []
		
	for i in range(numStars):
		star = __createStar(surface)
		stars.append(star)
		
	return stars

def __createStar(surface):
	rect = surface.get_rect()
	x = random.randint(rect.left, rect.width)
	y = random.randint(rect.top, rect.height)
	star = Star((3, 3))
	star.rect.topleft = (x, y)
	return star

def __updateStars(stars, surface):
	for i in reversed(range(len(stars))):
		star = stars[i]
		star.update()
		
def __drawStars(stars, surface):
	for star in stars:
		star.draw(surface)

if __name__ == "__main__":
	pygame.init()
	DISPLAY_SURFACE = pygame.display.set_mode((320, 240))
	BACKGROUND_COLOR = pygame.Color(15, 77, 143)
	DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
	FPS = 12
	CLOCK = pygame.time.Clock()
	
	stars = __createStars(10, DISPLAY_SURFACE)
	
	while True:
		DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
					
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		__drawStars(stars, DISPLAY_SURFACE)
		__updateStars(stars, DISPLAY_SURFACE)
					
		pygame.display.update()
		CLOCK.tick(FPS)