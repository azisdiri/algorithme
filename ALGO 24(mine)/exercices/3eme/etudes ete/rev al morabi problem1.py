from numpy import array
from random import randint
#module saisie:
def saisie():
    n = int(input('donner le nombre de clients : '))
    while not(5<=n<=1000):
        n = int(input('donner le nombre de clients : '))
    return n
#module remplir:
def remplir(T,n):
    for i in range(n):
        t[i] = input('t ['+str(i)+'] = ')
        while not (t[i].isdigit() and t[i][0] == '7' and len(t[i] == 8)):
            t[i] = input('t ['+str(i)+'] = ')
#module afficher :
def afficher(t,n):
    x = randint(0,n-1)
    y = int(t[x][:2])
    if 74<=y<=77:
        print('sud')
    elif y == 78:
        print('nord-ouest')
    elif y == 73:
         print('sahel')
    elif: y == 72:
        print('cap bon')
    else:
        print('grand tunis')
        
T = array([str])