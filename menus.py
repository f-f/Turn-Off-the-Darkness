from imports import *

class Bar(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image_loaded = pygame.image.load('img/Menu/Barra_tools_trasp.png').convert_alpha()
		self.rect = self.image_loaded.get_rect()
		
		self.imageEmpty = pygame.Surface(self.rect.size).convert_alpha()
		self.image = self.imageEmpty

		self.rect.topleft = self.game.rect.topleft

		self.image.fill(0)
		self.image.blit(self.image_loaded,(0,0))

	
	def update(self):
		None

class LifeBar(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image_loaded = pygame.image.load('img/Menu/vita.png').convert_alpha()
		self.rect = self.image_loaded.get_rect()
		self.rect.w *= self.game.lives
		
		self.imageEmpty = pygame.Surface(self.rect.size).convert_alpha()

		self.image = self.imageEmpty

		self.rect.topleft = self.game.rect.topleft
		self.rect.left += 130
		self.rect.top += 35

		self.image.fill(0)
		for i in xrange(0,self.game.lives):
			self.image.blit(self.image_loaded,(i*self.image_loaded.get_rect().w,0))
		
	
	def update(self):
		self.image.fill(0)
		for i in xrange(0,self.game.lives):
			self.image.blit(self.image_loaded,(i*self.image_loaded.get_rect().w,0))

class FrenzyNegBar(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image_loaded = pygame.image.load('img/Menu/fren_vuoto_grigio.png').convert_alpha()

		self.image = pygame.Surface(((self.image_loaded.get_rect().w +3)*10, self.image_loaded.get_rect().h)).convert_alpha()
		self.rect = self.image.get_rect()

		self.rect.topright = self.game.rect.topright
		self.rect.right -= 516
		self.rect.top += 52

		self.update()		
	
	def update(self):
		if self.game.beat:
			self.negfrenzy = 10-self.game.frenzy

			self.image.fill(0)
			for i in xrange(0,self.negfrenzy):
				self.image.blit(self.image_loaded,(self.rect.w -i*(self.image_loaded.get_rect().w + 3),0))


class Points(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		

		self.font = pygame.font.SysFont("monospace", 24)

		self.update()
		
	
	def update(self):
		self.image = self.font.render(
			str(self.game.points),
			True, (255,255,255)
		)
		self.rect = self.image.get_rect()

		self.rect.topright = self.game.rect.topright
		self.rect.right -= 60
		self.rect.top += 35

class LevelComp(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.font = pygame.font.SysFont("monospace", 24)

		self.update()
		
	
	def update(self):
		self.image = self.font.render(
			str(self.game.levelCompletion) + "%",
			True, (255,255,255)
		)
		self.rect = self.image.get_rect()

		self.rect.topright = self.game.rect.topright
		self.rect.right -= 200
		self.rect.top += 35

