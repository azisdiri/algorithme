
def saisir():
    global p
    p = int(input('donner p : '))
    while not (p<=30 and p>=2):
        p = int(input('donner n : '))
        
def dist(t,n,x):
    j = 0
    while (j<=n-1) and (t[j]!=x):
        j += 1
    return j == n    
def remplir():
    global f1
    f1 = open('Depart.dat','wb')
    t = array([int()]*30)
    u0 = int(input('1er terme: '))
    while not (u0>=2 and u0<=1000):
        u0 = int(input('1er terme: '))
    t[0] = u0
    dump(u0,f1)
    for i in range(1,p):
        u0 = int(input('remplir : '))
        while not (u0>=2 and u0<=1000 and dist(t,i,u0)):
            u0 = int(input('remplir : '))
        t[i] = u0
        dump(u0,f1)
    f1.close()
def nbtermes(x,j):
    if x == 1:
        return j
    else:
        if x%2 == 0:
            return nbtermes(x//2,j+1)
        else:
            return nbtermes(x*3+1,j+1)
def generer():
    global f2
    f1=open("Depart.dat","rb")
    f2=open("Suite.dat","wb")
    for i in range(p):
        u0=load(f1)
        e={}
        e["dep"]=u0
        e["nb"]=nbtermes(u0,0)
        dump(e,f2)
    f1.close()
    f2.close()
def rech_min(f2):
    f2=open("Suite.dat","rb")
    e=load(f2)
    min=e["nb"]
    eof=False
    while not(eof):
        try:
            e=load(f2)
            if e["nb"]<min:
                min=e["nb"]
        except:
            eof=True
    f2.close()
    return min

def afficher(f2):
    minimum=rech_min(f2)    
    f2=open("Suite.dat","rb")
    eof=False
    print("les nombres des termes de depart qui correspondent au nombre de termes minimal",minimum,"sont:")
    while not (eof):
        try:
            e=load(f2)
            if (e["nb"]==minimum):
                print(e["dep"])
        except:
            eof=True

from pickle import dump,load
from numpy import array
##pp
saisir()
remplir()
generer()
afficher(f2)
