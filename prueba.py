from chessPictures import *
from interpreter import draw

torre = Picture(ROCK)

torre_horizontal = torre.horizontalMirror()

tablero1 = torre.join(torre_horizontal).horizontalRepeat(3)
tablero2 = tablero1.negative()

tablero3 = tablero2.verticalRepeat(2)

# Ahora aplicamos la rotación
resultado = tablero3.rotate()

draw(resultado)
