from graphics import *
import math

class Chaser:

    def __init__(self, win, x, y):
        self.circle = Circle(Point(x, y), 25)
        self.circle.setFill(color_rgb(255, 255, 255))
        self.circle.setOutline(color_rgb(255, 255, 255))
        self.circle.draw(win)
        self.vel_x = -10
        #self.vel_y = 0       

    def set_to_chase(self, to_chase):
        self.to_chase = to_chase

    def chase(self, delta_time):
        dx = self.vel_x * delta_time
        #dy = self.vel_y * delta_time
        to_chase_point = self.to_chase.circle.getCenter()
        x = to_chase_point.getX()
        y = to_chase_point.getY()
        my_x = self.circle.getCenter().getX()
        my_y = self.circle.getCenter().getY()
        self.circle.move((x - my_x)/5.0*delta_time + dx,  (y - my_y)/5.0*delta_time)

    def chaser_collision(self, c):
        cx = c.circle.getCenter().getX()
        cy = c.circle.getCenter().getY()
        center = self.circle.getCenter()
        r = c.circle.getRadius()
        dist = math.sqrt((cx-center.x)**2 + (cy-center.y)**2)
        if dist <= r+25:
            return True
        return False






