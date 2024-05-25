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




  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical




  def horizontalMirror(self):
    return Picture(self.img[::-1])




  def negative(self):
    negativo = []
    for value in self.img:
        filaInvertida = ""
        for character in value:
            inverted_character = self._invColor(character)
            filaInvertida += inverted_character
        negativo.append(filaInvertida)
    return Picture(negativo)




  def join(self, p):
    unido = []
    for i in range(len(self.img)):
      filaJunta = self.img[i] + p.img[i]
      unido.append(filaJunta)
    return Picture(unido)




  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

