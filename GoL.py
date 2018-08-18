import random
import collections


class GameOfLife:

    def __init__(self, xsize, ysize):

        self.xsize = xsize
        self.ysize = ysize
        self.b1 = {}
        self.b2 = {}

    def get(self, x, y):
        if 0 < x < self.xsize and 0 < y < self.ysize:
            i = '{}x{}'.format(x, y)
            return self.b1[i]
        else:
            return 0

    def set(self, x, y, a):
        al = "{}x{}".format(x, y)
        self.b1[al] = a

    def setnew(self, x, y, a):
        o = "{}x{}".format(x, y)
        self.b2[o] = a

    def start(self):
        for a in range(0, self.xsize):
            for b in range(0, self.ysize):
                if random.random() > 0.9:
                    self.set(a, b, 1)
                else:
                    self.set(a, b, 0)

    def tick(self):

        self.b2 = {}

        for a in range(0, self.xsize):
            for b in range(0, self.ysize):
                neighbours = [self.get(a + 1, b), self.get(a - 1, b), self.get(a + 1, b - 1), self.get(a, b - 1),
                              self.get(a - 1, b - 1), self.get(a + 1, b + 1), self.get(a, b + 1),
                              self.get(a - 1, b + 1)]

                tot = sum(neighbours)
                if tot > 3:
                    self.setnew(a, b, 0)
                elif tot == 3 and self.get(a, b) == 0:
                    self.setnew(a, b, 1)
                elif tot < 2 and self.get(a, b) == 1:
                    self.setnew(a, b, 0)
                else:
                    self.setnew(a,b,self.get(a,b))

        self.b1 = self.b2


    def draw(self):
        outter = []
        for a in range(0, self.xsize):
            for b in range(0, self.ysize):
                    if self.get(a, b) == 0:
                        outter.append(" ")
                    else:
                        outter.append("X")
            outter.append("\n")
        jim: str = ''.join(outter)
        print(jim)
