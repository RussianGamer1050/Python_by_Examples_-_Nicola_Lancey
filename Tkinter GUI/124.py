from tkinter import *


def action():
    name = entry_box.get()
    hello = 'Hello ' + name
    msg1 = Label(text=hello)
    msg1['bg'] = 'black'
    msg1['fg'] = 'white'
    msg1.place(x=200, y=170, width=200, height=20)


window = Tk()
window.geometry('600x300')
msg = Label(text="Enter your name:")
msg.place(x=200, y=110, width=200, height=20)
msg['justify'] = 'center'

entry_box = Entry()
entry_box.place(x=200, y=130, width=200, height=20)

button = Button(text="Button", command=action)
button.place(x=250, y=150, width=100, height=20)

window.mainloop()
