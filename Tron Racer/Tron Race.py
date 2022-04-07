from Scene import *
from TronGrid import *
from TronBike import *
from Ai import *
import time

win = GraphWin("Tron", 600, 600)

def findDirection(key, currentD):
    """returns different strings for certain clicked keys"""
    if key == "Up":
        return "N"
    elif key == "Down":
        return "S"
    elif key == "Left":
        return "W"
    elif key == "Right":
        return "E"
    elif key == "L":
        return "l"
    else:
        return currentD

def Main():
    """runs the game of Tron"""
    sceneChanger = Scene(win)
    sceneChanger.drawIntro(win)
    check = None
    while check != "space": #keeps looping until space is clicked
        check = win.getKey()
    sceneChanger.undrawIntro()
    sceneChanger.drawInstructions(win)
    roundsWon = 0
    roundsLost = 0
    while roundsWon <= 2 and roundsLost <= 2: #as long as no one has won continues looping the game
        bikeCollision = False
        aiCollision = False
        t1 = TronGrid(win)
        bikeStart = [win.getWidth() // 10 - 2, (win.getHeight() // 10) // 2]
        aiStart = [1, (win.getHeight() // 10) // 2]
        b1 = TronBike(win, sceneChanger.bikeColor, t1.rows[bikeStart[0]][bikeStart[1]].getCenter(), bikeStart,
                      direction="W")
        a1 = AiBike(t1.rows[aiStart[0]][aiStart[1]].getCenter(), aiStart, direction="E")
        currentD = "W"
        while bikeCollision == False and aiCollision == False: #as long as no one has crashed continues looping the movements and color changing
            check = win.checkKey()
            if check != None:
                b1.moveBike(findDirection(check, currentD), win, t1)
                t1.changeColor(b1.location, b1.color)
                bikeCollision = b1.collision
                a1.moveAi(win, t1)
                t1.changeColor(a1.location, a1.color)
                aiCollision = a1.collision
                currentD = findDirection(check, currentD)
                time.sleep(.03)
        if aiCollision == True: #depending on who won the round changes the score
            roundsWon += 1
        else:
            roundsLost += 1
        t1.undraw()
        b1.undraw()
        a1.undraw()
        sceneChanger.scoreScene(a1.color,roundsWon,roundsLost,win)
    win.getMouse()

Main()