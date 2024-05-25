from chessPictures import *
from interpreter import draw

torre = Picture(ROCK)

torre_horizontal = torre.horizontalMirror()

tablero1 = torre.join(torre_horizontal)
tablero2 = tablero1.negative()


resultado = tablero1.up(tablero2)

draw(resultado)


