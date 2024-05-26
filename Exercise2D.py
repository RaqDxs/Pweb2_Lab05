from interpreter import draw
from chessPictures import *

cuadroBlanco = Picture(SQUARE)
cuadroNegro = cuadroBlanco.negative()

tablero1 = cuadroBlanco.join(cuadroNegro)

tablero = tablero1.horizontalRepeat(4)
draw(tablero)