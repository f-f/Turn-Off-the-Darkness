from imports import *		
		
class Background(pygame.sprite.Sprite):

	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		#self.rect = self.game.get_rect()

		self.image = pygame.Surface(self.game.rect.size).convert_alpha()

		# Lista di immagini tile
		self.tiles = list()
		
		# Tutti i tiles
		# .::Fogna::.
		self.tiles.append(pygame.image.load("img/Fogna/tile_pavim_fogna.png").convert())
		self.tiles.append(pygame.image.load("img/Fogna/tile_pavim_fogna2.png").convert())
		self.tiles.append(pygame.image.load("img/Fogna/tile_pavim_fogna3.png").convert())
		self.tiles.append(pygame.image.load("img/Fogna/tile_pavim_fogna_doppio.png").convert())
		self.tiles.append(pygame.image.load("img/Fogna/tile_pavim_fogna_doppio2.png").convert())
		self.tiles.append(pygame.image.load("img/Fogna/tile_pavim_fogna_doppio3.png").convert())
		self.tiles.append(pygame.image.load("img/Fogna/tile_pavim_fogna_doppio4.png").convert())

		# .::Dungeon::.

		self.tiles.append(pygame.image.load("img/Dungeon/tile_pavim_dungeon.png").convert())
		self.tiles.append(pygame.image.load("img/Dungeon/tile_pavim_dungeon2.png").convert())
		self.tiles.append(pygame.image.load("img/Dungeon/tile_pavim_dungeon3.png").convert())
		self.tiles.append(pygame.image.load("img/Dungeon/tile_pavim_dungeon_doppio2.png").convert())
		self.tiles.append(pygame.image.load("img/Dungeon/tile_pavim_dungeon_doppio3.png").convert())
		self.tiles.append(pygame.image.load("img/Dungeon/tile_pavim_dungeon_doppio4.png").convert())

		# .::Inferno::.
		self.tiles.append(pygame.image.load("img/Inferno/tile_pavim_morte.png").convert())
		self.tiles.append(pygame.image.load("img/Inferno/tile_pavim_morte2.png").convert())
		self.tiles.append(pygame.image.load("img/Inferno/tile_pavim_morte3.png").convert())
		self.tiles.append(pygame.image.load("img/Inferno/tile_pavim_morte_doppio.png").convert())
		self.tiles.append(pygame.image.load("img/Inferno/tile_pavim_inferno_doppio2.png").convert())
		self.tiles.append(pygame.image.load("img/Inferno/tile_pavim_inferno_doppio3.png").convert())
		self.tiles.append(pygame.image.load("img/Inferno/tile_pavim_inferno_doppio4.png").convert())

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

		fren = self.game.frenzy 
		for i in xrange(0, self.game.rect.w/self.side + 1):
			
			if (fren <= F_CALM):
				random_index = random.randint(0, NUM_TILES_FOGNA - 1)
			elif (fren <= F_TRANS2):
				random_index = random.randint(NUM_TILES_FOGNA, NUM_TILES_TOT - NUM_TILES_INFERNO - 1)
			else:
				random_index = random.randint(NUM_TILES_FOGNA + NUM_TILES_DUNGEON, NUM_TILES_TOT - 1)
			
			row.blit(self.tiles[random_index], (position, 0))
			position += self.tiles[random_index].get_rect().w

		return row

	def update(self):
		self.offset += self.game.tick * self.game.speed/4
		if (self.offset > self.side):
			self.offset = 0
			del self.rows[-1]
			self.rows.insert(0, self.new_row())
		for i in xrange(len(self.rows)):
			self.image.blit(self.rows[i], (0, i * self.side + self.offset))

		self.image.blit(self.rows[-1], (0, -self.side + self.offset))
