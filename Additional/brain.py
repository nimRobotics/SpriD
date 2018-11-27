# name = input("Enter a name: ")
# print(name)
pi = 3.14159265;
def interplt(x,y,a):
    if a in x:
        i=x.index(a)
        #print(i)
        return y[i]
    else:
        for j in range(len(x)):
            if(a<x[j]):
               x1=x[j-1]
               x2=x[j]
               y1=y[j-1]
               y2=y[j]
               m=(y2-y1)/(x2-x1)
               c=m*(a-x1)+y1
               return c
# material = [m, A(kpsi), E(mpsi), G(mpsi), density(ld/inch^3), relative cost]
A228 = [0.145, 201, 29.5, 12, 0.284, 2.6]
# # TODO: pg 510 diameter dependency
A229 = [0.147, 147, 30, 11.5, 0.284, 1.3]
A227 = [0.190, 140, 28.8, 11.7, 0.284, 1.0]
A232 = [0.168, 169, 29.5, 11.2, 0.284, 3.1]
A401 = [0.108, 202, 29.5, 11.2, 0.284, 4]

def calcMain(fmax, ymax, freelength, solidlength, material, endCondition):
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
        if material=='A228':
            # if d <0.032:
            #     E=29.5*1000000
            #     G=12*1000000
            # elif d > 0.033

            A=A228[1]*1000
            m=A228[0]
            E=A228[2]*1000000
            G=A228[3]*1000000
            rc=A228[5]
        if material=='A229':
            A=A229[1]*1000
            m=A229[0]
            E=A229[2]*1000000
            G=A229[3]*1000000
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
        if endCondition==1:
            Nt=Na
            ls = d*(Nt+1)
        if endCondition==2:
            Nt=Na+1
            ls = d*Nt
        if endCondition==3:
            Nt=Na+2
            ls = d*(Nt+1)
        if endCondition==4:
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
    return xD, xd, xNa, xls, xlo, xfom

# a = float(input("What is fmax"))
# b = float(input("What is ymax"))
# c = float(input("What is freelength"))
# d = float(input("What is solidlength"))
# m = str(input("Enter material"))
# e = int(input("End condition"))
#
# print(calcMain(a,b,c,d,m,e))
print(calcMain(20,2,4,1,'A228',4))

## TODO:  solve 10,18
