def get_pathname(livello, tipo, sufx = 1):
	if (tipo != "Muro"):
		return "img/%s/%s_%s.png" % (livello, tipo, sufx + 1)
	else:
		return "img/%s/%s_%s.png" % (livello, tipo, sufx)

def create_tilelist(livello):
	tiles = list()
	for i in xrange(1, 3):
		tiles.append(pygame.image.load(tools.get_pathname(livello, "Pav", i)).convert())
		tiles.append(pygame.image.load(tools.get_pathname(livello, "Pavimento", i)).convert())
	tiles.append(pygame.image.load(tools.get_pathname(livello, "Pavimento", 4)).convert())
	return tiles