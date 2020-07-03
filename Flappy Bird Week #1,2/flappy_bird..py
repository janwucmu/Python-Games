import math
import random
from tkinter import *

# first week
def init(data):
    # location of bird
    data.birdX, data.birdY = 400, 200
    # height of jump
    data.jump = 20
    # size of asteroid
    data.asteroidWidth = 40
    data.asteroidHeight = 20
    # size of bird
    data.birdWidth = 20
    data.birdHeight = 20
    # if it is jumping (when you hit spacebar)
    data.jumping = False

    # DO NOT TOUCH BELOW
    data.asteroids = []
    data.timer = 0
    data.gameOver = True;

# first week
def mousePressed(event, data):
    # use event.x and event.y
    pass

# first week
def keyPressed(event, data):
    # use event.char and event.keysym
    if(event.keysym == "space"):
        if (not data.gameOver):
            jump(data)
            data.jumping = True
    if(event.keysym == "s"):
        init(data)
        data.gameOver = not data.gameOver

# first week
def jump(data):
    data.birdY -= 30
# first week
def gravity(data):
    data.birdY += 10

# second week
def checkCollisions(data):
    for asteroid in data.asteroids:
        x, y, speed = asteroid
        if ((data.birdX + data.birdWidth > x) and 
            (data.birdX < (x + data.asteroidWidth)) and
            (data.birdY + data.birdHeight > y) and 
            (data.birdY < (y + data.asteroidHeight))):
                data.gameOver = True
    pass

# second week
def moveAsteroids(data):
    for asteroid in data.asteroids:
        x, y, speed = asteroid
        x -= speed
        data.asteroids.remove(asteroid)
        data.asteroids.append((x, y, speed))

# second week
def removeAsteroids(data):
    for asteroid in data.asteroids:
        x, y, speed = asteroid
        if (x <= 0):
            data.asteroids.remove(asteroid)

# first and second week
def timerFired(data):
    checkCollisions(data)
    if (not data.gameOver):
        data.timer += 1
        if (data.timer % 20 == 0):
            data.asteroids.append((800, random.randint(0, 400), 
                                    random.randint(3, 20)))
        moveAsteroids(data)
        removeAsteroids(data)
        if (not data.jumping):
            gravity(data)
        data.jumping = False

# first week
def drawBird(canvas, data):
    canvas.create_rectangle(data.birdX, data.birdY,
                        data.birdX + data.birdWidth,
                        data.birdY + data.birdHeight,
                        fill='black')

# second week
def drawAsteroid(canvas, data):
    for asteroid in data.asteroids:
        x, y, speed = asteroid
        canvas.create_rectangle(x, y, x + data.asteroidWidth, 
                                y + data.asteroidHeight, fill='green')

# first week
def drawText(canvas, data):
    if (not data.gameOver):
        instruction = "Press 's' to start and 'space' to jump\nDO NOT TOUCH THE GREEN BLOCKS"
    else:
        instruction = "Press 's' to start game"
    canvas.create_text(400, 20, anchor=CENTER, text=instruction,
                           fill='red')

def redrawAll(canvas, data):
    drawText(canvas, data)
    drawAsteroid(canvas, data)
    drawBird(canvas, data)

####################################
# use the run function as-is
####################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init

    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 80  # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
              mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
              keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(800, 400)