from tkinter import *


def hello():
    name = name_entry_box.get()
    hello_msg = "Hello " + name
    hello_text_box["text"] = hello_msg
    name_entry_box.delete(0, END)


window = Tk()
window.geometry("500x400")
window.wm_iconbitmap('Icon.ico')
window.configure(background='gray')

logo = PhotoImage(file='Logo.gif')
logo_image = Label(image=logo)
logo_image.place(x=100, y=50, width=200, height=150)

text_msg = Label(text="Enter your name:")
text_msg.place(x=20, y=250, width=200, height=25)
text_msg.configure(background='gray')

name_entry_box = Entry()
name_entry_box.place(x=180, y=250, width=200, height=25)

hello_button = Button(text="Press me", command=hello)
hello_button.place(x=60, y=300, width=80, height=25)
hello_button["justify"] = 'center'

hello_text_box = Label()
hello_text_box.place(x=150, y=300, width=280, height=25)
hello_text_box['justify'] = 'center'

mainloop()
