# proplem 3
from tkinter import *

window = Tk()

def rdo_change():
    if var.get() == 1:
        label1.configure(text = "Benz")
    else:
        label1.configure(text = " Porsche")
    
var = IntVar()

rdo1 = Radiobutton(window, text="Benz", variable=var, value=1, command=rdo_change)
rdo2 = Radiobutton(window, text="Porsche", variable=var, value=2, command=rdo_change)

label1 = Label(window, text="Your car:", fg = "red")

rdo1.pack()
rdo2.pack()
label1.pack()



window.mainloop()

# proplem 4  LEFT

from tkinter import *

window = Tk()

buttion1 = Button(window, text= "Button1")
buttion2 = Button(window, text= "Button2")
buttion3 = Button(window, text= "Button3")

buttion1.pack(side=LEFT)
buttion2.pack(side=LEFT)
buttion3.pack(side=LEFT)

window.mainloop()

# proplem 4  RIGHT

from tkinter import *

window = Tk()

buttion1 = Button(window, text= "Button1")
buttion2 = Button(window, text= "Button2")
buttion3 = Button(window, text= "Button3")

buttion1.pack(side=RIGHT)
buttion2.pack(side=RIGHT)
buttion3.pack(side=RIGHT)

window.mainloop()

# proplem 4  TOP
from tkinter import *

window = Tk()

buttion1 = Button(window, text= "Button1")
buttion2 = Button(window, text= "Button2")
buttion3 = Button(window, text= "Button3")

buttion1.pack(side=TOP)
buttion2.pack(side=TOP)
buttion3.pack(side=TOP)

window.mainloop()

# proplem 4  BOTTOM
from tkinter import *

window = Tk()

buttion1 = Button(window, text= "Button1")
buttion2 = Button(window, text= "Button2")
buttion3 = Button(window, text= "Button3")

buttion1.pack(side=BOTTOM)
buttion2.pack(side=BOTTOM)
buttion3.pack(side=BOTTOM)

window.mainloop()

# proplem 5

from tkinter import *
from time import *


fnameList = ["byuntear-meme.gif", "crying-dog.gif", "cute-doggo-dance-cute-dog.gif", "dog-doggie.gif", "dog-smirk-dog.gif",
             "dog.gif","dog2.gif", "fgty.gif", "scared-dog.gif", "side-eye.gif"]

photoList = [None]*9
num = 0

def clickNext():
    global num
    num+=1
    if num>8:
        num=0
    photo = PhotoImage(file="image\\"+ fnameList[num])
    pLabel1.configure(image = photo)
    pLabel1.image = photo
    pLabel2.configure(text= fnameList[num], fg= "red")
    pLabel2.place(x=(150+500)/2, y = 10 )

def clickPrev():
    global num
    num+=-1
    if num<0:
        num=8
    photo = PhotoImage(file="image\\" + fnameList[num])
    pLabel1.configure(image = photo)
    pLabel1.image = photo
    pLabel2.configure(text= fnameList[num], fg = "green")
    pLabel2.place(x=(150+500)/2, y = 10 )

window= Tk()
window.geometry("700x500")
window.title("My_Image_List")

btnPrev = Button(window, text="<<Prev", command= clickPrev)
btnNext = Button(window, text = "Next >>", command=clickNext)

photo = PhotoImage(file="image\\" + fnameList[0])
pLabel1 = Label(window, image=photo)
pLabel2 = Label(window,text= fnameList[0], fg= "blue")

btnPrev.place( x=150, y = 10)
btnNext.place( x=500, y = 10)
pLabel1.pack(side = BOTTOM)
pLabel2.place(x=(150+500)/2, y = 10 )

window.mainloop()








