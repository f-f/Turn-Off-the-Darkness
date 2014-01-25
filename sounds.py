from imports import *

class Sounds:
	def __init__(self, game):
		self.game = game
		self.counter = 0

		#array of loaded tracks
		self.tracks = {}
		self.intro = pygame.mixer.Sound("audio/Intro.ogg")
		self.guitar = pygame.mixer.Sound("audio/Guitar.ogg")
		self.bass = pygame.mixer.Sound("audio/Bass.ogg")
		self.ambient = pygame.mixer.Sound("audio/Ambient.ogg")
		self.drums = pygame.mixer.Sound("audio/Drums.ogg")

		#sounds
		self.tick = pygame.mixer.Sound("audio/Tick.ogg")
		self.monsters = pygame.mixer.Sound("audio/Monsters.ogg")
		self.diapason = pygame.mixer.Sound("audio/Diapason.ogg")
		self.step = pygame.mixer.Sound("audio/Step.ogg")

		self.death = pygame.mixer.Sound("audio/Step.ogg")

		pygame.mixer.init(44100,-16,2, 1024) #initialize mixer

		#self.channel = {}
		#for the keys in tracks we allocate a channel, and set the flag to false
		#for key in self.tracks:
		#	self.channel[key] = {'channel':self.tracks[key].play(),'threshold':0}
		#	key.set_volume(0.0) #the volume too

		#play only the intro
		self.intro.play(-1)
		self.ambient.play(-1)
		self.bass.play(-1)
		self.guitar.play(-1)
		self.drums.play(-1)
		
		self.intro.set_volume(0.75)
		self.guitar.set_volume(0.0)
		self.ambient.set_volume(0.0)
		self.bass.set_volume(0.0)
		self.drums.set_volume(0.0)

		self.step.play(-1)
		self.monsters.play(-1)

		self.step.set_volume(0.2)
		self.monsters.set_volume(0.1)


	def update(self):
		if self.game.death:
			self.death.play()
			self.diapason.set_volume(1.0)

		if self.game.beat: 
			self.counter +=1 #add a beat

			#events: light&sound
			if self.game.lightAction:
				self.tick.play()
				self.tick.set_volume(0.5)
			if self.game.soundAction:
				self.diapason.play()
				self.diapason.set_volume(0.4)

			if self.counter >= 32: 
				self.counter = 0 #resetting the counter

				if self.intro.get_volume() > 0.0:
					self.intro.stop()

				#now we set the thresholds
				if self.game.frenzy <= F_AMB: #begins the condition cycle
					self.ambient.set_volume(0.75)	
					self.bass.set_volume(0.75)
					self.guitar.set_volume(0.75)

					self.drums.set_volume(0.0)

				elif self.game.frenzy <= F_CALM:
					self.ambient.set_volume(0.75)	
					self.bass.set_volume(0.75)
					self.guitar.set_volume(0.75)
					self.drums.set_volume(0.75)

