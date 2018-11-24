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
# timestamp
import time
import datetime
from tkinter import *
from tkinter import ttk
# for using combobox
from tkinter.ttk import *
# for creating messagebox alert
from tkinter import messagebox
# for adding menu
from tkinter import Menu
# for Image
from PIL import ImageTk, Image
# add hyperlinks
import webbrowser
# timestamp
import time
import datetime

window = Tk()
window.title("Welcome to SpriD")
window.geometry('700x450')

# Radiobutton variable
var = IntVar()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^from brain ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
pi = 3.14159265;
# material = [m, A(kpsi), E(mpsi), G(mpsi), density(ld/inch^3), relative cost]
A228 = [0.145, 201, 29.5, 12, 0.284, 2.6]
# TODO: pg 510 diameter dependency
A229 = [0.147, 147, 30, 11.5, 0.284, 1.3]
A227 = [0.190, 140, 28.8, 11.7, 0.284, 1.0]
A232 = [0.168, 169, 29.5, 11.2, 0.284, 3.1]
A401 = [0.108, 202, 29.5, 11.2, 0.284, 4]

# _____________________________ DEFINITIONS for interpolation________________________________________________________________
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
        top.geometry('700x450')
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   DESIGN.py DEFINITIONS
        def calcMain():
            # def calcMain(fmax, ymax, freelength, solidlength, material, endCondition):
            # if inout in si
            if var.get()==2:
                fmax=float(txt_fmax.get())/4.44822
                ymax=float(txt_ymax.get())/25.4
                freelength=float(txt_freelength.get())/25.4
                solidlength=float(txt_solidlength.get())/25.4
            # if input in US
            if var.get()==1:
                fmax=float(txt_fmax.get())
                ymax=float(txt_ymax.get())
                freelength=float(txt_freelength.get())
                solidlength=float(txt_solidlength.get())
            #initial guess for 'd'
            d=0.001
            counter = 0
            while d>0:
                # factor of safety # TODO: take input
                ns = 1.2;
                # fixed pg510
                zeta = 0.15
                #for fom
                gama = 1;
                #for music wire
                ## TODO: reduce size
                material=combo_mat.get();
                if material=='A228':
                    if d <0.033:
                        E=29.5*1000000
                        G=12*1000000
                    elif d >= 0.033 and d<=0.063:
                        E=29*1000000
                        G=11.85*1000000
                    elif d > 0.063 and d<=0.125:
                        E=28.5*1000000
                        G=11.75*1000000
                    elif d > 0.125:
                        E=28*1000000
                        G=11.6*1000000
                    A=A228[1]*1000
                    m=A228[0]
                    # E=A228[2]*1000000
                    # G=A228[3]*1000000
                    rc=A228[5]
                if material=='A229':
                    if d <0.033:
                        E=28.8*1000000
                        G=11.7*1000000
                    elif d >= 0.033 and d<=0.063:
                        E=28.7*1000000
                        G=11.6*1000000
                    elif d > 0.063 and d<=0.125:
                        E=28.6*1000000
                        G=11.5*1000000
                    elif d > 0.125:
                        E=28.5*1000000
                        G=11.4*1000000
                    A=A229[1]*1000
                    m=A229[0]
                    # E=A229[2]*1000000
                    # G=A229[3]*1000000
                    rc=A229[5]
                if material=='A227':
                    A=A227[1]*1000
                    m=A227[0]
                    E=A227[2]*1000000
                    G=A227[3]*1000000
                    rc=A227[5]
                if material=='A232':
                    A=A232[1]*1000
                    m=A232[0]
                    E=A232[2]*1000000
                    G=A232[3]*1000000
                    rc=A232[5]
                if material=='A401':
                    A=A401[1]*1000
                    m=A401[0]
                    E=A401[2]*1000000
                    G=A401[3]*1000000
                    rc=A401[5]
                # A = 201000 ;
                # relative cost for mausc wire
                # rc = 2.6;
                # kpsi inch
                # m = 0.145;
                #E = 28.5;
                # G = 11750000;
                sut = A/(d**m);
                ssy = 0.45*sut;
                alpha = ssy/ns;
                beta = (8*(1+zeta)*fmax)/(pi*(d**2));
                C = (2*alpha-beta)/(4*beta) + (((2*alpha-beta)/(4*beta))**2 - (3*alpha)/(4*beta))**(0.5);
                D = d*C;
                # kb = (4*C+ 2)/(4*C - 3);
                # taus = (kb*8*(1+zeta)*fmax*D)/(3.147*(d^3));
                # OD = D+d;
                Na = (G*(d**4)*ymax)/(8*(D**3)*fmax);
                # checking end condition
                combo_end['values']= ('Plain','Plain-Ground','Square-Closed','Square-Ground')

                endCondition=combo_end.get()
                if endCondition=='Plain':
                    Nt=Na
                    ls = d*(Nt+1)
                if endCondition=='Plain-Ground':
                    Nt=Na+1
                    ls = d*Nt
                if endCondition=='Square-Closed':
                    Nt=Na+2
                    ls = d*(Nt+1)
                if endCondition=='Square-Ground':
                    Nt=Na+2
                    ls = d*Nt

                lo = ls + (1+zeta)*ymax;
                fom = -rc*gama*(pi**2)*(d**2)*Nt*D*0.25;

                if isinstance(C, complex) or isinstance(Na, complex) or isinstance(ls, complex) or isinstance(lo, complex):
                    print('complex values')
                elif (C >= 4 and C <= 12 and Na >= 3 and Na <= 15 and ls < solidlength and lo < freelength):
                    # break
                    # return D, d, Na, ls, lo, fom
                    if counter==0:
                        if var.get()==2:
                            xD=D*25.4
                            xd=d*25.4
                            xls=ls*25.4
                            xlo=lo*25.4
                        if var.get()==1:
                            xD=D
                            xd=d
                            xls=ls
                            xlo=lo
                            # fmax=float(txt_fmax.get())
                            # ymax=float(txt_ymax.get())
                            # freelength=float(txt_freelength.get())
                            # solidlength=float(txt_solidlength.get())
                        # xD=D
                        # xd=d
                        xNa=Na
                        # xls=ls
                        # xlo=lo
                        xfom=fom
                    counter=counter+1
                    f=open("res.txt", "a+")
                    f.write("Wire diameter %f\r\n" % d)
                    f.write("Spring diameter %f\r\n" % D)
                    f.write("Na %f\r\n" % Na)
                    f.write("ls %f\r\n" % ls)
                    f.write("lo %f\r\n" % lo)
                    f.write("Figure of merit %f\r\n" % fom)
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    f.write("____________"+st+"_____________\n")
                    f.close()
                elif d>1:
                    print("iteration stopped")
                    # messagebox.showinfo("Sorry! couldn't design the spring\nTIP:try different input")
                    break
                d = d+0.001;
            # print(xD, xd, xNa, xls, xlo, xfom)
            if var.get()==2:
                res = "Spring diameter " + str(xD) + "mm\nWire diameter "+str(xd)+"mm\nNa "+str(xNa)+"\nls "+str(xls)+"mm\nlo "+str(xlo)+"mm\nFigure of merit "+str(xfom)
            if var.get()==1:
                res = "Spring diameter " + str(xD) + "inch\nWire diameter "+str(xd)+"inch\nNa "+str(xNa)+"\nls "+str(xls)+"inch\nlo "+str(xlo)+"inch\nFigure of merit "+str(xfom)

            # res = "Spring diameter " + str(xD) + "\nWire diameter "+str(xd)+"\nNa "+str(xNa)+"\nls "+str(xls)+"\nlo "+str(xlo)+"\nFigure of merit "+str(xfom)
            lbl_res.configure(text= res)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^from brain ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        def callback(event):
            webbrowser.open_new(r"file://file/home/aakash/DME/res.txt")
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ radio units
        def rad_si():
            lbl_ut_fmx.configure(text="N")
            lbl_ut_ymx.configure(text="mm")
            lbl_ut_freelen.configure(text="mm")
            lbl_ut_solidlen.configure(text="mm")

        def rad_us():
            lbl_ut_fmx.configure(text="lbf")
            lbl_ut_ymx.configure(text="inch")
            lbl_ut_freelen.configure(text="inch")
            lbl_ut_solidlen.configure(text="inch")



        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ radio units
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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

        note = ttk.Notebook(top)
        tab1 = ttk.Frame(note)


        headFrame = Frame(tab1)
        toolbar1 = Frame(tab1)
        toolbar2 = Frame(tab1)
        toolbar3 = Frame(tab1)
        toolbar4 = Frame(tab1)
        calcFrame = Frame(tab1)
        toolbar5 = Frame(tab1)
        toolbar6 = Frame(tab1)
        toolbar7 = Frame(tab1)
        footFrame = Frame(tab1)

        lbl = Label(headFrame, text="Input the given params",font=("Arial B",14))
        lbl.pack(padx=2, pady=2)

        headFrame.pack(side=TOP, fill=X, padx=4 , pady=20)

        lbl = Label(toolbar1, text="Maximum force", width=15)
        lbl.pack(side=LEFT, padx=2, pady=2)

        txt_fmax = Entry(toolbar1,width=10)
        txt_fmax.pack(side=LEFT, padx=2, pady=2)
        txt_fmax.focus()

        lbl_ut_fmx = Label(toolbar1, text="",font=("Arial B", 10), width=6)
        lbl_ut_fmx.pack(side=LEFT, padx=2, pady=2)

        lbl = Label(toolbar1, text="ymax", width=15)
        lbl.pack(side=LEFT, padx=2, pady=2)

        txt_ymax = Entry(toolbar1,width=10)
        txt_ymax.pack(side=LEFT, padx=2, pady=2)

        lbl_ut_ymx = Label(toolbar1, text="",font=("Arial B", 10), width=6)
        lbl_ut_ymx.pack(side=LEFT, padx=2, pady=2)

        toolbar1.pack(fill=X, padx=70 )

        lbl = Label(toolbar2, text="Free Length", width=15)
        lbl.pack(side=LEFT, padx=2, pady=2)

        txt_freelength = Entry(toolbar2,width=10)
        txt_freelength.pack(side=LEFT, padx=2, pady=2)

        lbl_ut_freelen = Label(toolbar2, text="",font=("Arial B", 10), width=6)
        lbl_ut_freelen.pack(side=LEFT, padx=2, pady=2)

        lbl = Label(toolbar2, text="End condition", width=15)
        lbl.pack(side=LEFT, padx=2, pady=2)

        # txt = Entry(toolbar2,width=10)
        # txt.pack(side=LEFT, padx=2, pady=2)
        combo_end = Combobox(toolbar2,width=10)
        combo_end['values']= ('Plain','Plain-Ground','Square-Closed','Square-Ground')
        combo_end.current(1) #set the selected item
        combo_end.pack(side=LEFT, padx=2, pady=2)

        # lbl = Label(toolbar2, text="m/s^2",font=("Arial B", 10), width=6)
        # lbl.pack(side=LEFT, padx=2, pady=2)

        toolbar2.pack(fill=X, padx=70)

        lbl = Label(toolbar3, text="Solid Length", width=15)
        lbl.pack(side=LEFT, padx=2, pady=2)

        txt_solidlength = Entry(toolbar3,width=10)
        txt_solidlength.pack(side=LEFT, padx=2, pady=2)

        lbl_ut_solidlen = Label(toolbar3, text="",font=("Arial B", 10), width=6)
        lbl_ut_solidlen.pack(side=LEFT, padx=2, pady=2)

        lbl = Label(toolbar3, text="Material", width=15)
        lbl.pack(side=LEFT, padx=2, pady=2)

        combo_mat = Combobox(toolbar3,width=5)
        combo_mat['values']= ('A227','A228','A229','A232','A401')
        combo_mat.current(1) #set the selected item
        combo_mat.pack(side=LEFT, padx=2, pady=2)

        toolbar3.pack(fill=X, padx=70)

        lbl = Label(toolbar4, text="Output Units", width=15)
        lbl.pack(side=LEFT, padx=2, pady=2)

        rad1 = Radiobutton(toolbar4,text='US', value=1, variable=var, command=rad_us)
        rad1.pack(side=LEFT, padx=2, pady=2)

        rad2 = Radiobutton(toolbar4,text='SI', value=2, variable=var, command=rad_si)
        rad2.pack(side=LEFT, padx=2, pady=2)

        toolbar4.pack(fill=X, padx=70)

        b = Button(calcFrame, text="Calculate",command=calcMain)
        b.pack()
        calcFrame.pack(fill=X, pady=20)

        lbl = Label(toolbar5, text="Results", width=6,font=("Calibri",10))
        lbl.pack(padx=2, pady=2)

        link = Label(toolbar5, text="(more)", cursor="hand2")
        link.pack()
        link.bind("<Button-1>",callback)

        lbl_res = Label(toolbar5, text="", width=40)
        lbl_res.pack(padx=2, pady=2)

        toolbar5.pack(side=BOTTOM)


        note.add(tab1, text = "Spring design for Static load",compound=TOP)
        tab2 = ttk.Frame(note)
        lbl = Label(tab2, text="gf")
        lbl.pack(side = BOTTOM)
        note.add(tab2, text = "Spring design for Dynamic load")
        note.pack()
# function to create new window # TODO: Belleville SPRING  ******************************************
def create_window_2():
        top=Toplevel()
        top.title("SpriD")
        top.geometry('700x450')
        lbl = Label(top, text="Come back soon !",font=("Arial Bold", 30))
        # button1.pack(fill=X,pady=5)
        lbl.grid(column=0,row=0, padx = 160, pady = 120)
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
        top.geometry('700x450')

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
        imageAak = Frame(top)
        aadFrame = Frame(top)

        lbl = Label(aakFrame, text="Mr. Aakash Yadav", font=("Arial B", 16))
        lbl.pack(padx=2, pady=2)

        lbl = Label(aakFrame, wraplength = 600 , font=("Arial", 12),text="He is a tech enthusiast and is associated with app development (UI/UX), IoT, Robotics to name a few. He is currently pursuing Mechanical Engineering at Indian Institute of Technology Tirupati. He belives that consumer experience is most important pillar in developement of a product")
        lbl.pack(padx=2, pady=2)
        aakFrame.pack()

        # TODO: add Image
        img = ImageTk.PhotoImage(Image.open("spr2_2.png"))
        panel = Label(imageAak, image = img)
        panel.pack()
        imageAak.pack()

        lbl = Label(aadFrame, text="Mr. Aditya Kumar Choudhary", font=("Arial B", 16))
        lbl.pack(padx=2, pady=2)

        lbl = Label(aadFrame, wraplength = 600 , font=("Arial", 12),text="He is currently pursuing B.Tech in Mechanical engineering from IIT Tirupati. He is very interested in physics and specially in mechanics. He is also a gaming enthusiast and play a lot of e-games. Currently his favourite game is Dota 2. After his under-grad he wishes to go for a research oriented job in mechanical engineering. He is currently doing a research project with prof. Shree Ram Valluri of University of Western Ontario, Canada.")
        lbl.pack(padx=2, pady=2)
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
button3 = Button(topFrame, text="Torsion Spring", command = create_window_2)
button4 = Button(topFrame, text="Constant Force Spring", command = create_window_2)

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
img2 = ImageTk.PhotoImage(Image.open("spr3_3.png"))
panel2 = Label(imageFrame, image = img2)
panel2.pack(side=LEFT)
img3 = ImageTk.PhotoImage(Image.open("1.png"))
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
new_item.add_command(label='Export')
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
