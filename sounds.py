from imports import *

class Sounds:
	def __init__(self, game):
		self.game = game
		self.counter = 0

		#array of loaded tracks
		self.tracks = {}
		self.tracks['intro'] = pygame.mixer.Sound("audio/Intro.mp3")

		pygame.mixer.init(44100,-16,2, 1024) #initialize mixer

		self.channel = {}
		#for the keys in tracks we allocate a channel, and set the flag to false
		for key in tracks:
			self.channel[key] = {'channel':pygame.mixer.tracks[key].play(),'threshold':0}
			key.set_volume(0.0) #the volume too

		#play only the intro
		self.channel['intro'].set_volume(0.75)


	def update(self):
		if game.beat: 
			self.counter +=1 #add a beat
			if self.counter >= 32: self.counter = 0


