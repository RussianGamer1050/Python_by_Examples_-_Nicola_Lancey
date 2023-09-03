from tkinter import *


def add():
    num = int(entry_box.get())
    have = msg["text"]
    have = int(have)
    total = num + have
    msg["text"] = total
    entry_box.delete(0, END)


def clear():
    msg["text"] = 0
    entry_box.delete(0, END)


total = 0

window = Tk()
window.geometry('400x300')

entry_box = Entry()
entry_box.place(x=95, y=90, width=100, height=20)
entry_box['justify'] = 'center'

add_button = Button(text="Add", command=add)
add_button.place(x=205, y=90, width=100, height=20)

msg = Label(text=total)
msg.place(x=50, y=130, width=300, height=25)

reset_button = Button(text="Reset", command=clear)
reset_button.place(x=175, y=170, width=50, height=25)

mainloop()
