def euler(eps):   
    s1=1
    s2=1.25
    i=3
    while (sqrt(6*s2)-sqrt(6*s1))>eps:
        s1=s2
        s2=s1+(1/(i*i))
        i+=1
    return  sqrt(s2*6)
    
from math import sqrt    
eps=0.000000001
print(euler(eps))