from tkinter import *


def add():
    num = entry_box.get()
    if num.isdigit():
        text_box.insert(END, num)
    entry_box.delete(0, END)


def clear():
    text_box.delete(0, END)


window = Tk()
window.geometry('300x300')

title = Label(text="Enter a number:")
title.place(x=50, y=30, width=200, height=25)
title['justify'] = 'center'

entry_box = Entry()
entry_box.place(x=50, y=60, width=200, height=25)
entry_box['justify'] = 'center'

add_button = Button(text="Add", command=add)
add_button.place(x=70, y=90, width=70, height=25)

clear_button = Button(text="Clear", command=clear)
clear_button.place(x=160, y=90, width=70, height=25)

text_box = Listbox()
text_box.place(x=50, y=140, width=200, height=125)
text_box['justify'] = 'center'

mainloop()
