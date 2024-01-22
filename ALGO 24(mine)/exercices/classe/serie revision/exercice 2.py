def palindrome(ch):
    i = 0
    while (i<=(len(ch) // 2 )-1) and (ch[i] == ch[len(ch)-i-1]):
        i += 1
    return i == len(ch)//2

def verif(mot):
    i = 0
    while (i<len(mot)) and ('A'<=mot[i]<='Z'):
        i += 1
    return i == len(mot)

def saisir():
    mot = input('donner ch : ')
    while not((len(mot)>0) and (verif(mot))):
        mot = input('erreur donner ch : ')
    return mot

def remplir(T,n):
    for i in range(n):
        T[i] =  saisir()
    
def afficher(T,n):
    ch = ""
    for i in range(n):
        if palindrome(T[i]):
            ch = ch + T[i] + '/'
    if ch!="":
        print('les mots palindromes : ', ch[:len(ch)-1])
    else: 
        print("il n'ya pas des mots palindromes dans ce tableau : ", ch[:len(ch)-1])
#pp
from numpy import array
n = int(input('donner n : '))
while not (3<=n<=15):
    n = int(input('erreur donner n : '))
T = array([str]*n)
remplir(T,n)
afficher(T,n)