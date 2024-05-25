from chessPictures import *
from interpreter import draw

peon = Picture(BISHOP)
torre = Picture(ROCK)
tablero = peon.join(torre)

draw(tablero)