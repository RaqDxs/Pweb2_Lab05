def horizontalRepeat(self, n):
    repetidoH = []
    for fila in self.img:
        filaRepetida = fila * n
        repetidoH.append(filaRepetida)
    return Picture(repetidoH)
