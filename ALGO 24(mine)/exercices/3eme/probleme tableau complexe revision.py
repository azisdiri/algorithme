from numpy import array
from math import *
def saisie():
    n = int(input('n =  '))
    while not((3<=n<=100) and (n%2==0)):
        n = int(input('n =  '))
    return n 
def remplir(t1,t2,n):
    for i in range(n):
        print('former le nombre complexe no  '+str(i+1))
        a = int(input('donner a : '))
        b = int(input('donner b : '))
        while not(a>0 and b>0):
            a = int(input('donner a : '))
            b = int(input('donner b : '))
        t1[i] = str(a) +'+'+ str(b)  + "*i"
        t2[i] = sqrt(a*a + b*b)
        
def maxi(t1,t2,n):
    m = t2[0]
    p = 0
    for i in range(1,n):
        if t2[i] > m:
            p = i
            m = t2[i]
    return 'le module maximal est '+str(round(m,2))+' correspond au nombre complexe '+t1[p]
def afficher(t1,t2,n):
    for i in range(n):
        print('le module de ',t1[i],' = ',round(t2[i],2))
    print(maxi(t1,t2,n))
##pp
n = saisie()
t1 = array([str]*n)
t2 = array([float]*n)
remplir(t1,t2,n)
afficher(t1,t2,n)