from Bike import *

class TronBike(Bike):
    """creates the player controlled bike"""

    def __init__(self, win, color, center, location, direction):
        """constructor for the Player Controlled Bike"""
        super(TronBike, self).__init__(center, location)
        self.color = color
        self.center = center
        self.direction = direction
        self.draw(win)
        self.collision = False

    def draw(self, win):
        """draws the player controlled bike on the screen"""
        self.square.setFill(self.color)
        self.square.setOutline(self.color)
        super().drawBike(win)

    def moveBike(self, direction, win, TronGrid):
        """moves the bike based on direction, updates its location, and detects collision"""
        self.direction = direction #updates direction based on given direction
        if self.direction == "N":
            self.square.move(0, -10)
            self.location[1] -= 1
            self.collision = self.detectCollision(win, TronGrid, self.direction) #detects if the bike collides with the trail on its location
        elif self.direction == "S":
            self.square.move(0, 10)
            self.location[1] += 1
            self.collision = self.detectCollision(win, TronGrid, self.direction)
        elif self.direction == "W":
            self.square.move(-10, 0)
            self.location[0] -= 1
            self.collision = self.detectCollision(win, TronGrid, self.direction)
        elif self.direction == "E":
            self.square.move(10, 0)
            self.location[0] += 1
            self.collision = self.detectCollision(win, TronGrid, self.direction)