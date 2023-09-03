from tkinter import *


def create():
    file = open('List.csv', 'w')
    file.write("")
    file.close()


def add():
    name = name_entry_box.get()
    age = age_entry_box.get()
    file = open('List.csv', 'a')
    file.write(name + ", " + age + "\n")
    file.close()
    age_entry_box.delete(0, END)
    name_entry_box.delete(0, END)


window = Tk()
window.geometry('400x225')

create_message = Label(text="Do you want to create a new file?")
create_message.place(x=50, y=20, width=300, height=25)
create_message["justify"] = "center"

create_button = Button(text="Create", command=create)
create_button.place(x=160, y=50, width=80, height=25)

name_msg = Label(text="Name:")
name_msg.place(x=30, y=100, width=50, height=25)

name_entry_box = Entry()
name_entry_box.place(x=80, y=100, width=200, height=25)

age_msg = Label(text="Age:")
age_msg.place(x=29, y=130, width=40, height=25)

age_entry_box = Entry()
age_entry_box.place(x=70, y=130, width=60, height=25)

add_button = Button(text="Add", command=add)
add_button.place(x=165, y=170, width=70, height=25)

mainloop()
