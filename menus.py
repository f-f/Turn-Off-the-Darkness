from imports import *

class LifeBar(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image_loaded = pygame.image.load('img/Menu/vita.png').convert_alpha()
		self.rect = self.image_loaded.get_rect()
		self.rect.w *= self.game.lives
		
		self.imageEmpty = pygame.Surface(self.rect.size).convert_alpha()
		self.imageEmpty.fill(0)

		self.image = self.imageEmpty

		self.rect.topleft = self.game.rect.topleft
		self.rect.left += 100
		self.rect.top += 50

		self.image.fill(0)
		for i in xrange(0,self.game.lives):
			self.image.blit(self.image_loaded,(i*self.image_loaded.get_rect().w,0))
		
	
	def update(self):
		if self.game.death:
			self.image.fill(0)
			for i in xrange(0,self.game.lives):
				self.image.blit(self.image_loaded,(i*self.image_loaded.get_rect().w,0))

