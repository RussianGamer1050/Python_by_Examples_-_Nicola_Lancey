from tkinter import *


def add():
    name = entry_box.get()
    msg.insert(END, name)
    entry_box.delete(0, END)


def clear():
    msg.delete(0, END)
    entry_box.delete(0, END)


window = Tk()
window.geometry('400x300')

entry_box = Entry()
entry_box.place(x=95, y=40, width=150, height=20)
entry_box['justify'] = 'center'

add_button = Button(text="Add", command=add)
add_button.place(x=250, y=30, width=60, height=20)

msg = Listbox()
msg.place(x=60, y=90, width=280, height=200)
msg['justify'] = 'center'

reset_button = Button(text="Reset", command=clear)
reset_button.place(x=250, y=55, width=60, height=25)

mainloop()
