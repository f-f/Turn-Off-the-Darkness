from imports import *
from random import randint		
		
class Background(pygame.sprite.Sprite):

	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		#self.rect = self.game.get_rect()

		self.image = pygame.Surface(self.game.rect.size).convert_alpha()

		# Numero dei file tipo tile
		self.num_tiles = 4
		self.num_tiles_single = 3

		# Lista di immagini tile
		self.tiles = list()
		
		self.tiles.append(pygame.image.load("img/tile_pavim_fogna1.png").convert())
		self.tiles.append(pygame.image.load("img/tile_pavim_fogna2.png").convert())
		self.tiles.append(pygame.image.load("img/tile_pavim_fogna3.png").convert())

		# Tile doppi:
		self.tiles.append(pygame.image.load("img/tile_pavim_fogna_doppio.png").convert())

		# rect di tile
		self.side = self.tiles[0].get_rect().h

		# offeset per aggiungere rows
		self.offset = 0

		# Lista di rows
		self.rows = list()
		for i in xrange(0, self.game.rect.h/self.side + 1):
			self.rows.append(self.new_row())

	# Metodo che crea rows secondo un indice random per i tiles
	def new_row(self):
		row = pygame.Surface((self.game.rect.w, self.side)).convert_alpha()
		# row.fill((0, 0, 255))
		position = -self.side/2
		for i in xrange(0, self.game.rect.w/self.side + 1):
			random_index = randint(0, self.num_tiles - 1)
			row.blit(self.tiles[random_index], (position, 0))
			position += self.tiles[random_index].get_rect().w

		return row

	def update(self):
		self.offset += self.game.tick * self.game.speed
		if (self.offset > self.side):
			self.offset = 0
			del self.rows[-1]
			self.rows.insert(0, self.new_row())
		for i in xrange(len(self.rows)):
			self.image.blit(self.rows[i], (0, i * self.side + self.offset))

		self.image.blit(self.rows[-1], (0, -self.side + self.offset))