from imports import *

from player import *

class Game(pygame.sprite.Sprite):
	def __init__(self):
		# se funziona si tiene
		pygame.sprite.Sprite.__init__(self)
		#
		
		self.quit = False
		
		pygame.init()
		
		self.clock = pygame.time.Clock()
		self.max_fps = 120
		self.tick = 0
		
		# se usati insieme permettono di muovere il mouse infinitamente
		#pygame.mouse.set_visible(False)
		#pygame.event.set_grab(True)
		
		self.image = pygame.display.set_mode(
			(800,600),DOUBLEBUF
			#(1366,768),DOUBLEBUF|FULLSCREEN|HWSURFACE
		)
		self.rect = self.image.get_rect()
		pygame.display.set_caption('GGJ')
		
		self.background = pygame.sprite.Group()
		self.foreground = pygame.sprite.Group()
		
		self.player = Player(self)
		self.foreground.add(self.player)
	
	def run(self):
		while not self.quit:
			self.events()
			self.update()
			self.draw()
			self.tick = float(self.clock.tick(self.max_fps))/1000
		pygame.quit()
	
	def events(self):
		for event in pygame.event.get():
			if event.type==QUIT:
				self.quit = True
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.quit = True
			
		
		self.mouse_rel = pygame.mouse.get_rel()
	
	def update(self):
		self.background.update()
		self.foreground.update()
		
	def draw(self):
		self.background.draw(self.image)
		self.foreground.draw(self.image)
		
		pygame.display.update()
		#pygame.display.flip()


def main():
	print "GGJ"
	Game().run()

if __name__=="__main__":
	main()
