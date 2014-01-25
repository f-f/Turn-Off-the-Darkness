from imports import *

class Wall(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image = pygame.Surface(self.game.rect.size).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = (0,0)
		
		self.radius = WALL_INNER_RADIUS
		self.outer_radius = self.radius + UNIT
		self.step = 2*math.asin(float(UNIT)/(2*self.outer_radius))  # angle between tiles
		
		self.tiles = pygame.sprite.Group()
		
		#
		self.image.fill(0)
		#self.image.fill((0,255,255))
		
		# variabili diverse istanza per istanza
		self.n = 40
		self.angle = 2*math.pi/3  # angolo centrale della prima tile
		#
		
		for i in xrange(0,self.n):
			self.tiles.add(Tile(
					game, self, self.angle + i*self.step
				))
		
		self.tiles.update()
		self.tiles.draw(self.image)
		# il disegno va in draw() ?
		#for tile in self.tiles:
		#	self.image.blit(tile.image, (0,0))
		#
		
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
			self.wall.rect.centerx + r*math.cos(self.angle),
			self.wall.rect.h + r*math.sin(self.angle)
		)
		
