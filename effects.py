from imports import *

class Black(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
	
		self.image = pygame.Surface(self.game.rect.size).convert_alpha()
		self.image.fill((0,0,0))
		
		self.rect = self.image.get_rect()
		
	
	def update(self):
		if self.game.lightTimer > 0 or self.game.soundTimer > 0: 
			self.image.fill(0)
		if self.game.lightTimer <= 0 and self.game.soundTimer <= 0:
			self.image.fill((0,0,0))


class Light(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image_loaded = pygame.image.load('img/Raggio_luce/Luce.png').convert_alpha()
		self.rect = self.image_loaded.get_rect()
		
		self.imageEmpty = pygame.Surface(self.rect.size).convert_alpha()
		self.imageEmpty.fill(0)

		self.image = self.imageEmpty		
		self.rect.midbottom = self.game.rect.midbottom
		
	
	def update(self):
		if self.game.beat:
			if self.game.lightTimer > 0: self.image = self.image_loaded
			else: self.image = self.imageEmpty

class Radar(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image_loaded = pygame.image.load('img/Radar/radar_unico_2.png').convert_alpha()
		self.rect = self.image_loaded.get_rect()
		
		self.imageEmpty = pygame.Surface(self.rect.size).convert_alpha()
		self.imageEmpty.fill(0)

		self.image = self.imageEmpty		
		self.rect.center = self.game.player.rect.center
		
	
	def update(self):
		if self.game.beat:
			if self.game.soundTimer > 0: self.image = self.image_loaded
			else: self.image = self.imageEmpty

		
