from GoL import *
from graphics import *

new = GameOfLife(64,64)
new.start()
win = GraphWin("grid", 1024, 1024, autoflush=False)

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def drawer():
  for x in range(0,64):
    for y in range(0,64):
        if new.get(x,y) == 1:
            aRectangle = Rectangle(Point(x*16, y*16), Point(x*16+16, y*16+16))
            aRectangle.setFill("red")
            aRectangle.setOutline("red")
            aRectangle.draw(win)
        else:
            bRectangle = Rectangle(Point(x * 16, y * 16), Point(x * 16 + 16, y * 16 + 16))
            bRectangle.setFill("white")
            bRectangle.setOutline("white")
            bRectangle.draw(win)

  update(30)
  new.tick()
  clear(win)
  drawer()
drawer()