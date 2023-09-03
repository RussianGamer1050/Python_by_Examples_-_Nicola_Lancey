from tkinter import *


def kilometre():
    num = int(entry_box.get())
    answer = num * 1.6093
    msg["text"] = answer


def mile():
    num = int(entry_box.get())
    answer = num * 0.6214
    msg["text"] = answer


window = Tk()
window.geometry('300x250')
window.title("Converter")

title = Label(text="Enter a number:")
title.place(x=50, y=50, width=200, height=25)
title['justify'] = 'center'

entry_box = Entry()
entry_box.place(x=75, y=80, width=150, height=25)
entry_box['justify'] = 'center'

kilometre_button = Button(text="To Kilometres", command=kilometre)
kilometre_button.place(x=35, y=110, width=110, height=25)

mile_button = Button(text="To Miles", command=mile)
mile_button.place(x=150, y=110, width=110, height=25)

msg = Label(text="")
msg.place(x=75, y=140, width=150, height=25)
msg['justify'] = 'center'

mainloop()
