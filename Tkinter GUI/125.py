from tkinter import *
from random import randint


def roll():
    number = randint(1, 6)
    msg = Label(text=number)
    msg.place(x=140, y=100, width=20, height=35)


window = Tk()
window.geometry('300x160')
button = Button(text="Roll", command=roll)
button.place(x=125, y=40, width=50, height=35)

mainloop()
