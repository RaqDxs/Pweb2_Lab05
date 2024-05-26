def up(self, p):
    compuesto = []
    for fila in self.img:
        compuesto.append(fila)
    for fila in p.img:
        compuesto.append(fila)
    return Picture(compuesto)
