# https://stackoverflow.com/questions/34611100/is-it-possible-to-keep-the-same-window-for-every-class-in-pythons-tkinter

from tkinter import *


class Window1:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master
        master.title("Welcome to Aakash")
        master.geometry('350x200')
        btn = Button(self.master, text="Click Me")
        # btn = Button(window, text="Click Me")
        # btn = Button(window, text="Click Me", bg="orange", fg="red")
        btn.pack()
        self.label = Button(self.master, text="Example", command=self.load_new)
        self.label.pack()

    def load_new(self):
        self.label.destroy()

        # use `root` with another class
        self.another = Window2(self.master)


class Window2:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Example")
        self.label.pack()


root = Tk()
run = Window1(root)
root.mainloop()
