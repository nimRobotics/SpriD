from tkinter import *

def hide(x):
    x.pack_forget()

root = Tk()
d=Button(root, text="Click to hide me!")

d.configure(command=lambda: hide(d))
d.pack()
root.mainloop()
