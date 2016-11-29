from graphics import *
import math
import random


class Projectile:

    def __init__(self, win, x, y):
        self.circle = Circle(Point(x, y), 20)
        self.circle.setFill(color_rgb(0, 255, 130))
        self.circle.setOutline(color_rgb(0, 255, 130))
        self.circle.draw(win)
        self.vel_x = 80
        self.vel_y = 0
   

    def update(self, delta_time):
        dx = self.vel_x * delta_time
        dy = self.vel_y * delta_time
        self.circle.move(dx, dy)

    def projectile_collision(self, c):
        cx = c.circle.getCenter().getX()
        cy = c.circle.getCenter().getY()
        center = self.circle.getCenter()
        r = c.circle.getRadius()
        dist = math.sqrt((cx-center.x)**2 + (cy-center.y)**2)
        if dist <= r+20:
            return True
        return False
