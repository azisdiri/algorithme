from random import randint
from numpy import array
##pp
T = array([int]*n)
M = array([[int]*n]*n)
saisir()
remplir(M)
remplir1(T)
trier(T)
afficher(T)
#sp
def saisir():
    
    global n
    n = int(input('longeur du matrice: '))
    while not(4<=n<=20):
        n = int(input('longeur du matrice: '))
        
def remplir(M):

for i in range(n):
        for j in range(n):
            M[i,j] = randint(4,9)
            
def remplir1(T):
    for i in range(n):
        s = 0
            for j in range(n):
                s = s + M[i,j]
            T[i] = s
            
            
def trier(T,n):
    
    x = 0
    while not(n =1):
        for i in range(x,n-1):
            if t[i]>t[i+1]:
                aux = t[i]
                t[i] = t[i+1]
                t[i+1] = aux
        n = n-1
        for j in range(n,x+1,-1):
            if t[]<t[]
            