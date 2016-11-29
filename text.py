from graphics import *
import time

win = GraphWin("text", 400, 400)
text = Text(Point(200, 200), "Hello")
text.draw(win)
text.setText("world")


