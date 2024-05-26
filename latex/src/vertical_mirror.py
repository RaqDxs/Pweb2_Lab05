def verticalMirror(self):
    vertical = []
    for value in self.img:
        vertical.append(value[::-1])
    return Picture(vertical)
