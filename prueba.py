from chessPictures import *
from interpreter import draw

torre = Picture(ROCK)

torre_horizontal = torre.horizontalMirror()

tablero = torre.join(torre_horizontal)

resultado = tablero.up(tablero)

draw(resultado)


