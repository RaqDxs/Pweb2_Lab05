from chessPictures import *
from interpreter import draw


torre = Picture(ROCK)

torrehorizontal= torre.horizontalMirror()

tablero = torre.join(torrehorizontal)

draw(tablero)

