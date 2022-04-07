from Bike import *
import random

class AiBike(Bike):

    def __init__(self, center, location, direction):
        """"creates an ai"""
        super(AiBike, self).__init__(center, location)
        self.colors = ["red", "orange", "purple", color_rgb(234,58,208)]
        pick = random.randint(0,3)
        for i in range(4):
            if i == pick:
                self.color = self.colors[i]
        self.direction = direction
        self.collision = False
    def draw(self, win):
        """draws the ai in the window"""
        self.square.setFill(self.color)
        super().draw(win)

    def moveAi(self, win, tronGrid):
       """moves the ai and updates its location based on direction"""
       self.direction = self.changeDir(win, tronGrid)
       if self.direction == "N":
           self.square.move(0, -10)
           self.location[1] -= 1
           self.collision = self.detectCollision(win, tronGrid, self.direction)
       elif self.direction == "S":
           self.square.move(0, 10)
           self.location[1] += 1
           self.collision = self.detectCollision(win, tronGrid, self.direction)
       elif self.direction == "W":
           self.square.move(-10, 0)
           self.location[0] -= 1
           self.collision = self.detectCollision(win, tronGrid, self.direction)
       elif self.direction == "E":
           self.square.move(10, 0)
           self.location[0] += 1
           self.collision = self.detectCollision(win, tronGrid, self.direction)


    def changeDir(self, win, tronGrid):
        """changes direction based on checkWallCollision and tron grid"""
        if self.direction == "N" and self.location[
            1] != 1:  # determines the x and y of the next location depending on the direction and whether it is touching the wall or not
            y = -1
            x = 0
            leftLocation = [self.location[0] - 1, self.location[1]]
            rightLocation = [self.location[0] + 1, self.location[1]]
            must = False
        elif self.direction == "N" and self.location[0] == 1:
            x = 0
            y = 0
            leftLocation = [self.location[0] + 1, self.location[1]]
            rightLocation = [self.location[0] + 1, self.location[1]]
            must = True
        elif self.direction == "N" and self.location[0] == win.getWidth() // 10 - 2:
            x = 0
            y = 0
            leftLocation = [self.location[0] - 1, self.location[1]]
            rightLocation = [self.location[0] - 1, self.location[1]]
            must = True
        elif self.direction == "N":
            x = 0
            y = 0
            leftLocation = [self.location[0] - 1, self.location[1]]
            rightLocation = [self.location[0] + 1, self.location[1]]
            must = True
        elif self.direction == "S" and self.location[1] != win.getHeight() // 10 - 2:
            y = 1
            x = 0
            leftLocation = [self.location[0] + 1, self.location[1]]
            rightLocation = [self.location[0] - 1, self.location[1]]
            must = False
        elif self.direction == "S" and self.location[0] == 1:
            x = 0
            y = 0
            leftLocation = [self.location[0] + 1, self.location[1]]
            rightLocation = [self.location[0] + 1, self.location[1]]
            must = True
        elif self.direction == "S" and self.location[0] == win.getWidth() // 10 - 2:
            x = 0
            y = 0
            leftLocation = [self.location[0] - 1, self.location[1]]
            rightLocation = [self.location[0] - 1, self.location[1]]
            must = True
        elif self.direction == "S":
            x = 0
            y = 0
            leftLocation = [self.location[0] + 1, self.location[1]]
            rightLocation = [self.location[0] - 1, self.location[1]]
            must = True
        elif self.direction == "W" and self.location[0] != 1:
            x = -1
            y = 0
            leftLocation = [self.location[0], self.location[1] + 1]
            rightLocation = [self.location[0], self.location[1] - 1]
            must = False
        elif self.direction == "W" and self.location[1] == 1:
            x = 0
            y = 0
            leftLocation = [self.location[0], self.location[1] + 1]
            rightLocation = [self.location[0], self.location[1] + 1]
            must = True
        elif self.direction == "W" and self.location[1] == win.getHeight() // 10 - 2:
            x = 0
            y = 0
            leftLocation = [self.location[0], self.location[1] - 1]
            rightLocation = [self.location[0], self.location[1] - 1]
            must = True
        elif self.direction == "W":
            x = 0
            y = 0
            leftLocation = [self.location[0], self.location[1] + 1]
            rightLocation = [self.location[0], self.location[1] - 1]
            must = True
        elif self.direction == "E" and self.location[0] != win.getWidth() // 10 - 2:
            x = 1
            y = 0
            leftLocation = [self.location[0], self.location[1] - 1]
            rightLocation = [self.location[0], self.location[1] + 1]
            must = False
        elif self.direction == "E" and self.location[1] == 1:
            x = 0
            y = 0
            leftLocation = [self.location[0], self.location[1] + 1]
            rightLocation = [self.location[0], self.location[1] + 1]
            must = True
        elif self.direction == "E" and self.location[1] == win.getHeight() // 10 - 2:
            x = 0
            y = 0
            leftLocation = [self.location[0], self.location[1] - 1]
            rightLocation = [self.location[0], self.location[1] - 1]
            must = True
        elif self.direction == "E":
            x = 0
            y = 0
            leftLocation = [self.location[0], self.location[1] - 1]
            rightLocation = [self.location[0], self.location[1] + 1]
            must = True

        Nextlocation = [self.location[0] + x, self.location[1] + y] #using the x and y from above makes a next location variable
        yes = random.randint(1,10)
        if tronGrid.getIsTrail(Nextlocation) == True or must == True: #using getIsTrail from trongrid determines if it needs to change direction
            pick = random.randint(0,1)
            if self.direction == "N": #depending on direction and pick and whether the left or right location are good to go to, changes direction to the left or right
                if leftLocation == rightLocation:
                    if self.location[0] == 1:
                        change = "E"
                    else:
                        change = "W"
                elif pick == 0 and tronGrid.getIsTrail(leftLocation) == False:
                    change = "W"
                elif pick == 0 and tronGrid.getIsTrail(rightLocation) == False:
                    change = "E"
                elif pick == 1 and tronGrid.getIsTrail(rightLocation) == False:
                    change = "E"
                elif pick == 1 and tronGrid.getIsTrail(leftLocation) == False:
                    change = "W"
                else:
                    change = "N"
            elif self.direction == "S":
                if leftLocation == rightLocation:
                    if self.location[0] == 1:
                        change = "E"
                    else:
                        change = "W"
                elif pick == 0 and tronGrid.getIsTrail(leftLocation) == False:
                    change = "E"
                elif pick == 0 and tronGrid.getIsTrail(rightLocation) == False:
                    change = "W"
                elif pick == 1 and tronGrid.getIsTrail(rightLocation) == False:
                    change = "W"
                elif pick == 1 and tronGrid.getIsTrail(leftLocation) == False:
                    change = "E"
                else:
                    change = "S"
            elif self.direction == "W":
                if leftLocation == rightLocation:
                    if self.location[1] == 1:
                        change = "S"
                    else:
                        change = "N"
                elif pick == 0 and tronGrid.getIsTrail(leftLocation) == False:
                    change = "S"
                elif pick == 0 and tronGrid.getIsTrail(rightLocation) == False:
                    change = "N"
                elif pick == 1 and tronGrid.getIsTrail(rightLocation) == False:
                    change = "N"
                elif pick == 1 and tronGrid.getIsTrail(leftLocation) == False:
                    change = "S"
                else:
                    change = "W"
            elif self.direction == "E":
                if leftLocation == rightLocation:
                    if self.location[1] == 1:
                        change = "S"
                    else:
                        change = "N"
                elif pick == 0 and tronGrid.getIsTrail(leftLocation) == False:
                    change = "N"
                elif pick == 0 and tronGrid.getIsTrail(rightLocation) == False:
                    change = "S"
                elif pick == 1 and tronGrid.getIsTrail(rightLocation) == False:
                    change = "S"
                elif pick == 1 and tronGrid.getIsTrail(leftLocation) == False:
                    change = "N"
                else:
                    change = "E"
        else:
            change = self.direction
        return change #returns the direction it needs to change too
