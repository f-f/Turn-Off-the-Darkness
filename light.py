from imports import *

class Light(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image_loaded = pygame.image.load('img/Raggio_luce/Raggio_luce.png').convert_alpha()
		self.rect = self.image_loaded.get_rect()
		
		self.image = pygame.Surface(self.rect.size).convert_alpha()
		self.image.fill(0)
		
		self.rect.midbottom = self.game.rect.midbottom
		self.rect.y -= 2*UNIT
		
	
	def update(self):
		self.image = self.image_loaded
		None
		
