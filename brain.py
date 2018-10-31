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

def calcMain(fmax, ymax, freelength, solidlength, material):
    d=0.071
    while d>0:
        # factor of safety # TODO: take input
        ns = 1.2;
        # fixed pg510
        zeta = 0.15
        #for fom
        gama = 1;
        #for music wire

        ## TODO: add cases
        if material=='A228':
            A=A228[1]*1000
            m=A228[0]
            E=A228[2]*1000000
            G=A228[3]*1000000
            rc=A228[5]


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
        Nt = Na +2;
        # for square and groun spring
        ls = d*Nt;
        # p = (lo-2*d)
        lo = ls + (1+zeta)*ymax;
        fom = -rc*gama*(pi**2)*(d**2)*Nt*D*0.25;
        # if (C > 4 and C < 12 and Na > 3 and Na < 15 and ls < solidlength and lo < freelength):
        if (C >= 4 and C <= 12 and Na >= 3 and Na <= 15 and ls < solidlength and lo < freelength):
            break
        if d>0.1:
            print("error in iteration results")
            break
        d = d+0.001;
        # print(beta, C, D, d, Na, ls, lo, fom)
        # print("beta, C, D, d, Na, ls, lo, fom")
    return D, d, Na, ls, lo, fom

a = float(input("What is fmax"))
b = float(input("What is ymax"))
c = float(input("What is freelength"))
d = float(input("What is solidlength"))
m = input("Enter material")
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
print(calcMain(a,b,c,d,m))
