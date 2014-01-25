from imports import *

class Sounds:
	def __init__(self, game):
		self.game = game
		self.counter = 0

		self.intro = pygame.mixer.Sound("audio/Intro.ogg")
		self.guitar = pygame.mixer.Sound("audio/Guitar.ogg")
		self.bass = pygame.mixer.Sound("audio/Bass.ogg")
		self.ambient = pygame.mixer.Sound("audio/Ambient.ogg")
		self.drums = pygame.mixer.Sound("audio/Drums.ogg")
		self.drums2 = pygame.mixer.Sound("audio/Drums2.ogg")
		self.funks = pygame.mixer.Sound("audio/Funks.ogg")
		self.dists = pygame.mixer.Sound("audio/Dists.ogg")
		self.electro = pygame.mixer.Sound("audio/Electro.ogg")

		#sounds
		self.tick = pygame.mixer.Sound("audio/Tick.ogg")
		self.monsters = pygame.mixer.Sound("audio/Monsters.ogg")
		self.diapason = pygame.mixer.Sound("audio/Diapason.ogg")
		self.step = pygame.mixer.Sound("audio/Step.ogg")

		self.death = pygame.mixer.Sound("audio/Step.ogg")

		pygame.mixer.init(44100,-16,2, 4096) #initialize mixer
		pygame.mixer.set_num_channels(16)

		#play only the intro
		self.intro.play(-1)
		self.ambient.play(-1)
		self.bass.play(-1)
		self.guitar.play(-1)
		self.drums.play(-1)
		self.drums2.play(-1)
		self.funks.play(-1)
		self.dists.play(-1)
		self.electro.play(-1)
		
		self.intro.set_volume(0.75)
		self.setVolumes(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

		self.step.play(-1)
		self.monsters.play(-1)

		self.step.set_volume(0.15)
		self.monsters.set_volume(0.1)

	def setVolumes(self,G,A,B,D1,D2,F,D,E):
		self.guitar.set_volume(G)
		self.ambient.set_volume(A)
		self.bass.set_volume(B)
		self.drums.set_volume(D1)
		self.drums2.set_volume(D2)
		self.funks.set_volume(F)
		self.dists.set_volume(D)
		self.electro.set_volume(E)


	def update(self):
		pygame.mixer.set_num_channels(16)
		if self.game.death:
			self.death.play()

		if self.game.beat: 
			self.counter +=1 #add a beat

			#events: light&sound
			if self.game.lightAction:
				self.tick.play()
				self.tick.set_volume(0.3)
			if self.game.soundAction:
				self.diapason.play()
				self.diapason.set_volume(0.3)

			if self.counter >= 32: 
				self.counter = 0 #resetting the counter

				if self.intro.get_volume() > 0.0:
					self.intro.stop()

				#now we set the thresholds
				if self.game.frenzy <= F_AMB: #begins the condition cycle
					self.setVolumes(0.75, 0.75, 0.75, 0.0, 0.0, 0.0, 0.0, 0.0)

				elif self.game.frenzy <= F_CALM:
					self.setVolumes(0.75, 0.75, 0.75, 0.75, 0.0, 0.0, 0.0, 0.0)

				elif self.game.frenzy == F_TRANS1:
					self.setVolumes(0.75, 0.75, 0.75, 0.0, 0.75, 0.0, 0.0, 0.0)

				elif self.game.frenzy == F_TRANS2:
					self.setVolumes(0.70, 0.75, 0.75, 0.0, 0.75, 0.75, 0.0, 0.0)

				elif self.game.frenzy == F_FRNZ1:
					self.setVolumes(0.6, 0.75, 0.75, 0.0, 0.75, 0.70, 0.75, 0.0)

				elif self.game.frenzy >= F_FRNZ2:
					self.setVolumes(0.5, 0.75, 0.75, 0.0, 0.75, 0.6, 0.75, 0.75)

