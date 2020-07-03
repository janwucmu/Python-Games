from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("675x400")

answer = StringVar()
question = IntVar()

# image #1
image1 = Image.open("key.jpeg")
resized1 = image1.resize((300, 250))
img1 = ImageTk.PhotoImage(resized1)
# image #2
image2 = Image.open("password.jpeg")
resized2 = image2.resize((300, 250))
img2 = ImageTk.PhotoImage(resized2)
# image #3
image3 = Image.open("lightsaber.jpeg")
resized3 = image3.resize((300, 250))
img3 = ImageTk.PhotoImage(resized3)
# image #4
image4 = Image.open("robber.jpeg")
resized4 = image4.resize((300, 250))
img4 = ImageTk.PhotoImage(resized4)
# image #5
image5 = Image.open("hotdog.jpeg")
resized5 = image5.resize((300, 250))
img5 = ImageTk.PhotoImage(resized5)
# image #6
image6 = Image.open("circus.jpeg")
resized6 = image6.resize((300, 250))
img6 = ImageTk.PhotoImage(resized6)

def clearCanvas():
    canvas.create_rectangle(0, 0, 300, 250, fill="gainsboro", outline="gainsboro")
def right():
    canvas.create_rectangle(0, 0, 300, 250, fill="green", outline="green")
def wrong():
    canvas.create_rectangle(0, 0, 300, 250, fill="red", outline="red")

def game():
    q = question.get()
    ans = answer.get()
    if (q == 1):
        if (ans == "key"):
            right()
        else:
            wrong()
            canvas.create_text(150, 100, text="key", font=("Times New Roman", 20))
    elif (q == 2):
        if (ans == "password"):
            right()
        else:
            wrong()
            canvas.create_text(150, 100, text="password", font=("Times New Roman", 20))
    elif (q == 3):
        if (ans == "lightsaber"):
            right()
        else:
            wrong()
            canvas.create_text(150, 100, text="lightsaber", font=("Times New Roman", 20))
    elif (q == 4):
        if (ans == "robber" or ans == "thief"):
            right()
        else:
            wrong()
            canvas.create_text(150, 100, text="robber or thief", font=("Times New Roman", 20))
    elif (q == 5):
        if (ans == "hotdog" or ans == "hot dog"):
            right()
        else:
            wrong()
            canvas.create_text(150, 100, text="hotdog or hot dog", font=("Times New Roman", 20))
    else:
        if (ans == "circus"):
            right()
        else:
            wrong()
            canvas.create_text(150, 100, text="circus", font=("Times New Roman", 20))

def draw1():
    clearCanvas()
    canvas.create_image(0, 0, image=img1, anchor=NW)
def draw2():
    clearCanvas()
    canvas.create_image(0, 0, image=img2, anchor=NW)
def draw3():
    clearCanvas()
    canvas.create_image(0, 0, image=img3, anchor=NW)
def draw4():
    clearCanvas()
    canvas.create_image(0, 0, image=img4, anchor=NW)
def draw5():
    clearCanvas()
    canvas.create_image(0, 0, image=img5, anchor=NW)
def draw6():
    clearCanvas()
    canvas.create_image(0, 0, image=img6, anchor=NW)

# initializing Tkinter widgets 
buttonInstruction = Button(root,text="Enter", command=game)
button1 = Radiobutton(root,text="1", variable=question, value=1, command=draw1)
button2 = Radiobutton(root,text="2", variable=question, value=2, command=draw2)
button3 = Radiobutton(root,text='3', variable=question, value=3, command=draw3)
button4 = Radiobutton(root,text='4', variable=question, value=4, command=draw4)
button5 = Radiobutton(root,text='5', variable=question, value=5, command=draw5)
button6 = Radiobutton(root,text='6', variable=question, value=6, command=draw6)
usernameLabel = Label(root, text="What is it?")
entry = Entry(root, bd=5, textvariable=answer)
canvas = Canvas(root, bg="gainsboro", height=250, width=300)

# pack each widget
buttonInstruction.place(x=430)
button1.place(x=490)
button2.place(x=530)
button3.place(x=570)
button4.place(x=490, y=20)
button5.place(x=530, y=20)
button6.place(x=570, y=20)
usernameLabel.place(x=150)
entry.place(x=230)
canvas.pack(side=BOTTOM, pady=50)
root.mainloop()