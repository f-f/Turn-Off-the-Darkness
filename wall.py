from imports import *

class Wall(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.radius = WALL_INNER_RADIUS
		self.outer_radius = self.radius + UNIT
		self.step = 2*math.asin(float(UNIT)/(2*self.outer_radius))  # angle between tiles
		
		self.image = pygame.Surface(
			(self.outer_radius*2,
			self.outer_radius*2)
		).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (self.game.rect.centerx,self.game.rect.h)
		
		self.tiles = pygame.sprite.Group()
		
		# variabili generate
		self.n = 40
		self.angle = 2*math.pi/3  # angolo centrale della prima tile
		#
		
		for i in xrange(0,self.n):
			self.tiles.add(Tile(
					game, self, self.angle + i*self.step
				))
		
		#self.update()
		
		
		# il disegno va in draw() ?
		#for tile in self.tiles:
		#	self.image.blit(tile.image, (0,0))
		#

	def update(self):
		self.tiles.update()
		
		self.image.fill(0)
		self.tiles.draw(self.image)
		
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
		
