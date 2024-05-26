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
    return Picture(vertical)

# Completed 
  def horizontalMirror(self):
    return Picture(self.img[::-1])



# Completed 
  def negative(self):
      negativo = []
      for value in self.img:
          filaInvertida = ""
          for caracter in value:
              filaInvertida += self._invColor(caracter)
          negativo.append(filaInvertida)
      return Picture(negativo)



# Completed 
  def join(self, p):
    unido = []
    for i in range(len(self.img)):
      filaJunta = self.img[i] + p.img[i]
      unido.append(filaJunta)
    return Picture(unido)



# Completed 
  def up(self, p):
    compuesto = []
    for fila in self.img:
      compuesto.append(fila)
    for fila in p.img:
      compuesto.append(fila)
    return Picture(compuesto)


# Completed
  def under(self, p):
    sobrepuesto = []
    for fila_index, fila in enumerate(p.img):  
      filaSobrepuesta = ""
      for col_index, caracter in enumerate(fila):  
        if caracter != " ":
          filaSobrepuesta += caracter
        else:
          filaSobrepuesta += self.img[fila_index][col_index]  
      sobrepuesto.append(filaSobrepuesta)
    return Picture(sobrepuesto)

# Completed 
  def horizontalRepeat(self, n):
    repetidoH = []
    for fila in self.img:
      filaRepetida = fila * n
      repetidoH.append(filaRepetida)
    return Picture(repetidoH)

# Completed
  def verticalRepeat(self, n):
    repetidoV = []
    for i in range(n):
      for fila in self.img:
        repetidoV.append(fila)
    return Picture(repetidoV)


# Completed
  def rotate(self):
    b = []
    lenSelf = len(self.img)
    for i in range(lenSelf):
      a = ""
      for value in self.img:
        a += value[lenSelf - 1 - i]
      b.append(a)
    return Picture(b)

