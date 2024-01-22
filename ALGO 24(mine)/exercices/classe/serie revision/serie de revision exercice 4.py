from random import randint
from numpy import array
#procedure remplir
def remplir(M,n):
    for i in range(n):
        for j in range(n):
            M[i,j] = randint(1,101)
            
#procedure afficher
def afficher(M,n):
    s = 0
    max = M[0,0]
    for i in range(n):
        ch  = ''
        for j in range(n):
            ch = ch + str(M[i,j]) + ","
            s += M[i,j]
            if M[i,j] >= max:
                max = M[i,j] 
        print(ch[:len(ch)-1])
    print('la somme de la matrice M :  ', s)
    print('la plus grande valeur dans M : ',max)
#pp
n = int(input('donner n : '))
while not (2<=n<=10):
    n = int(input('erreur donner n : '))
M = array([[int()]*n]*n)
remplir(M,n)
afficher(M,n)