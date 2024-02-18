from pickle import *
from numpy import array
def dist(t,n,x):
    j = 0
    while (j<=n-1) and (t[j]!=x):
        j += 1
    return j == n


def nbtermes(x,j):
    if x == 1:
        return j + 1
    elif x % 2 == 0:
        return nbtermes(x // 2, j + 1)
    else:
        return nbtermes(x * 3 + 1, j + 1)

def saisir():
    global p
    p = int(input('donner p : '))
    while not (p<=30 and p>=2):
        p = int(input('donner n : '))
        
        
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
    
def generer():
    global f2
    f1 = open("Depart.dat","rb")
    f2 = open("Suite.dat","wb")
    for i in range(p):
        u0 = load(f1)
        e = {}
        e["dep"] = u0
        e["nb"] = nbtermes(u0,0)
        dump(e,f2)
    f1.close()
    f2.close()
    
def afficher():
    f2 = open("Suite.dat","rb")
    fin_fichier = False
    while not (fin_fichier):
        try:
            e = load(f2)
            print("x = ",e["dep"],"nobre de termes",e["nb"])
        except:
            fin_fichier == False


##pp
saisir()
remplir()
generer()
afficher()