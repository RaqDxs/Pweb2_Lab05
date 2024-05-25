from chessPictures import *
from interpreter import draw


rook_picture = Picture(ROCK)
rook_negative = rook_picture.negative()
draw(rook_negative)

