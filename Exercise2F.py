from interpreter import draw
from chessPictures import *

cuadroBlanco = Picture(SQUARE)
cuadroNegro = cuadroBlanco.negative()

tablero1 = cuadroBlanco.join(cuadroNegro).horizontalRepeat(4)
tablero2 = tablero1.negative()

tablero = tablero1.up(tablero2).verticalRepeat(2)
draw(tablero)