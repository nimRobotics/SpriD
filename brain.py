# name = input("Enter a name: ")
# print(name)
def solutio(x,y,a):
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
a = float(input("What is x? "))

x = [1,2,3,4,5]
y = [2,4,6,8,10]
print(solutio(x,y,a))
