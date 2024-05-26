def join(self, p):
    unido = []
    for i in range(len(self.img)):
        filaJunta = self.img[i] + p.img[i]
        unido.append(filaJunta)
    return Picture(unido)
