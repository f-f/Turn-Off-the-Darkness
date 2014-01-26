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
		
		self.rect.centerx = int(self.game.rect.w/2)
		self.rect.bottom = int(self.game.rect.h)
		
		self.wait = 0.0
		self.fps = 15.0
		self.index = 0
		self.passaggio = 0
		
	def update(self):
		self.fps = 15.0 * (self.game.speed)/(8.0*UNIT) + 0.01
		self.wait += self.game.tick
		if self.wait > 1.0/self.fps:
			self.wait = 0.0
			
			self.index = (self.index+1)%len(self.images)
			
			self.image = self.images[self.index]
		
		for w in self.game.walls:
			d = math.hypot(
					self.rect.centerx - w.rect.centerx,
					self.rect.centery - w.rect.centery
				)
			if w.radius-d<UNIT and d-w.outer_radius<UNIT:
				if (
						#math.fmod(w.angle-w.step/2,2*math.pi)-math.pi < (-math.pi/2)
						#and
						#math.fmod(w.angle+w.step/2+w.n*w.step,2*math.pi)-math.pi > (-math.pi/2)
						math.fmod(w.angle-w.step/2, 2*math.pi) < (3*math.pi/2)
						and
						math.fmod(w.angle+w.step/2+w.n*w.step,2*math.pi) > (3*math.pi/2)
					):
					self.game.death = True
					print "morto?"
					#exit(1)
				elif self.passaggio == 0:
					self.passaggio = 1
					self.game.levelCompletion += 1
			else:
				self.passaggio = 0
			
			#
			#	self.game.death = True
			#	print "distanza"
			#	exit(1)	
				
