def f(x):
    return x**2-5

def zro(a,b,eps):
    m=(a+b)/2
    i=0
    while (b-a)>eps and f(m)!=0:
        i+=1
        print("iteration n°"+str(i))
        print(b,"-",a,"=",b-a)
        if f(a)*f(m)>0:
            a=m
        else:
            b=m
        m=(a+b)/2
    return m
            
        
        
from math import *
eps=float(input("eps:"))
a=float(input("donner a : "))
b=float(input("donner b : "))
print(zro(a,b,eps))