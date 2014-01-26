from imports import *

class Slide(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.imageEmpty = pygame.Surface(self.game.rect.size).convert_alpha()
		self.imageEmpty.fill(0)
		
		self.images = [
			pygame.image.load('img/Menu/menu.png').convert_alpha(),
			pygame.image.load('img/Menu/slide.png').convert_alpha(),
			]
	
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		
		#self.rect.centerx = int(self.game.rect.w/2)
		#self.rect.bottom = int(self.game.rect.h)
		
	def update(self):
		if self.game.slideCount < 2:
			self.image = self.images[self.game.slideCount]
		else:
			self.image = self.imageEmpty
				
