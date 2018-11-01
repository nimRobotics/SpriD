from tkinter import *
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


root = Tk()

#Radiobutton variable
var = IntVar()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^from brain ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
pi = 3.14159265;
# material = [m, A(kpsi), E(mpsi), G(mpsi), density(ld/inch^3), relative cost]
A228 = [0.145, 201, 29.5, 12, 0.284, 2.6]
# # TODO: pg 510 diameter dependency
A229 = [0.147, 147, 30, 11.5, 0.284, 1.3]
A227 = [0.190, 140, 28.8, 11.7, 0.284, 1.0]
A232 = [0.168, 169, 29.5, 11.2, 0.284, 3.1]
A401 = [0.108, 202, 29.5, 11.2, 0.284, 4]

def calcMain():
    #def calcMain(fmax, ymax, freelength, solidlength, material, endCondition):
# if inout in si
    if var.get()==1:
        fmax=float(txt_fmax.get())/4.44822
        ymax=float(txt_ymax.get())/25.4
        freelength=float(txt_freelength.get())/25.4
        solidlength=float(txt_solidlength.get())/25.4
    if var.get()==2:
        fmax=float(txt_fmax.get())
        ymax=float(txt_ymax.get())
        freelength=float(txt_freelength.get())
        solidlength=float(txt_solidlength.get())


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
                xD=D
                xd=d
                xNa=Na
                xls=ls
                xlo=lo
                xfom=fom
            counter=counter+1
            f=open("res.txt", "a+")
            f.write("Wire diameter %f\r\n" % d)
            f.write("Spring diameter %f\r\n" % D)
            f.write("Na %f\r\n" % Na)
            f.write("ls %f\r\n" % ls)
            f.write("lo %f\r\n" % lo)
            f.write("Figure of merit %f\r\n" % fom)
            f.write("_________________________\n")
            f.close()
        elif d>1:
            print("iteration stopped")
            break
        d = d+0.001;
    print(xD, xd, xNa, xls, xlo, xfom)
    res = "Spring diameter " + str(xD) + "\nWire diameter "+str(xd)+"\nNa "+str(xNa)+"\nls "+str(xls)+"\nlo "+str(xlo)+"\nFigure of merit "+str(xfom)
    lbl_res.configure(text= res)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^from brain ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def callback(event):
    webbrowser.open_new(r"file://res.txt")
    # /home/aakash/DME/res.txt
    #
    # "file://c:\test\test.csv"


headFrame = Frame(root)
toolbar1 = Frame(root)
toolbar2 = Frame(root)
toolbar3 = Frame(root)
toolbar4 = Frame(root)
calcFrame = Frame(root)
toolbar5 = Frame(root)
toolbar6 = Frame(root)
toolbar7 = Frame(root)
footFrame = Frame(root)

lbl = Label(headFrame, text="Input the given params",font=("Arial B",14))
lbl.pack(padx=2, pady=2)

headFrame.pack(side=TOP, fill=X, padx=4 , pady=20)

lbl = Label(toolbar1, text="Maximum force", width=15)
lbl.pack(side=LEFT, padx=2, pady=2)

txt_fmax = Entry(toolbar1,width=10)
txt_fmax.pack(side=LEFT, padx=2, pady=2)

lbl = Label(toolbar1, text="m/s^2",font=("Arial B", 10), width=6)
lbl.pack(side=LEFT, padx=2, pady=2)

lbl = Label(toolbar1, text="ymax", width=15)
lbl.pack(side=LEFT, padx=2, pady=2)

txt_ymax = Entry(toolbar1,width=10)
txt_ymax.pack(side=LEFT, padx=2, pady=2)

lbl = Label(toolbar1, text="m/s^2",font=("Arial B", 10), width=6)
lbl.pack(side=LEFT, padx=2, pady=2)

toolbar1.pack(fill=X, padx=70 )

lbl = Label(toolbar2, text="Free Length", width=15)
lbl.pack(side=LEFT, padx=2, pady=2)

txt_freelength = Entry(toolbar2,width=10)
txt_freelength.pack(side=LEFT, padx=2, pady=2)

lbl = Label(toolbar2, text="MPa",font=("Arial B", 10), width=6)
lbl.pack(side=LEFT, padx=2, pady=2)

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

lbl = Label(toolbar3, text="MPa",font=("Arial B", 10), width=6)
lbl.pack(side=LEFT, padx=2, pady=2)

lbl = Label(toolbar3, text="Material", width=15)
lbl.pack(side=LEFT, padx=2, pady=2)

combo_mat = Combobox(toolbar3,width=5)
combo_mat['values']= ('A227','A228','A229','A232','A401')
combo_mat.current(1) #set the selected item
combo_mat.pack(side=LEFT, padx=2, pady=2)

# lbl = Label(toolbar3, text="m/s^2",font=("Arial B", 10), width=6)
# lbl.pack(side=LEFT, padx=2, pady=2)

toolbar3.pack(fill=X, padx=70)

lbl = Label(toolbar4, text="Output Units", width=15)
lbl.pack(side=LEFT, padx=2, pady=2)

rad1 = Radiobutton(toolbar4,text='US', value=1, variable=var)
rad1.pack(side=LEFT, padx=2, pady=2)

rad2 = Radiobutton(toolbar4,text='SI', value=2, variable=var)
rad2.pack(side=LEFT, padx=2, pady=2)

toolbar4.pack(fill=X, padx=70)

b = Button(calcFrame, text="Calculate",command=calcMain)
b.pack()
calcFrame.pack(fill=X, pady=20)

lbl = Label(toolbar5, text="Results", width=6,font=("Calibri",10))
lbl.pack(padx=2, pady=2)

link = Label(toolbar5, text="(more)", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)

lbl_res = Label(toolbar5, text="", width=40)
lbl_res.pack(padx=2, pady=2)

toolbar5.pack(side=BOTTOM)



mainloop()
