from imports import *		

class Background(pygame.sprite.Sprite):

	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game

		self.image = pygame.Surface(self.game.rect.size).convert_alpha()
		self.side = UNIT * 2
		self.offset = 0
		self.rows = list()
		for i in xrange(0, self.game.rect.h/self.side + 1):
			self.rows.append(self.new_row())

	def new_row(self):
		self.row = pygame.Surface((self.game.rect.w, self.side)).convert_alpha()
		self.position = -self.side/2

		fren = self.game.frenzy 
		for i in xrange(0, self.game.rect.w/self.side + 1):
			
			if (fren <= F_CALM):
				self.livello = "Fogna"
				self.returntile()
			elif (fren <= F_TRANS2):
				self.livello = "Dungeon"
				self.returntile()
			else:
				self.livello = "Inferno"
				self.returntile()
			
			self.position += self.tile.get_rect().w
		return self.row

	def load(self, folder, tipo, sufx):
		return pygame.image.load("img/%s/%s" % (folder, tipo) + "_" + "%s" % (sufx + 1) + ".png").convert()

	def returntile(self):
		if (random.randint(0,1) == 0):
			self.tile = self.load(self.livello, "Pav", random.randint(0,2))
		else:
			self.tile = self.load(self.livello, "Pavimento", random.randint(0,2))
		self.row.blit(self.tile, (self.position, 0))

	def update(self):
		self.offset += self.game.tick * self.game.speed/4
		if (self.offset > self.side):
			self.offset = 0
			del self.rows[-1]
			self.rows.insert(0, self.new_row())
		for i in xrange(len(self.rows)):
			self.image.blit(self.rows[i], (0, i * self.side + self.offset))

		self.image.blit(self.rows[-1], (0, -self.side + self.offset))