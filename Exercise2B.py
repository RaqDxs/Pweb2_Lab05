from interpreter import draw
from chessPictures import *

caballo1 = Picture(KNIGHT)
caballo2 = caballo1.negative()
fila1 = caballo1.join(caballo2)
fila2 = fila1.verticalMirror()

fila1_picture = Picture(fila1)
fila2_picture = Picture(fila2)

tablero = fila1_picture.up(fila2_picture)
draw(tablero)