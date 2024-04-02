def f(x):
    return  1-sin(x)

def ptfix(eps):
    x=0.5
    i=0
    while (abs(f(x)-x)>eps):
        print("f(x)-x=",abs(f(x)-x))
        x=f(x)
        i+=1
        print(i)
    return "res est:",x

from math import *
eps=0.001
f=ptfix(eps)
#print(float('%.3f' % (f)))
print(f)