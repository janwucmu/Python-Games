from tkinter import *
from PIL import ImageTk,Image
root = Tk()

resize_size = 40

image1 = Image.open("cat.png")
image2 = Image.open("fox.png")
image3 = Image.open("penguin.png")
image4 = Image.open("pooh.png")
image5 = Image.open("rabbit.png")
image6 = Image.open("sleeping_dog.png")
image7 = Image.open("bunny.png")
image8 = Image.open("elephant.png")
image9 = Image.open("hamster.png")
image10 = Image.open("panda.png")
image11 = Image.open("pikachu.png")
image12 = Image.open("shiba.png")
image13 = Image.open("snail.png")
image14 = Image.open("mickey.png")
image15 = Image.open("chubby_penguin.png")
image16 = Image.open("birdy.png")
image17 = Image.open("ff.png")
image18 = Image.open("llama.png")
image19 = Image.open("pig.png")
image20 = Image.open("unicorn.png")

all_image = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, \
    image11, image12, image13, image14, image15, image16, image17, image18, image19, image20]
all_img = []

def insertLists(mylist):
    mylist.insert(END, "Cat")
    mylist.insert(END, "Fox")
    mylist.insert(END, "Penguin")
    mylist.insert(END, "Pooh")
    mylist.insert(END, "Rabbit")
    mylist.insert(END, "Dog")
    mylist.insert(END, "Bunny")
    mylist.insert(END, "Elephant")
    mylist.insert(END, "Hamster")
    mylist.insert(END, "Panda")
    mylist.insert(END, "Pikachu")
    mylist.insert(END, "Shiba")
    mylist.insert(END, "Snail")
    mylist.insert(END, "Mickey Mouse")
    mylist.insert(END, "Chubby Penguin")
    mylist.insert(END, "Bird")
    mylist.insert(END, "French Fries")
    mylist.insert(END, "Llama")
    mylist.insert(END, "Pig")
    mylist.insert(END, "Unicorn")

# spin box
spin = Spinbox(root, from_=1, to=10)
spin.pack(side=TOP)

def resizing():
    index = int(spin.get())
    if (index == 1):
        return 40
    elif (index == 2):
        return 45
    elif (index == 3):
        return 50
    elif (index == 4):
        return 55
    elif (index == 5):
        return 60
    elif (index == 6):
        return 65
    elif (index == 7):
        return 70
    elif (index == 8):
        return 75
    elif (index == 9):
        return 80
    else:
        return 85

def imageResizing(image, size):
    resized = image.resize((size, size))
    return ImageTk.PhotoImage(resized)

# scroll bar and list box
scrollbar = Scrollbar(root)
mylist = Listbox(root, yscrollcommand=scrollbar.set)
insertLists(mylist)
scrollbar.pack(side = RIGHT, fill = Y)
mylist.pack(side = RIGHT, fill = BOTH)
scrollbar.config(command = mylist.yview)

# canvas
canvas = Canvas(root, bg="white", height=300, width=500, highlightbackground="black", highlightthickness=1)
def clicked(event):
    if (mylist.curselection() != ()):
        resize_size = resizing()
        index = mylist.curselection()[0]
        image = all_image[index]
        all_img.append(imageResizing(image, resize_size))
        canvas.create_image(event.x, event.y, image=all_img[-1], anchor=CENTER)

canvas.bind("<Button-1>", clicked)
canvas.pack(side=LEFT)

root.mainloop()
