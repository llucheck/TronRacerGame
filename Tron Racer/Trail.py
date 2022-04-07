from updatedGraphics import *

class Trail(object):
    """creates a Trail object"""

    def __init__(self, x, y, color, win, size = 10):
        """constructor for trail object"""
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.isTrail = False
        self.body = Rectangle(Point(self.x, self.y), Point(self.x + self.size, self.y + self.size))
        self.body.setFill(color)

    def draw(self, win):
        """draws the trail object"""
        self.body.draw(win)

    def changeColor(self, color):
        """changes the color of the trail object and sets isTrail to True"""
        self.body.setFill(color)
        self.body.setOutline(color)
        self.isTrail = True

    def getCenter(self):
        """returns center of Trail object"""
        return self.body.getCenter()

    def undraw(self):
        """undraws Trail object"""
        self.body.undraw()
