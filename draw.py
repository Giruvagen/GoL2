from gof2 import *
from graphics import *

new = boardStart(64,64)
new.evalBoard(new.alive())
plott = new.bs
win = GraphWin("grid", 64, 64, autoflush=False)

def drawer(plotter):
  plott = new.bs
  for x in range(0,64):
    for y in range(0,64):
        if plotter[str(x)+','+str(y)] == 1:
            win.plot(x,y, "blue")
            update(100000)
        else:
            win.plot(x,y, "white")
            update(100000)
  new.evalBoard(plott)
  drawer(new.bs)
drawer(plott)