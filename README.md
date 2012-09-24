# nyancat.py

Scalable Nyan Cat animation written in Python from scratch. [pygame](http://www.pygame.org/) required.

![Nyan Cat](/borealkiss/nyancat.py/raw/master/example.gif)

![Nyan Cat](/borealkiss/nyancat.py/raw/master/cat.gif)
	
![Nyan Cat](/borealkiss/nyancat.py/raw/master/rainbow.gif)
	
![Nyan Cat](/borealkiss/nyancat.py/raw/master/stars.gif)

## Example

The simplest implementation is here (note that half of the code is boilerplate for pygame):

	import pygame
	from nyancat import Nyancat
	from rainbow import Rainbow
	from star_manager import StarManager

	pygame.init()
	DISPLAY_SURFACE = pygame.display.set_mode((320, 240))
	BACKGROUND_COLOR = pygame.Color(15, 77, 143)
	DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
	FPS = 12
	CLOCK = pygame.time.Clock()
	
	#Create objects.
	cat = Nyancat(pygame.Rect(110, 90, 100, 250))
	rainbow = Rainbow(cat.rect, cat.pixelSize)
	stars = StarManager(10, DISPLAY_SURFACE, cat.pixelSize)

	while True:
		DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
		
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		#Draw the objects. 
		rainbow.draw(DISPLAY_SURFACE)
		cat.draw(DISPLAY_SURFACE)
		stars.draw(DISPLAY_SURFACE)
		
		#Update the animation state of the objects.
		cat.update()
		stars.update(DISPLAY_SURFACE)
		
		if cat.initialState:
			rainbow.update()
		
		pygame.display.update()
		CLOCK.tick(FPS)

## License

The source code itself is provided under the terms of the [MIT License](http://www.opensource.org/licenses/mit-license.php). However licensing is subject to change in the future version. For the usage of the character, visit [http://nyan.cat/](http://nyan.cat/).

## Contact

* [http://blog.boreal-kiss.net/](http://blog.boreal-kiss.net/)
* [http://twitter.com/borealkiss](http://twitter.com/borealkiss)