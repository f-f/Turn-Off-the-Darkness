from imports import *
from PIL import Image


img = Image.open("img/tile_fogna.png")
img = img.convert("RGBA")
width, height = img.size
m = 0.25
img = img.transform((width, height), Image.AFFINE, (1, m, 0, 0, 1, 0), Image.BICUBIC).transpose(Image.FLIP_LEFT_RIGHT)
#img = img.transform((width, height), Image.AFFINE, (1, m, 0, 0, 1, 0), Image.BICUBIC)
img.save("img/tile_trapez.png")