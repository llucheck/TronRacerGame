from updatedGraphics import *

class Bike(object):
    """creates a bike object"""
    def __init__(self, center, location):
        """constructor for bike"""
        self.location = location
        self.x = center.getX()
        self.y = center.getY()
        self.square = Rectangle(Point(self.x + 5, self.y + 5), Point(self.x - 5, self.y - 5))

    def drawBike(self, win: GraphWin):
        """draws the bike"""
        self.square.draw(win)

    def detectCollision(self, win, TronGrid, direction):
        """collision detection : if it collides with the walls or the trail returns true"""
        collision = False
        if self.location[1] == 0 and direction == "N":
            collision = True
        elif self.location[1] == win.getHeight()//10 -1 and direction == "S":
            collision = True
        elif self.location[0] == 0 and direction == "W":
            collision = True
        elif self.location[0] == win.getWidth()//10 - 1 and direction == "E":
            collision = True
        elif TronGrid.getIsTrail(self.location) != False:
            collision = True
        return collision

    def undraw(self):
        """undraws the bike"""
        self.square.undraw()


