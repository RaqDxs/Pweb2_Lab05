from interpreter import draw
from chessPictures import *

cuadroBlanco = Picture(SQUARE)
cuadroNegro = cuadroBlanco.negative()




tablero1 = cuadroBlanco.join(cuadroNegro).horizontalRepeat(4)
tablero2 = tablero1.negative()
fila1 = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
fila2 = pawn.horizontalRepeat(8)


tableroSuperior = tablero2.up(tablero1).under(fila1.up(fila2)).negative()
tableroMedio = tablero1.up(tablero2).verticalRepeat(2)
tableroInferior = tablero1.up(tablero2).under(fila2.up(fila1))

final = tableroSuperior.up(tableroMedio).up(tableroInferior)
draw(final)
