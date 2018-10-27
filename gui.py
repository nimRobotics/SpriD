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

# _____________________________ DEFINITIONS________________________________________________________________
def about_click():
    messagebox.showinfo('About Us', 'This product has been developed by Aakash Yadav and Aditya from IIT Tirupati, India')
# function to create new window # TODO: HELICAL SPRING  ******************************************
def create_window():
        top=Toplevel()
        top.title("Helical Spring Design")
        top.geometry('700x400')
        # adding a menu
        menu = Menu(top)
        # add submenu below three lines
        new_item = Menu(menu,tearoff=0)
        new_item.add_command(label='New',command=create_window)
        new_item.add_command(label='Exit', command=top.quit)
        new_item2 = Menu(menu,tearoff=0)
        new_item2.add_command(label='Helical',command=create_window)
        new_item2.add_command(label='Belleville', command=create_window_2)
        new_item2.add_command(label='Torsion')
        new_item2.add_command(label='Constant Force')
        menu.add_cascade(label='File',menu=new_item)
        menu.add_cascade(label='Start', menu=new_item2)
        menu.add_command(label='Save')
        menu.add_command(label='About', command=about_click)
        menu.add_command(label='Help')
        top.config(menu=menu)

        topFrame = Frame(top)
        topFrame.pack()
        bottomFrame = Frame(top)
        bottomFrame.pack(side=BOTTOM)

        lbl = Label(topFrame, text="Aakash Yadav",font=("Arial Bold", 20))
        lbl2 = Label(bottomFrame, text="Aakash Yadav",font=("Arial Bold", 20))

        lbl.pack()
        lbl2.pack(side=LEFT)
# function to create new window # TODO: Belleville SPRING  ******************************************
def create_window_2():
        top=Toplevel()
        top.title("Helical Spring Design")
        top.geometry('700x400')
        btn = Button(top,text='BellevilleSpring')
        btn.grid(column=0,row=0)
        menu = Menu(top)
        # add submenu below three lines
        new_item = Menu(menu,tearoff=0)
        new_item.add_command(label='New',command=create_window)
        new_item.add_command(label='Exit', command=top.quit)
        new_item2 = Menu(menu,tearoff=0)
        new_item2.add_command(label='Helical',command=create_window)
        new_item2.add_command(label='Belleville', command=create_window_2)
        new_item2.add_command(label='Torsion')
        new_item2.add_command(label='Constant Force')
        menu.add_cascade(label='File',menu=new_item)
        menu.add_cascade(label='Start', menu=new_item2)
        menu.add_command(label='Save')
        menu.add_command(label='About', command=about_click)
        menu.add_command(label='Help')
        top.config(menu=menu)
# function to create new window # TODO: ABOUT US  ******************************************
def create_window_about():

        top=Toplevel()
        top.title("About Us ")
        top.geometry('700x400')

        menu = Menu(top)
        # add submenu below three lines
        new_item = Menu(menu,tearoff=0)
        new_item.add_command(label='New',command=create_window)
        new_item.add_command(label='Exit', command=top.quit)
        new_item2 = Menu(menu,tearoff=0)
        new_item2.add_command(label='Helical',command=create_window)
        new_item2.add_command(label='Belleville', command=create_window_2)
        new_item2.add_command(label='Torsion')
        new_item2.add_command(label='Constant Force')
        menu.add_cascade(label='File',menu=new_item)
        menu.add_cascade(label='Start', menu=new_item2)
        menu.add_command(label='Save')
        menu.add_command(label='About', command=about_click)
        menu.add_command(label='Help')
        top.config(menu=menu)

        topFrame = Frame(top)
        topFrame.pack()
        # bottomFrame = Frame(top)
        # bottomFrame.pack(side=BOTTOM)
        img = ImageTk.PhotoImage(Image.open("spr2_2.png"))
        panel = Label(topFrame, image = img)
        panel.pack()
        lbl = Label(topFrame, text="Aakash Yadav",font=("Arial Bold", 20))
        lbl.pack(side=LEFT)
#*****************************************************************************************************************************

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
imageFrame = Frame(window)
imageFrame.pack(side= BOTTOM)


lbl = Label(topFrame, text="Select the spring type you want to design",font=("Arial Bold", 20))
lbl2 = Label(bottomFrame, text="All rights reserved. Indian Institute of Technology Tirupati ",font=("Arial", 8))
# button1 = Button(topFrame, text="Helical Spring", fg = "red")
button1 = Button(topFrame, text="Helical Spring", command=create_window)
button2 = Button(topFrame, text="Belleville Spring", command=create_window_2)
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

# adding a menu
menu = Menu(window)
# add submenu below three lines
new_item = Menu(menu,tearoff=0)
new_item.add_command(label='New',command=create_window)
new_item.add_command(label='Exit', command=window.quit)
new_item2 = Menu(menu,tearoff=0)
new_item2.add_command(label='Helical',command=create_window)
new_item2.add_command(label='Belleville', command=create_window_2)
new_item2.add_command(label='Torsion')
new_item2.add_command(label='Constant Force')
menu.add_cascade(label='File',menu=new_item)
menu.add_cascade(label='Start', menu=new_item2)
menu.add_command(label='Save')
menu.add_command(label='About', command=create_window_about)
menu.add_command(label='Help')
window.config(menu=menu)


window.mainloop()
