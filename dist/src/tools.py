LEVELS = ["Fogna","Dungeon","Inferno",]
N_TILES = [1,1,5]

def get_pathname(livello, tipo, sufx = 1):
	if (tipo != "Muro"):
		return "img/Tile/%s/%s_%s.png" % (livello, tipo, sufx)
	else:
		return "img/Tile/%s/%s_%s.png" % (livello, tipo, sufx)

def create_tilelist(livello):
	tiles = list()
	for i in xrange(1, 3):
		tiles.append(pygame.image.load(tools.get_pathname(livello, "Pav", i)).convert())
		tiles.append(pygame.image.load(tools.get_pathname(livello, "Pavimento", i)).convert())
	tiles.append(pygame.image.load(tools.get_pathname(livello, "Pavimento", 4)).convert())
	return tiles


import os,sys, pygame

def OS_PATH(path):
	path = os.path.dirname(os.path.realpath(__file__)) + os.sep + path
	return os.path.normpath(path)

pygame_image_load = pygame.image.load
def load_image(path):
	return pygame_image_load(OS_PATH(path))
#pygame.image.load = load_image

pygame_mixer_Sound = pygame.mixer.Sound
def load_sound(path):
	return pygame_mixer_Sound(OS_PATH(path))
#pygame.mixer.Sound = load_sound
