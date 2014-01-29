from imports import *		

class Background(pygame.sprite.Sprite):

	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game

		self.image = pygame.Surface(self.game.rect.size).convert_alpha()
		self.side = UNIT * 2
		self.offset = 0

		self.tiles_fogna = self.create_tilelist("Fogna")
		self.tiles_dungeon = self.create_tilelist("Dungeon")		
		self.tiles_inferno = self.create_tilelist("Inferno")
		
		self.rows = list() # Lista di righe dello schermo
		for i in xrange(0, self.game.rect.h/self.side + 1):
			self.rows.append(self.new_row())
		
		self.black = False

	def create_tilelist(self, livello):
	# Ritorna una lista di tiles (pygame.image) caricati
		self.tiles = list()
		for i in xrange(0, 2):
			self.tiles.append(pygame.image.load(tools.get_pathname(livello, "Pavimento", i)).convert())
			self.tiles.append(pygame.image.load(tools.get_pathname(livello, "Pav", i)).convert())			
		self.tiles.append(pygame.image.load(tools.get_pathname(livello, "Pav", 3)).convert())
		return self.tiles

	def new_row(self):
	# Definisce una riga dello schermo con tiles random in base al livello e la ritorna
		self.row = pygame.Surface((self.game.rect.w, self.side)).convert_alpha()
		self.position = -self.side/2 + random.randint(-self.side/2 + 10, self.side/2 - 10)
		fr = self.game.frenzy
		
		for i in xrange(0, self.game.rect.w/self.side + 1):
			
			random_index = random.randint(0, 4);
			if (fr <= F_CALM):
				self.row.blit(self.tiles_fogna[random_index], (self.position, 0))
				self.position += self.tiles_fogna[random_index].get_rect().w
			elif (fr <= F_TRANS2):
				self.row.blit(self.tiles_dungeon[random_index], (self.position, 0))
				self.position += self.tiles_dungeon[random_index].get_rect().w
			else:
				self.row.blit(self.tiles_inferno[random_index], (self.position, 0))
				self.position += self.tiles_inferno[random_index].get_rect().w	
			
		return self.row

	def update(self):
		if self.black:
			self.image.fill((0,0,0))
		else:
			self.image.fill(0)
			self.offset += self.game.tick * self.game.speed
			if (self.offset > self.side):
				self.offset = 0
				del self.rows[-1]
				self.rows.insert(0, self.new_row())
				
			for i in xrange(len(self.rows)):
				self.image.blit(self.rows[i], (0, i * self.side + self.offset))

			self.image.blit(self.rows[-1], (0, -self.side + self.offset))
