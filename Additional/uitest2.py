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
window.title("Welcome to Aakash Yadav's app")
window.geometry('350x200')


# panel.pack(side = "bottom", fill = "both", expand = "yes")



lbl = Label(window, text="Enter your name:")
#lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
# for disabling use -  txt = Entry(window,width=10, state='disabled')
txt.grid(column=1, row=0)
#to set the cursor to this field when the program starts txt.focus()

# onclick type function for button
def clicked():
    #lbl.configure(text="Button was clicked !!")
    res = "Welcome \n to" + txt.get()
    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked)
# btn = Button(window, text="Click Me")
# btn = Button(window, text="Click Me", bg="orange", fg="red")
btn.grid(column=0, row=2)

# using combobox i.e drop down menu
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=3)

# using checkbox
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
# changing state of check box
# chk_state.set(0) #uncheck
# chk_state.set(1) #check
chk.grid(column=0, row=4)

rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=5)
rad2.grid(column=1, row=5)
rad3.grid(column=2, row=5)

# rad1 = Radiobutton(window,text='First', value=1, command=clicked)
# def clicked():
#       # Do what you need

# Create a pop up dialoguebox
def clicked2():
    messagebox.showinfo('Message title', 'Message content')
btn2 = Button(window,text='Create dialoguebox', command=clicked2)
btn2.grid(column=0,row=6)

# spinbox
spin = Spinbox(window, from_=0, to=100, width=5)
# show particular property
# spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0,row=7)
#set default value for spinbox
# var =IntVar()
# var.set(36)
# spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)

# message box for About
def about_click():
    messagebox.showinfo('About Us', 'This product has been developed by Aakash Yadav and Aditya from IIT Tirupati, India')

# function to create new window # TODO: cv
def create_window():
        top=Toplevel()
        top.title("Helical Spring Design")
        top.geometry('350x200')
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
