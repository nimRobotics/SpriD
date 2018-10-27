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

def calculate():
    #sorted array
    x = [1.1,2,3,4,5,6]
    y = [2.2,4,6,8,10,12]
    t = float(txt.get())
    i= x.index(t)
    print(i)
    # res = float(txt.get())+float(txt2.get())
    lbl.configure(text= y(i))

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

lbl = Label(topFrame, text="Give the input to the params below",font=("Arial Bold", 20))
lbl2 = Label(bottomFrame, text="All rights reserved. Indian Institute of Technology Tirupati ",font=("Arial", 8))
# button1 = Button(topFrame, text="Helical Spring", fg = "red")
button1 = Button(topFrame, text="Calculate", command=calculate)
txt = Entry(topFrame,width=10)
txt2 = Entry(topFrame,width=10)

lbl.pack(side=TOP,pady=20)
lbl2.pack()
button1.pack(fill=X,pady=5)
txt.pack()
txt2.pack()







window.mainloop()
