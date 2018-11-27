function [ D, d, Na, ls, lo, fom ] = myFunction( fmax, ymax, freelength, solidlength )

d=0.01;

while (d>0) 
    
 ns = 1.2;
 zeta = 0.15;
 gama = 1;
 %for fom
 
 % for music wire
 A = 201000 ;
 % relative cost for mausc wire
 rc = 2.6;
 % kpsi inch
 m = 0.145;
 %E = 28.5;
 G = 11750000;
  
 sut = A/(d^m);
 ssy = 0.45*sut;
 alpha = ssy/ns;
 beta = (8*(1+zeta)*fmax)/(pi*(d^2));
 C = (2*alpha-beta)/(4*beta) + (((2*alpha-beta)/(4*beta))^2 - (3*alpha)/(4*beta))^(0.5);
 D = d*C;
 % kb = (4*C+ 2)/(4*C - 3);
 % taus = (kb*8*(1+zeta)*fmax*D)/(3.147*(d^3));
 % OD = D+d;
 Na = (G*(d^4)*ymax)/(8*(D^3)*fmax);            
 Nt = Na +2;
 % for square and groun spring
 ls = d*Nt;
 lo = ls + (1+zeta)*ymax;
 fom = -rc*gama*(pi^2)*(d^2)*Nt*D*0.25;
    
    if ((C>=4)&&(C<=12)&&(Na>=3)&&(Na<=15)&&(ls<solidlength)&&(lo<freelength))
        break
    end
    if (d>1)
        break
    end
    d = d+0.001;
end  

end
    