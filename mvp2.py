# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

from tkinter import *
# for using combobox
from tkinter.ttk import *
# for creating messagebox alert
from tkinter import messagebox
# for adding menu
from tkinter import Menu
# for Image
from PIL import ImageTk, Image

window = Tk()
window.title("Welcome to SpriD")
window.geometry('700x400')

# function to create new window # TODO: cv
def create_window():
        top=Toplevel()
        top.title("Helical Spring Design")
        top.geometry('700x400')
        btnn = Button(top,text='DDDDD')
        btnn.grid(column=0,row=0)

lbl = Label(window, text="Enter your name:")
#lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=1)

a = Button(text="Center Button")
d = Button(text="Center Button")

e = Button(text="Center Button")
f = Button(text="Center Button")

b = Button(text="Top Left Button")
c = Button(text="Bottom Right Button")
# https://stackoverflow.com/questions/31128780/tkinter-how-to-make-a-button-center-itself
a.place(relx=0.1, rely=0.1, anchor=CENTER)
d.place(relx=0.4, rely=0.1, anchor=CENTER)
# e.place(relx=0.0, rely=1.0, anchor=CENTER)
# b.place(relx=0.0, rely=0.0, anchor=NW)
# f.place(relx=0.0, rely=0.0, anchor=NW)
# c.place(relx=1.0, rely=1.0, anchor=SE)

w = Label(window, text="Red Sun", bg="red", fg="white")
w.pack(fill=X,padx=10)
w = Label(window, text="Green Grass", bg="green", fg="black")
w.pack(fill=X,padx=10)
w = Label(window, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X,padx=10)

# adding an image
# img = ImageTk.PhotoImage(Image.open("spr.jpeg"))
# panel = Label(window, image = img)
# panel.grid(column =1 ,row=1)

# adding a menu
menu = Menu(window)
menu.add_command(label='File')
menu.add_command(label='Save')
menu.add_command(label='About')
# add submenu below three lines
new_item = Menu(menu,tearoff=0)
new_item.add_command(label='New',command=create_window)
# using onclick
# new_item.add_command(label='New', command=clicked)
menu.add_cascade(label='undo', menu=new_item)
window.config(menu=menu)

window.mainloop()
