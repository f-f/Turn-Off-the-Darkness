from imports import *

class Walls(pygame.sprite.Group):
	def __init__(self, game):
		pygame.sprite.Group.__init__(self)
		self.game = game
		
		self.beat_counter = 0
		
		self.last_angle = random.uniform(-math.pi,+math.pi)
	
	def update(self):
		if self.game.beat:
			self.beat_counter += 1
		
		if self.beat_counter >= 2:
			self.beat_counter = 0
			#angle = random.uniform(-math.pi,+math.pi)  # migliore finora
			angle = self.last_angle + random.uniform(-math.pi/4,+math.pi/4)
			w = Wall(
					self.game,
					random.randint(30,50),
					angle
				)
			self.last_angle += w.n*w.step
			self.add(w)
		
		#for w in self:
		#	w.rect.y += self.game.tick*self.game.speed
		pygame.sprite.Group.update(self)

class Wall(pygame.sprite.Sprite):
	def __init__(self, game, n, angle):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.n = n
		
		self.radius = WALL_INNER_RADIUS
		self.outer_radius = self.radius + UNIT
		self.step = 2*math.asin(float(UNIT)/(2*self.outer_radius))  # angle between tiles
		
		angle = math.fmod(angle, 2*math.pi)
		self.angle = angle # + self.n*self.step/2  # angolo centrale
		
		self.image = pygame.Surface(
			(self.outer_radius*2,
			self.outer_radius*2)
		).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (self.game.rect.centerx, self.game.rect.w/2)
		
		self.tiles = pygame.sprite.Group()
		
		for i in xrange(0,self.n):
			tile = Tile(
					game, self, self.angle + i*self.step
				)
			self.tiles.add(tile)
		
	
	def set_angle(self, angle):
		delta = angle - self.angle
		for tile in self.tiles:
			tile.angle += delta
		
		self.angle = angle
	
	def update(self):
		if self.game.left:
			self.set_angle(self.angle - 5*self.game.tick*self.game.speed*self.step/UNIT)
		if self.game.right:
			self.set_angle(self.angle + 5*self.game.tick*self.game.speed*self.step/UNIT)
		self.tiles.update()
		
		self.rect.y += self.game.tick*self.game.speed
		
		self.image.fill(0)
		self.tiles.draw(self.image)
		
		if self.rect.top > self.game.rect.w:
			for t in self.tiles:
				t.kill()
				del t
			self.kill()
			del self
		
class Tile(pygame.sprite.Sprite):
	def __init__(self, game, wall, angle):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.wall = wall
		self.angle = angle
		
		# load png
		#self.image_start = pygame.Surface((UNIT,UNIT)).convert_alpha()
		#self.image_start.fill((0,255,255))
		self.image_start = pygame.image.load('img/test_tile01.png').convert_alpha()
		#
		self.update()
		
	def update(self):
		self.image = pygame.transform.rotate(self.image_start, -180.0*self.angle/math.pi+90)
		#self.image = self.image_start
		self.rect = self.image.get_rect()
		
		#self.rect.centerx = self.wall.rect.centerx
		#self.rect.centery = self.wall.rect.centery
		
		r = (self.wall.radius+self.wall.outer_radius)/2
		self.rect.center = (
			self.wall.rect.w/2 + r*math.cos(self.angle),
			self.wall.rect.h/2 + r*math.sin(self.angle)
		)
		
		if self.rect.top > self.game.rect.w:
			self.kill()
			del self
		
