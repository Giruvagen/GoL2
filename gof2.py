# oonways game of life python implementation
import numpy
import turtle
import random
import collections


class boardStart:
    # creates the board and initial condition
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.start = []
        self.bs = collections.OrderedDict()
        self.b2 = collections.OrderedDict()

    def alive(self):
        for a in range(0, self.xsize):
            for b in range(0, self.ysize):
                self.start.append(str(a) + "," + str(b))
        for i in self.start:
            if random.randint(1,100) > 90:
                self.bs[i] = 0
            else:
                self.bs[i] = 1
        return self.bs

    def evalBoard(self, bs):
        self.bs = bs
        self.b2 = bs
        x = self.xsize
        y = self.ysize
        for a in range(0, x):
            for b in range(0, y):
                if self.bs[str(a) + "," + str(b)] == 1:
                    eval = []
                    if str(a - 1) + "," + str(b) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b)])
                    if str(a + 1) + "," + str(b) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b)])
                    if str(a - 1) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b - 1)])
                    if str(a) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a) + "," + str(b - 1)])
                    if str(a + 1) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b - 1)])
                    if str(a - 1) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b + 1)])
                    if str(a) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a) + "," + str(b + 1)])
                    if str(a + 1) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b + 1)])
                    if sum(eval) == 3 or sum(eval) == 2:
                        self.b2[str(a) + "," + str(b)] = 1
                    elif sum(eval) < 1:
                        self.b2[str(a) + "," + str(b)] = 0
                    elif sum(eval) > 3:
                        self.b2[str(a) + "," + str(b)] = 0
                else:
                    eval = []
                    if str(a - 1) + "," + str(b) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b)])
                    if str(a + 1) + "," + str(b) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b)])
                    if str(a - 1) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b - 1)])
                    if str(a - 2) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a - 2) + "," + str(b - 1)])
                    if str(a + 1) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b - 1)])
                    if str(a - 1) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b + 1)])
                    if str(a) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a) + "," + str(b + 1)])
                    if str(a + 1) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b + 1)])
                    if sum(eval) == 3:
                        self.b2[str(a) + "," + str(b)] = 1
        return self.bs
