from updatedGraphics import *
import time

class Scene(object):
    """the different scenes for the game"""

    def __init__(self, win):
        """constructor for scene object"""
        self.tronTitle = Image(Point(win.getWidth() / 2 - 15, win.getHeight() / 2 - 200), "TronTitle.png")
        self.background = Rectangle(Point(0,0), Point(win.getHeight(), win.getWidth()))
        self.orangeGuy = Image(Point(100, win.getHeight()/2), "orangeGuy.png")
        self.blueGuy = Image(Point(150, win.getHeight()/2), "blueGuy.png")
        self.text = ["Press Start", "Instructions", "You Win", "You Lost"]
        self.textOn = Text(Point(win.getWidth() / 2 - 15, win.getHeight() / 2 + 100), self.text[1])
        self.bikeColor = None

    def drawIntro(self, win):
        """draws the intro"""
        self.background.setFill('black')
        self.background.draw(win)
        self.tronTitle.draw(win)
        self.orangeGuy.draw(win)
        self.textOn = Text(Point(win.getWidth() / 2 - 15, win.getHeight() / 2 + 100), self.text[0])
        self.textOn.setFace("arial")
        self.textOn.setFill(color_rgb(171, 199, 244))
        self.textOn.setSize(24)
        self.textOn.draw(win)

    def undrawIntro(self):
        """undraws the intro"""
        self.tronTitle.undraw()
        self.orangeGuy.undraw()
        self.textOn.undraw()

    def drawInstructions(self, win):
        """draws all of the instructions"""
        self.blueGuy.draw(win)
        self.textOn = Text(Point(win.getWidth()/ 2 + 150, win.getHeight() / 2 - 100), self.text[1])
        self.textOn.setFace("arial")
        self.textOn.setFill(color_rgb(171, 199, 244))
        self.textOn.setSize(24)
        self.textOn.draw(win)
        bestO = Text(Point(win.getWidth()//2 - 10, 15), "Win 3/5 Games to Win")
        bestO.setFace("arial")
        bestO.setSize(24)
        bestO.setFill(color_rgb(171, 199, 244))
        bestO.draw(win)
        keys = Image(Point(win.getWidth()/2 + 150, win.getHeight()/2 ), "keys.png")
        keys.draw(win)
        colorWant = Text(Point(win.getWidth()/2, win.getHeight() - 15), "Pick the color you want using 1 - 5")
        colorWant.setSize(24)
        colorWant.setFill(color_rgb(171, 199, 244))
        colorWant.draw(win)
        colorOne = Text(Point(win.getWidth()/2 - 200, win.getHeight() - 100), "1")
        colorOne.setFill("white")
        colorOne.setSize(24)
        colorOne.draw(win)
        colorTwo = Text(Point(win.getWidth() / 2 - 100, win.getHeight() - 100), "2")
        colorTwo.setFill(color_rgb(101,214,36))
        colorTwo.setSize(24)
        colorTwo.draw(win)
        colorThr = Text(Point(win.getWidth() / 2 , win.getHeight() - 100), "3")
        colorThr.setFill(color_rgb(36, 216, 180))
        colorThr.setSize(24)
        colorThr.draw(win)
        colorFour = Text(Point(win.getWidth() / 2 + 100, win.getHeight() - 100), "4")
        colorFour.setFill(color_rgb(25, 201, 255))
        colorFour.setSize(24)
        colorFour.draw(win)
        colorFive = Text(Point(win.getWidth() / 2 + 200, win.getHeight() - 100), "5")
        colorFive.setFill(color_rgb(27, 61, 232))
        colorFive.setSize(24)
        colorFive.draw(win)
        color = None
        numbers = ["1","2","3","4","5"]
        while color not in numbers:
            color = win.getKey()
        if color == "1":
            self.bikeColor = "white"
        elif color == "2":
            self.bikeColor = color_rgb(101,214,36)
        elif color == "3":
            self.bikeColor = color_rgb(36, 216, 180)
        elif color == "4":
            self.bikeColor = color_rgb(25, 201, 255)
        elif color == "5":
            self.bikeColor = color_rgb(27, 61, 232)
        colorOne.undraw()
        colorTwo.undraw()
        colorThr.undraw()
        colorFour.undraw()
        colorFive.undraw()
        colorWant.undraw()
        for i in range(5, 0 , -1):
            Timer = Text(Point(win.getWidth()/2, 100), str(i))
            Timer.setFace("arial")
            if i == 5 or i == 4:
                Timer.setFill("Green")
            elif i == 3 or i == 2:
                Timer.setFill('yellow')
            else:
                Timer.setFill("red")
            Timer.setSize(24)
            Timer.draw(win)
            time.sleep(1)
            Timer.undraw()
        self.textOn.undraw()
        self.blueGuy.undraw()
        bestO.undraw()
        keys.undraw()

    def scoreScene(self, aiColor, roundsWon, roundsLost, win):
        """draws the score of both the ai and the player"""
        if roundsWon <= 2 and roundsLost <= 2: #if the player or ai has not won draws, pauses and undraws scores, else shows who won and scores
            won = Text(Point(win.getWidth()//2 - 100, 150), "Player Won:")
            won.setFill(self.bikeColor)
            won.setSize(24)
            won.setFace("arial")
            won.draw(win)
            lost = Text(Point(win.getWidth() // 2 + 100, 150), "Ai Won:")
            lost.setFill(aiColor)
            lost.setSize(24)
            lost.setFace("arial")
            lost.draw(win)
            wonR = Text(Point(win.getWidth() // 2 - 100, 200), str(roundsWon) + " Rounds")
            wonR.setFill(self.bikeColor)
            wonR.setSize(24)
            wonR.setFace("arial")
            wonR.draw(win)
            lostR = Text(Point(win.getWidth() // 2 + 100, 200), str(roundsLost) + " Rounds")
            lostR.setFill(aiColor)
            lostR.setSize(24)
            lostR.setFace("arial")
            lostR.draw(win)
            time.sleep(3)
            won.undraw()
            wonR.undraw()
            lost.undraw()
            lostR.undraw()
        else:
            if roundsWon > 2:
                youWon = Text(Point(win.getWidth()//2, 50), "You Won!")
                youWon.setFill(self.bikeColor)
            else:
                youWon = Text(Point(win.getWidth() // 2, 50), "Ai Won!")
                youWon.setFill(aiColor)
            youWon.setFace("arial")
            youWon.setSize(24)
            youWon.draw(win)
            won = Text(Point(win.getWidth() // 2 - 100, 150), "Player Won:")
            won.setFill(self.bikeColor)
            won.setSize(24)
            won.setFace("arial")
            won.draw(win)
            lost = Text(Point(win.getWidth() // 2 + 100, 150), "Ai Won:")
            lost.setFill(aiColor)
            lost.setSize(24)
            lost.setFace("arial")
            lost.draw(win)
            wonR = Text(Point(win.getWidth() // 2 - 100, 200), str(roundsWon) + " Rounds")
            wonR.setFill(self.bikeColor)
            wonR.setSize(24)
            wonR.setFace("arial")
            wonR.draw(win)
            lostR = Text(Point(win.getWidth() // 2 + 100, 200), str(roundsLost) + " Rounds")
            lostR.setFill(aiColor)
            lostR.setSize(24)
            lostR.setFace("arial")
            lostR.draw(win)

