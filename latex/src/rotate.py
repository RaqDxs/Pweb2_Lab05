def rotate(self):
    b = []
    lenSelf = len(self.img)
    for i in range(lenSelf):
        a = ""
        for value in self.img:
            a += value[lenSelf - 1 - i]
        b.append(a)
    return Picture(b)
