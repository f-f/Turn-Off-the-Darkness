from imports import *

from player import *
from wall import *

from background import *

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
		self.speed = 4*UNIT  # per second
		
		# se usati insieme permettono di muovere il mouse infinitamente
		# ma bloccano la tastiera "all'esterno"
		#pygame.mouse.set_visible(False)
		#pygame.event.set_grab(True)
		
		# game.state_varible
		pygame.time.set_timer(USEREVENT, int(60*1000/BPM))
		self.beat = False
		#self.sounds = Sounds(self)
		
		self.left = False
		self.right = False
		#
		
		
		self.image = pygame.display.set_mode(
			(800,600),DOUBLEBUF
			#(1366,768),DOUBLEBUF|FULLSCREEN|HWSURFACE
		)
		self.rect = self.image.get_rect()
		pygame.display.set_caption('GGJ')
		
		self.foreground = pygame.sprite.Group()
		
		self.player = Player(self)
		self.foreground.add(self.player)

		self.background = Background(self)
		
		self.test_wall = Wall(self)
		self.foreground.add(self.test_wall)
		
		
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
				if event.key == K_LEFT:
					self.left = True
				if event.key == K_RIGHT:
					self.right = True
				
				
			elif event.type == KEYUP:
				if event.key == K_LEFT:
					self.left = False
				if event.key == K_RIGHT:
					self.right = False
			
			if event.type==USEREVENT:
				self.beat = True
			
		
		self.mouse_rel = pygame.mouse.get_rel()
	
	def update(self):
		#self.sounds.update()
		
		self.background.update()
		self.foreground.update()
		
		self.beat = False
		
	def draw(self):
		self.image.fill(0)
		
		self.image.blit( self.background.image, (0,0) )
		self.foreground.draw(self.image)
		
		
		fps = pygame.font.SysFont(
				"monospace", 24
			).render(
				str(int(self.clock.get_fps()))+"fps",
				True, (100,100,100)
			)
		
		self.image.blit(
			fps,
			(
				self.rect.w-fps.get_width(),
				self.rect.h-fps.get_height()
			)
		)
		
		pygame.display.update()
		#pygame.display.flip()


def main():
	print "GGJ"
	Game().run()

if __name__=="__main__":
	main()
