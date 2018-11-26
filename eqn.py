from sympy import *
x = Symbol('x')
# y = solve(x**4 - 4*x -1, x)
# print(N(y[1])*(-1)**0.5)
# print((-1)**0.5)

ns =1.5
zeta = 0.15
famp = 7
fmean = 11
sse = 56861.6	
sut = 284306.60
d = 0.0915
# temp = ns*2*(1+zeta)*(famp/se  + fmean/sy)
# eqn  = 4*(x**2)*temp + 2*temp*x-4*x+3
eqn = (((4*x+2)*8*(1+zeta)*x*ns)/(pi*d*d))*(famp/sse+fmean/sut)+3-4*x

c = solve(eqn, x)
for tt in c:
  print(N(tt))


