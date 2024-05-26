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
