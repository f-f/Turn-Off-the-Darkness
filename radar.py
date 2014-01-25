from imports import *

class Radar(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image = pygame.image.load('img/Radar/radar_unico.png').convert_alpha()
		self.rect = self.image.get_rect()
		
		self.rect.center = self.game.player.rect.center
		
		#
		self.image.fill(0)
		#
	
	def update(self):
		None
