from imports import *
from random import randint

class Background(pygame.sprite.Sprite):

	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game

		self.image = pygame.Surface(self.game.rect.size).convert_alpha()
		self.rect = self.image.get_rect()

		num_tiles = 4
		num_tiles_single = 3

		self.tile = list()
		# for i in (0, self.num_tiles - 1):
		self.tile.append(pygame.image.load("img/tile_pavim_fogna1.png").convert())
		self.tile_rect = self.tile[0].get_rect()

		self.tile.append(pygame.image.load("img/tile_pavim_fogna2.png").convert())
		self.tile.append(pygame.image.load("img/tile_pavim_fogna3.png").convert())

		# Tile doppi:
		# self.tile.append(pygame.image.load("img/tile_pavim_fogna_doppio.png").convert())
		# self.tile_rect_double = self.tile[3].get_rect()

		for x in range(0, self.game.rect.w , self.tile_rect.w):
			for y in range(0, self.game.rect.h, self.tile_rect.h):
					
					random_index = randint(0, num_tiles_single - 1)	# Per ora sono tile singoli.
					self.image.blit( self.tile[random_index], (x,y) )

	def update(self):
		None