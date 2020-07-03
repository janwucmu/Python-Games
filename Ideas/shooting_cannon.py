import math
import random
from tkinter import *

def init(data):
    # load data.xyz as appropriate
    data.kerryWidth, data.kerryHeight = 80, 40
    data.kerryCX, data.kerryCY = (data.kerryWidth/2,
                                  data.height-data.kerryHeight/2)
    data.angle = 0
    data.lineSize = 60
    data.bulletX, data.bulletY = data.kerryCX, data.kerryCY
    data.bulletR = 5
    data.bullets = []
    data.missiles = []
    data.timer = 0
    data.missileR = 20
    data.bulletSpeed = 35


def mousePressed(event, data):
    # use event.x and event.y
    pass


def keyPressed(event, data):
    # use event.char and event.keysym
    angleSpeed = 10
    maxAngle, minAngle = 90, 0
    if(event.keysym == "Up"):
        if(data.angle < maxAngle):
            data.angle += angleSpeed
    if(event.keysym == "Down"):
        if(data.angle > minAngle):
            data.angle -= angleSpeed
    if(event.keysym == "space"):
        data.bullets.append((data.bulletX, data.bulletY, data.angle, data.bulletSpeed))
    # add a new bullet to the bullet list when the user presses space
    # add in reset if there is time


def circleCollision(cx1, cy1, cx2, cy2, r1, r2):
    # fill me in!
    pass


def checkCollisions(data):
    # check collisions of missiles and bullets
    pass


def moveBullets(data):
    for bullet in data.bullets:
        x, y, angle, bulletYSpeed = bullet
        x += bulletYSpeed * math.cos(math.radians(data.angle))
        y -= bulletYSpeed * math.sin(math.radians(data.angle))
        data.bullets.remove(bullet)
        data.bullets.append((x, y, angle, bulletYSpeed))

    


def moveMissiles(data):
    # fill me in
    pass


def timerFired(data):
    moveBullets(data)

def drawBullets(canvas, data):
    for bullet in data.bullets:
        x, y, angle, bulletYSpeed = bullet
        canvas.create_oval(x - data.bulletR,
                           y - data.bulletR,
                           x + data.bulletR,
                           y + data.bulletR,
                           fill='tan')


def drawMissiles(canvas, data):
    for missile in data.missiles:
        x, y, r = missile
        canvas.create_oval(x - r,
                           y - r,
                           x + r,
                           y + r,
                           fill='blue')


def redrawAll(canvas, data):
    # draw in canvas
    # add a background image

    # fill in these two functions
    drawMissiles(canvas, data)
    drawBullets(canvas, data)
    # draws cannon front
    canvas.create_line(data.kerryCX, data.kerryCY,
                       data.kerryCX + data.lineSize *
                       math.cos(math.radians(data.angle)),
                       data.kerryCY - data.lineSize *
                       math.sin(math.radians(data.angle)),
                       width=10)
    # draws cannon body
    canvas.create_rectangle(data.kerryCX - data.kerryWidth/2,
                            data.kerryCY - data.kerryHeight/2,
                            data.kerryCX + data.kerryWidth/2,
                            data.kerryCY + data.kerryHeight/2,
                            fill='darkBlue')

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
    data.timerDelay = 100  # milliseconds
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