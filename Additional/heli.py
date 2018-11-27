from tkinter import *
# for using combobox
from tkinter.ttk import *
# for creating messagebox alert
from tkinter import messagebox
# for adding menu
from tkinter import Menu
# for Image
from PIL import ImageTk, Image

# TODO: http://www.java2s.com/Code/Python/GUI-Tk/LayoutsideTOPLEFT.htm

window = Tk()
window.title("Welcome to SpriD")
window.geometry('700x400')

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

headFrame = Frame(window)
toolbar1 = Frame(window)
toolbar2 = Frame(window)
toolbar3 = Frame(window)
calcFrame = Frame(window)
toolbar4 = Frame(window)
toolbar5 = Frame(window)
toolbar6 = Frame(window)
footFrame = Frame(window)

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




window.mainloop()
