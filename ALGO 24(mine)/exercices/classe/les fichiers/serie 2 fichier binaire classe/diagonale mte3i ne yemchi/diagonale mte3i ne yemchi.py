from numpy import array
from random import randint

# fonction du classe


def differents(ch):
    ch1 = ch[0]
    i = 1
    while ((i < len(ch)) and (len(ch) >= 4)):
        if ch1.find(ch[i]) == -1:
            ch1 += ch[i]
        i += 1
    return len(ch1) >= 4


def saisir():
    global n
    n = int(input('donner n : '))
    while not (3 <= n <= 10):
        n = int(input('erreur donner n : '))


def remplir():
    for i in range(n):
        m[0, i] = randint(0, 9)
    for l in range(1, n):
        for c in range(0, n-l):
            s = 0
            for k in range(c, n-l):
                s += m[l-1, k]
            m[l, c] = s


def transfert():
    with open('diagonale.txt', 'w') as f1:
        for l in range(0, n):
            k = l
            ch = ''
            for c in range(0, l+1):
                ch = str(m[k-c, c]) + ch
            f1.write(ch+'\n')


def afficher():
    with open('diagonale.txt', 'r') as f1:
        ch = f1.readline()
        ch = ch[:len(ch)-1]
        # on supprime le dernier caractere '\n'
        while ch != '':
            if (differents(ch)):
                print(ch)
            ch = f1.readline()
            ch = ch[:len(ch)-1]


# pp
saisir()
m = array([[int()]*n]*n)
remplir()
transfert()
afficher()
