from interpreter import draw
from chessPictures import *

cuadroBlanco = Picture(SQUARE)
cuadroNegro = cuadroBlanco.negative()

tablero1 = cuadroNegro.join(cuadroBlanco)

tablero = tablero1.horizontalRepeat(4)
draw(tablero)