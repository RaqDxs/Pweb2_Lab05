from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]



# Completed 
  def verticalMirror(self):
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical



# Completed 
  def horizontalMirror(self):
    return Picture(self.img[::-1])



# Completed 
  def negative(self):
    negativo = []
    for value in self.img:
        filaInvertida = ""
        for character in value:
            inverted_character = self._invColor(character)
            filaInvertida += inverted_character
        negativo.append(filaInvertida)
    return Picture(negativo)



# Completed 
  def join(self, p):
    unido = []
    for i in range(len(self.img)):
      filaJunta = self.img[i] + p.img[i]
      unido.append(filaJunta)
    return Picture(unido)



# ToDo 
  def up(self, p):
    return Picture(None)

# ToDo
  def under(self, p):
    return Picture(None)

# ToDo 
  def horizontalRepeat(self, n):
    return Picture(None)

# ToDo
  def verticalRepeat(self, n):
    return Picture(None)

# ToDo
  def rotate(self):
    return Picture(None)

