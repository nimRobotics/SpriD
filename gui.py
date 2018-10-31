from tkinter import *
# for using combobox
from tkinter.ttk import *
# for creating messagebox alert
from tkinter import messagebox
# for adding menu
from tkinter import Menu
# for Image
from PIL import ImageTk, Image
# for hyperlinks
import webbrowser

window = Tk()
window.title("Welcome to SpriD")
window.geometry('700x400')

# _____________________________ DEFINITIONS________________________________________________________________
def interplt(x,y,a):
    if a in x:
        i=x.index(a)
        lbl1.configure(text= y[i])
        # return y[i]
    else:
        for j in range(len(x)):
            if(a<x[j]):
               x1=x[j-1]
               x2=x[j]
               y1=y[j-1]
               y2=y[j]
               m=(y2-y1)/(x2-x1)
               c=m*(a-x1)+y1
               lbl1.configure(text= c)
               # return c
x = [1,2,3,4,5]
y = [2,4,6,8,10]
# button1 = Button(topFrame, text="Calculate", command=lambda: interplt(x,y,float(txt1.get())))
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

        headFrame = Frame(top)
        toolbar1 = Frame(top)
        toolbar2 = Frame(top)
        toolbar3 = Frame(top)
        calcFrame = Frame(top)
        toolbar4 = Frame(top)
        toolbar5 = Frame(top)
        toolbar6 = Frame(top)
        footFrame = Frame(top)

        lbl = Label(headFrame, text="Input the given params",font=("Arial B",14))
        lbl.pack(padx=2, pady=2)

        headFrame.pack(side=TOP, fill=X, padx=4 )

        lbl = Label(toolbar1, text="open", width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        txt = Entry(toolbar1,width=10)
        txt.pack(side=LEFT, padx=2, pady=2)

        lbl = Label(toolbar1, text="m/s^2",font=("Arial B", 10), width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        lbl = Label(toolbar1, text="open", width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        txt = Entry(toolbar1,width=10)
        txt.pack(side=LEFT, padx=2, pady=2)

        lbl = Label(toolbar1, text="m/s^2",font=("Arial B", 10), width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        toolbar1.pack(fill=X, padx=4 )

        lbl = Label(toolbar2, text="open", width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        txt = Entry(toolbar2,width=10)
        txt.pack(side=LEFT, padx=2, pady=2)

        lbl = Label(toolbar2, text="MPa",font=("Arial B", 10), width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        toolbar2.pack(fill=X, padx=4)

        lbl = Label(toolbar3, text="open", width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        txt = Entry(toolbar3,width=10)
        txt.pack(side=LEFT, padx=2, pady=2)

        lbl = Label(toolbar3, text="MPa",font=("Arial B", 10), width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        toolbar3.pack(fill=X, padx=4)

        b = Button(calcFrame, text="Calculate")
        b.pack()

        calcFrame.pack(fill=X)

        lbl = Label(toolbar4, text="length", width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        lbl = Label(toolbar4, text="20.28mm", width=6)
        lbl.pack(side=LEFT, padx=2, pady=2)

        toolbar4.pack(side=BOTTOM)
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

        aakFrame = Frame(top)
        aadFrame = Frame(top)

        lbl = Label(aakFrame, text="Aakash Yadav", font=("Arial B", 16))
        lbl.pack(padx=2, pady=2)

        lbl = Label(aakFrame, wraplength = 600 , font=("Arial", 10),text="He is a budding mechanical engineer and is currently pursuing the same at Indian Institute of Technology Tirupati. He belives that consumer experience is most important pillar in developement of as product")
        lbl.pack(padx=2, pady=2)

        aakFrame.pack()
        # TODO: add web hyperlink http://effbot.org/zone/tkinter-text-hyperlink.htm
        # text.insert(INSERT, "this is a ")
        # text.insert(INSERT, "link", hyperlink.add(click1))
        # text.insert(INSERT, "\n\n")

        lbl = Label(aadFrame, text="Aditya Kumar Choudhary", font=("Arial B", 16))
        lbl.pack(padx=2, pady=2)

        lbl = Label(aadFrame, wraplength = 600, font=("Arial", 10), text="He is a budding mechanical engineer and is currently pursuing the same at Indian Institute of Technology Tirupati")
        lbl.pack(padx=2, pady=2)
        # TODO: add Image
        # img = ImageTk.PhotoImage(Image.open("spr2_2.png"))
        # panel = Label(toolbar1, image = img)
        # panel.pack(side=LEFT)
        aadFrame.pack()


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
