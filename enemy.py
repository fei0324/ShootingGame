from graphics import *


class Enemy:

    def __init__(self, win, x, y):
        self.circle = Circle(Point(x, y), 40)
        self.circle.setFill("yellow")
        self.circle.setOutline("yellow")
        self.circle.draw(win)
        self.vel_x = -50
        self.vel_y = 0

    def update(self, delta_time):
        dx = self.vel_x * delta_time
        dy = self.vel_y * delta_time
        self.circle.move(dx, dy)
