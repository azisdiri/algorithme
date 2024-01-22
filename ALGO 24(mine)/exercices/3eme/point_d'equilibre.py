def remplir(T,n):
    
    for i in range(n):
        T[i] = int(input('T['+str(i)+'] : '))
        
def inconnue(T,db,fn):
    s = 0
    for i in range(db,fn):
        s += T[i]
    return s 

def affiche_equilibre(T,n):
    eq = 0
    for k in range(1,n-2):
        s1 = inconnue(T,0,k)
        s2 = inconnue(T,k+1,n)
        if s1 == s2:
            eq += 1
            print(k,'pt eq')
    if eq == 0:
        print("Aucun point d'equilibre")
        
##pp
from random import randint
from numpy import array
n = 10
T = array([int]*n)
remplir(T,n)
affiche_equilibre(T,n)