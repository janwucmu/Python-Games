# import turtle

# # set up the game
# wn = turtle.Screen()
# wn.title("Pong")
# wn.bgcolor("black")
# wn.setup(width=800, height=600)
# wn.tracer(0)

# # Score
# score_a = 0
# score_b = 0

# # Paddle A
# paddle_a = turtle.Turtle()
# paddle_a.speed(0)
# paddle_a.shape("square")
# paddle_a.color("white")
# paddle_a.shapesize(stretch_wid=5,stretch_len=1)
# paddle_a.penup()
# paddle_a.goto(-350, 0)

# # Paddle B
# paddle_b = turtle.Turtle()
# paddle_b.speed(0)
# paddle_b.shape("square")
# paddle_b.color("white")
# paddle_b.shapesize(stretch_wid=5,stretch_len=1)
# paddle_b.penup()
# paddle_b.goto(350, 0)

# # Ball
# ball = turtle.Turtle()
# ball.speed(0)
# ball.shape("square")
# ball.color("white")
# ball.penup()
# ball.goto(0, 0)
# ball.moveX = 2
# ball.moveY = 2

# # Pen
# pen = turtle.Turtle()
# pen.speed(0)
# pen.shape("square")
# pen.color("white")
# pen.penup()
# pen.hideturtle()
# pen.goto(0, 260)
# pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# # Functions
# def paddle_a_up():
#     y = paddle_a.ycor()
#     y += 20
#     paddle_a.sety(y)

# def paddle_a_down():
#     y = paddle_a.ycor()
#     y -= 20
#     paddle_a.sety(y)

# def paddle_b_up():
#     y = paddle_b.ycor()
#     y += 20
#     paddle_b.sety(y)

# def paddle_b_down():
#     y = paddle_b.ycor()
#     y -= 20
#     paddle_b.sety(y)

# # Keyboard bindings
# wn.listen()
# wn.onkeypress(paddle_a_up, "a")
# wn.onkeypress(paddle_a_down, "z")
# wn.onkeypress(paddle_b_up, "Up")
# wn.onkeypress(paddle_b_down, "Down")

# # Main game loop
# while True:
#     wn.update()
    
#     # Move the ball
#     ball.setx(ball.xcor() + ball.moveX)
#     ball.sety(ball.ycor() + ball.moveY)

#     # Border checking

#     # Top
#     if ball.ycor() >= 290:
#         ball.sety(290)
#         ball.moveY *= -1
    
#     # Bottom
#     elif ball.ycor() <= -290:
#         ball.sety(-290)
#         ball.moveY *= -1

#     # Right
#     if ball.xcor() >= 350:
#         score_a += 1
#         pen.clear()
#         pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
#         ball.goto(0, 0)
#         ball.moveX *= -1

#     # Left
#     elif ball.xcor() <= -350:
#         score_b += 1
#         pen.clear()
#         pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
#         ball.goto(0, 0)
#         ball.moveX *= -1

#     # Paddle and ball collisions
#     if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
#         ball.moveX *= -1 
    
#     elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
#         ball.moveX *= -1


from tkinter import *

root = Tk()

def printHelloWorld():
    print("Hello World")

button = Button(root,text="Hello", command=printHelloWorld)

button.pack()
button.mainloop()
