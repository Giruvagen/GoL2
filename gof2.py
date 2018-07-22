# conways game of life python implementation
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
            if random.random() > 0.8:
                self.bs[i] = 1
            else:
                self.bs[i] = 0
        return self.bs

    def evalBoard(self,bs):
        x = self.xsize
        y = self.ysize
        self.bs = bs
        self.b2 = self.bs
        for a in range(0, x):
            for b in range(0, y):
                if self.bs[str(a) + "," + str(b)] == 1:
                    eval = []
                    if str(a - 1) + "," + str(b) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b)])
                    else:
                        eval.append(0)
                    if str(a + 1) + "," + str(b) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b)])
                    else:
                        eval.append(0)
                    if str(a - 1) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b - 1)])
                    else:
                        eval.append(0)
                    if str(a) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a) + "," + str(b - 1)])
                    else:
                        eval.append(0)
                    if str(a + 1) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b - 1)])
                    else:
                        eval.append(0)
                    if str(a - 1) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b + 1)])
                    else:
                        eval.append(0)
                    if str(a) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a) + "," + str(b + 1)])
                    else:
                        eval.append(0)
                    if str(a + 1) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b + 1)])
                    else:
                        eval.append(0)
                    if sum(eval) == 3 or sum(eval) == 2:
                        self.b2[str(a) + "," + str(b)] = 1
                    else:
                        self.b2[str(a) + "," + str(b)] = 0
                elif self.bs[str(a) + "," + str(b)] == 0:
                    eval = []
                    if str(a - 1) + "," + str(b) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b)])
                    else:
                        eval.append(0)
                    if str(a + 1) + "," + str(b) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b)])
                    else:
                        eval.append(0)
                    if str(a - 1) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b - 1)])
                    else:
                        eval.append(0)
                    if str(a - 2) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a - 2) + "," + str(b - 1)])
                    else:
                        eval.append(0)
                    if str(a + 1) + "," + str(b - 1) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b - 1)])
                    else:
                        eval.append(0)
                    if str(a - 1) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a - 1) + "," + str(b + 1)])
                    else:
                        eval.append(0)
                    if str(a) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a) + "," + str(b + 1)])
                    else:
                        eval.append(0)
                    if str(a + 1) + "," + str(b + 1) in self.bs:
                        eval.append(self.bs[str(a + 1) + "," + str(b + 1)])
                    else:
                        eval.append(0)
                    if sum(eval) == 3:
                        self.b2[str(a) + "," + str(b)] = 1
                    else:
                        self.b2[str(a) + "," + str(b)] = 0
        return self.b2
