from graphics import *
import math


class Wave:

    def __init__(self, win, x, y):
        self.circle = Circle(Point(x, y), 20)
        self.circle.setFill(color_rgb(255, 0, 130))
        self.circle.setOutline(color_rgb(255, 0, 130))
        self.circle.draw(win)
        self.vel_x = -50
   

    def update(self, delta_time):
        dx = self.vel_x * delta_time
        dy = math.sin(time.time())*2
        self.circle.move(dx, dy)

    def wave_collision(self, c):
        cx = c.circle.getCenter().getX()
        cy = c.circle.getCenter().getY()
        center = self.circle.getCenter()
        r = c.circle.getRadius()
        dist = math.sqrt((cx-center.x)**2 + (cy-center.y)**2)
        if dist <= r+20:
            return True
        return False




