from graphics import *
import math

class Player:

    def __init__(self, window, x, y):
        """ Player class initializer.

        Parameters:
            self (Player): The class instance.
            window (GraphWin): The game window.
            x (int): The x position of the center of the Player.
            y (int): The y position of the center of the Player.

        Output:
            Player: an instance of the Player class.

        Examples:
            Player(w, 100, 100) => Places a new Player instance at position
                <100, 100> on the w instance of the GraphWin class.
        """
        self.circle = Circle(Point(x,y), 20)
        self.circle.setFill(color_rgb(0,130,255))
        self.circle.setOutline(color_rgb(0,130,255))
        self.circle.draw(window)
        

    def update(self, keys, delta_time):
        """ The update function for instances of the Player class. This
        function is where Player instances respond to changing game state and
        keyboard input.

        Parameters:
            self (Player): The class instance.
            keys (dict): A dictionary containing characters (represented as
                strings) as keys and boolean values. The booleans are true
                when the keyboard input specified by the corresponding dict
                key is pressed. It is false if the key is not pressed.
            delta_time (float): How much time has passed in seconds since
                update was last called.

        Examples:
            p.update({"a": True}, 0.0033) => Updates the Player instance by
                by 0.0033 seconds. Since "a" is a key in the keys dict
                parameter, the ship should move to the left by its movement
                speed per second times delta_time (which has the value of
                0.0033).
        """
        if keys["a"] == True:
            self.circle.move(-60*delta_time, 0)
        elif keys["w"] == True:
            self.circle.move(0, -60*delta_time)
        elif keys["s"] == True:
            self.circle.move(0, 60*delta_time)
        elif keys["d"] == True:
            self.circle.move(60*delta_time, 0)
        
    def point_collision(self, x, y):
        """ Determines if an instance of the Player class coincides with a
        with an <x,y> coordinate.

        Parameters:
            self (Player): The class instance.
            x (int): x of coordinate to check for collision.
            y (int): y of coordinate to check for collision.

        Output:
            boolean: True if <x,y> collides with this instance of the Player
                class or False otherwise.

        Examples:
            p = Player(window, 100, 100)
            p.point_collision(100, 100) => True
            p.point_collision(500, 500) => False
        """
        center = self.circle.getCenter()
        dis = math.sqrt((x-center.x)**2 + (y-center.y)**2)
        if -25 <= dis <= 25:
            return True
        return False

    def circle_collision(self, c):
        """ Determines if an instance of the Player class coincides with a
        with a Cirlce instance.

        Parameters:
            self (Player): The class instance.
            c (Circle): The circle with which to detect collisions.
        Output:
            boolean: True if the Circle c collides with this instance of
             the Player class or False otherwise.

        Examples:
            p = Player(window, 100, 100)
            c1 = Circle(Point(95, 95), 20)
            c2 = Circle(Point(500, 500), 20)
            p.point_collision(c1) => True
            p.point_collision(c2) => False
        """
        cx = c.getCenter().getX()
        cy = c.getCenter().getY()
        center = self.circle.getCenter()
        r = c.getRadius()
        dist = math.sqrt((cx-center.x)**2 + (cy-center.y)**2)
        if dist <= r+20:
            return True
        return False

    def collision_with_enemy(self):
        """ This function should be called when the player collides with an 
        enemy. When a player collides with an enemy, the player turns red.

        Parameters:
            self (Player): The class instance.

        Output:
            No return value. The player turns red.
        """
        self.circle.setFill(color_rgb(255, 0, 0))
        self.circle.setOutline(color_rgb(255, 0, 0))

    def recover_from_collision(self):
        self.circle.setFill(color_rgb(255, 255, 255))