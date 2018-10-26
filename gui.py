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

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
imageFrame = Frame(window)
imageFrame.pack(side= BOTTOM)


lbl = Label(topFrame, text="Select the spring type you want to design",font=("Arial Bold", 20))
lbl2 = Label(bottomFrame, text="All rights reserved. Indian Institute of Technology Tirupati ",font=("Arial", 8))

# button1 = Button(topFrame, text="Helical Spring", fg = "red")
button1 = Button(topFrame, text="Helical Spring")
button2 = Button(topFrame, text="Belleville Spring")
button3 = Button(topFrame, text="Torsion Spring")
button4 = Button(topFrame, text="Constant Force Spring")

lbl.pack(side=TOP,pady=20)
lbl2.pack()
button1.pack(fill=X,pady=5)
button2.pack(fill=X,pady=5)
button3.pack(fill=X,pady=5)
button4.pack(fill=X,pady=5)

# adding an image
img = ImageTk.PhotoImage(Image.open("spr2_2.png"))
panel = Label(imageFrame, image = img)
panel.pack(side=LEFT)
img2 = ImageTk.PhotoImage(Image.open("spr2_2.png"))
panel2 = Label(imageFrame, image = img2)
panel2.pack(side=LEFT)
img3 = ImageTk.PhotoImage(Image.open("spr2_2.png"))
panel3 = Label(imageFrame, image = img3)
panel3.pack(side=LEFT)
img4 = ImageTk.PhotoImage(Image.open("spr2_2.png"))
panel4 = Label(imageFrame, image = img4)
panel4.pack(side=LEFT)

# adding an image
# img = ImageTk.PhotoImage(Image.open("spr.jpeg"))
# panel = Label(window, image = img)
# panel.grid(column =1 ,row=1)

#Menu
def about_click():
    messagebox.showinfo('About Us', 'This product has been developed by Aakash Yadav and Aditya from IIT Tirupati, India')
# function to create new window # TODO: create the gui for the new window
def create_window():
        top=Toplevel()
        top.title("Helical Spring Design")
        top.geometry('700x400')
        btnn = Button(top,text='DDDDD')
        btnn.grid(column=0,row=0)
# adding a menu
menu = Menu(window)
menu.add_command(label='File')
menu.add_command(label='Save')
menu.add_command(label='About', command=about_click)
# add submenu below three lines
new_item = Menu(menu,tearoff=0)
new_item.add_command(label='New',command=create_window)
# using onclick
# new_item.add_command(label='New', command=clicked)
menu.add_cascade(label='undo', menu=new_item)
window.config(menu=menu)

window.mainloop()
