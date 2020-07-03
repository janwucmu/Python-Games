from tkinter import *

root = Tk()
root.geometry("675x400")

instruction = "Questions"
left = "left button"
right = "right button"
ice_cream = "Ice Cream"
cheeseburger = "Cheeseburger"

var = IntVar()
question = IntVar()
clinic = IntVar()

def drawCheeseburger():
    clearCanvas()
    canvas.create_oval(100, 90, 200, 160, fill="tan")
    canvas.create_rectangle(100, 115, 200, 135, fill="white", outline="white")
    canvas.create_rectangle(100, 115, 200, 120, fill="chartreuse2", outline="white")
    canvas.create_rectangle(100, 120, 200, 125, fill="yellow", outline="white")
    canvas.create_rectangle(100, 125, 200, 135, fill="sienna4", outline="white")
    canvas.create_oval(120, 105, 123, 108, fill="papaya whip")
    canvas.create_oval(130, 100, 133, 103, fill="papaya whip")
    canvas.create_oval(145, 102, 148, 105, fill="papaya whip")
    canvas.create_oval(160, 100, 163, 103, fill="papaya whip")
    canvas.create_oval(170, 105, 173, 108, fill="papaya whip")

def drawIceCream():
    clearCanvas()
    canvas.create_oval(125, 100, 175, 150, fill="lemon chiffon")
    canvas.create_polygon(120, 125, 180, 125, 150, 200, fill='tan')

def drawTooEarly():
    clearCanvas()
    canvas.create_text(150, 100, text="Too early! You fell asleep!", font=("Times New Roman", 20))

def drawTooHot():
    clearCanvas()
    canvas.create_text(150, 100, text="Too hot! You are melting!", font=("Times New Roman", 20))

def clearCanvas():
    canvas.create_rectangle(0, 0, 300, 250, fill="gainsboro", outline="gainsboro")

def leftPressed():
    quiz(True, var.get(), question.get(), clinic.get())

def rightPressed():
    quiz(False, var.get(), question.get(), clinic.get())

def quiz(buttonPressed, choose_icecream, question, clinic):
    if (question == 1):
        if buttonPressed:
            if (choose_icecream == 1):
                drawIceCream()
            else:
                drawCheeseburger()
        else:
            if clinic == 730:
                drawTooEarly()
            else:
                drawTooHot()
    elif (question == 2):
        if not buttonPressed:
            if (choose_icecream == 1):
                drawIceCream()
            else:
                drawCheeseburger()
        else:
            if clinic == 730:
                drawTooEarly()
            else:
                drawTooHot()
    else:
        if buttonPressed:
            if (choose_icecream == 1):
                drawIceCream()
            else:
                drawCheeseburger()
        else:
            if clinic == 730:
                drawTooEarly()
            else:
                drawTooHot()

def displayQuestion1():
    clearCanvas()
    instruction = "Who has won more grand slam tennis titles?"
    left = "Serena Williams"
    right = "Roger Federer"
    buttonInstruction.config(text=instruction)
    buttonLeftChoice.config(text=left)
    buttonRightChoice.config(text=right)

def displayQuestion2():
    clearCanvas()
    instruction = "How many World Cups has USWNT won?"
    left = "3 World Cups"
    right = "4 World Cups"
    buttonInstruction.config(text=instruction)
    buttonLeftChoice.config(text=left)
    buttonRightChoice.config(text=right)

def displayQuestion3():
    clearCanvas()
    instruction = "Who won the last Super Bowl (LIV)?"
    left = "Kansas City Chiefs"
    right = "San Francisco 49ers"
    buttonInstruction.config(text=instruction)
    buttonLeftChoice.config(text=left)
    buttonRightChoice.config(text=right)

buttonInstruction = Button(root,text=instruction)
button1 = Radiobutton(root,text="1", variable=question, value=1, command=displayQuestion1)
button2 = Radiobutton(root,text="2", variable=question, value=2, command=displayQuestion2)
button3 = Radiobutton(root,text='3', variable=question, value=3, command=displayQuestion3)
clinicLeft = Radiobutton(root,text='Clinic Time: 7:30am', variable=clinic, value=730)
clinicRight = Radiobutton(root,text='Clinic Time: 4:30pm', variable=clinic, value=430)
buttonLeftChoice = Button(root, text=left, command=leftPressed)
buttonRightChoice = Button(root, text=right, command=rightPressed)
radioIce = Radiobutton(root, text=ice_cream, variable=var, value=1)
radioCheese = Radiobutton(root, text=cheeseburger, variable=var, value=2)
canvas = Canvas(root, bg="gainsboro", height=250, width=300)

# pack each widget
buttonInstruction.pack()
button1.place(x=490)
button2.place(x=530)
button3.place(x=570)
clinicLeft.place(x=325, y=30)
clinicRight.place(x=500, y=30)
buttonLeftChoice.place(x=50, y=50)
buttonRightChoice.place(x=175, y=50)
radioIce.place(x=325, y=50)
radioCheese.place(x=500, y=50)
canvas.pack(side=BOTTOM, pady=50)
root.mainloop()