from imports import *

class Light(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image = pygame.image.load('img/Raggio_luce/Raggio_luce.png').convert_alpha()
		self.rect = self.image.get_rect()
		
		self.rect.midbottom = self.game.rect.midbottom
		self.rect.y -= 2*UNIT
		
		#
		self.image.fill(0)
		#
	
	def update(self):
		None
