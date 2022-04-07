from updatedGraphics import *
from Trail import *

class TronGrid(object):
    """creates a TronGrid"""
    """creates the grid for the tron grid"""

    def __init__(self, win):
        """constructor for the grid"""
        self.rows = []
        self.color = "black"
        self.drawGrid(win)

    def drawGrid(self, win):
        """creates and draws the grid"""
        for x in range(0, win.getWidth(), 10):
            colums = []
            for y in range(0, win.getHeight(), 10):
                l = Trail(x, y, self.color, win)
                colums.append(l)
            self.rows.append(colums)
        for x in self.rows:
            for i in x:
                i.draw(win)

    def changeColor(self, location, bikeColor):
        """changes the color of a set location to the bike color"""
        row = location[0]
        column = location[1]
        self.rows[row][column].changeColor(bikeColor)

    def getIsTrail(self, location):
        """returns isTrail of Trail object"""
        row = location[0]
        column = location[1]
        return self.rows[row][column].isTrail

    def undraw(self):
        """undraws TronGrid"""
        for i in self.rows:
            for j in i:
                j.undraw()