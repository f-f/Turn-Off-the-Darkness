from imports import *

class Player(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image = pygame.Surface((UNIT,2*UNIT)).convert_alpha()
		self.rect = self.image.get_rect()
		
		self.rect.centerx = int(self.game.rect.w*PLAYER_REL_POS[0])
		self.rect.centery = int(self.game.rect.h*PLAYER_REL_POS[1])
		
		#
		self.image.fill((255,255,255))
		#
