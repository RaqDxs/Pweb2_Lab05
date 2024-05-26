def verticalRepeat(self, n):
    repetidoV = []
    for i in range(n):
        for fila in self.img:
            repetidoV.append(fila)
    return Picture(repetidoV)
