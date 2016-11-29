from graphics import *

class Healthbar:

    def __init__(self, win, x1, y1, x2, y2):
        self.rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rectangle.setOutline(color_rgb(255, 255, 255))
        self.rectangle.setFill(color_rgb(255, 50, 50))
        self.rectangle.draw(win)

    def health_drop(self):
        self.rectangle.setFill(color_rgb(0, 0, 0))