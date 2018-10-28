from tkinter import *

root = Tk()

def callback():
    print ("called the callback!")

headFrame = Frame(root)
toolbar1 = Frame(root)
toolbar2 = Frame(root)
toolbar3 = Frame(root)
calcFrame = Frame(root)
toolbar4 = Frame(root)
toolbar5 = Frame(root)
toolbar6 = Frame(root)
footFrame = Frame(root)

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

b = Button(calcFrame, text="Calculate",command=callback)
b.pack()

calcFrame.pack(fill=X)

lbl = Label(toolbar4, text="length", width=6)
lbl.pack(side=LEFT, padx=2, pady=2)

lbl = Label(toolbar4, text="20.28mm", width=6)
lbl.pack(side=LEFT, padx=2, pady=2)

toolbar4.pack(side=BOTTOM)



mainloop()
