def negative(self):
    negativo = []
    for value in self.img:
        filaInvertida = ""
        for caracter in value:
            filaInvertida += self._invColor(caracter)
        negativo.append(filaInvertida)
    return Picture(negativo)
