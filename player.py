from imports import *

class Player(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		
		
		self.images = [
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_01.png').convert_alpha(),
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_02.png').convert_alpha(),
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_03.png').convert_alpha(),
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_04.png').convert_alpha(),
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_05.png').convert_alpha(),
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_06.png').convert_alpha(),
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_07.png').convert_alpha(),
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_08.png').convert_alpha(),
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_09.png').convert_alpha(),
			pygame.image.load('img/Walkcycle/walkcycleGABlevelsdef_10.png').convert_alpha()
			]
		
		self.image = self.images[0]
		
		self.rect = self.image.get_rect()
		
		self.rect.centerx = int(self.game.rect.w*PLAYER_REL_POS[0])
		self.rect.centery = int(self.game.rect.h*PLAYER_REL_POS[1])
		
		self.wait = 0.0
		self.fps = 15.0
		self.index = 0
		
	def update(self):
		self.wait += self.game.tick
		if self.wait > 1.0/self.fps:
			self.wait = 0.0
			
			self.index = (self.index+1)%len(self.images)
			
			self.image = self.images[self.index]
		
		
	
