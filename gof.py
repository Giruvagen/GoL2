# oonways game of life python implementation
import numpy
import turtle
import random


class boardStart:
    # creates the board and initial condition
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.bs = []
        self.b2 = []
        self.al = []

    def alive(self):
        for a in range(0, self.xsize):
            for b in range(0, self.ysize):
                if random.random() > 0.5:
                    self.bs.append([a, b,1])
                else:
                    self.bs.append([a,b,0])
    def evalBoard(self):
        self.b2 = self.bs
        for a in self.bs:
            self.al.append(a[2])
        for i in self.al:
            if i[2] == 0:
              nsum =
              if nsum == 3:
                self.b2[i][2] = 1
              else:
                self.b2[i][2] = 0
            elif i[2] == 1:
              n = []
              nsum = sum(n)
              if nsum == 2 or 3:
                  self.b2[i][2] = 1
              elif nsum == 0 or 1:
                  self.b2[i][2] = 0
              elif nsum > 3:
                  self.b2[i][2] = 0
        self.bs = self.b2




new = boardStart(16, 16)
new.alive()
