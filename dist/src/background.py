from imports import *		

class Tile(pygame.sprite.Sprite):
	def __init__(self, game, background, (x,y), w):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.background = background
		
		if w==1:
			rand = random.randint(1,3)
			self.images = [
					pygame.image.load(tools.get_pathname("Fogna", "Pavimento", rand)).convert_alpha(),
					pygame.image.load(tools.get_pathname("Dungeon", "Pavimento", rand)).convert_alpha(),
					pygame.image.load(tools.get_pathname("Inferno", "Pavimento", rand)).convert_alpha()
				]
		elif w==2:
			rand = random.randint(1,6)
			self.images = [
					pygame.image.load(tools.get_pathname("Fogna", "Pav", rand)).convert_alpha(),
					pygame.image.load(tools.get_pathname("Dungeon", "Pav", rand)).convert_alpha(),
					pygame.image.load(tools.get_pathname("Inferno", "Pav", rand)).convert_alpha()
				]
		else:
			print "error"
		
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)
		
		self.fixed = False
	
	def update(self):
		change = False
		
		if not self.fixed:
			self.rect.top += self.game.tick * self.game.speed
			if self.rect.top >= self.background.tot_h:
				self.rect.top -= self.background.tot_h
				change = True
		
		if change or self.fixed:
			if self.game.frenzy < F_CALM:
				self.image = self.images[0]
			#elif self.game.frenzy < F_TRANS2-1:
			#	self.image = self.images[random.randint(0,1)]
			elif self.game.frenzy < F_TRANS2:
				self.image = self.images[1]
			#elif self.game.frenzy < F_TRANS2+1:
			#	self.image = self.images[random.randint(1,2)]
			else:
				self.image = self.images[2]

class Background(pygame.sprite.OrderedUpdates):
	def __init__(self, game):
		pygame.sprite.OrderedUpdates.__init__(self)
		self.game = game
		
		self.side = UNIT * 2
		#self.tot_h = (self.game.rect.h/self.side) * self.side
		self.tot_h = self.game.rect.h-(self.game.rect.h%self.side) + self.side
		
		# same old bug same horrible solution
		pos_x = -self.side/2
		for j in xrange(0, self.game.rect.w/self.side + 1):
			w = random.randint(1,2)
			tile = Tile(self.game, self, (pos_x,0), w)
			tile.fixed = True
			self.add(tile)
			pos_x += w*self.side
		#
		
		for i in xrange(0, self.game.rect.h/self.side+1):
			pos_x = -self.side/2
			for j in xrange(0, self.game.rect.w/self.side + 1):
				w = random.randint(1,2)
				tile = Tile(self.game, self, (pos_x,self.side*i), w)
				self.add(tile)
				pos_x += w*self.side
		
		
		self.black = False
	
	def update(self):
		if not self.black:
			pygame.sprite.OrderedUpdates.update(self)
	
	def draw(self, image):
		if not self.black:
			pygame.sprite.OrderedUpdates.draw(self, image)
	
