from pickle import *
from math import *
from numpy import *
from random import randint

def chance():
    ch = ''
    for i in range(4):
        ch = ch + chr(randint(65,90))
    return ch

def poids(ch):
    s = 0
    for i in range (4):
        s = s + ord(ch[i])
    return s

def heureux(x):
    while (len(str(x)) != 1):
        ch = convch(x)
        s = 0
        for i in range(len(ch)):
           s = s + int(ch[i])
        x = s
    return x == 1

def verif(ch):
    i = 0
    nb = 0
    while (i<len(ch) and (('A'<= ch[i].upper()<='Z')or(ch[i] == ' '))):
        if ch[i] == ' ':
            nb += 1
        i += 1
    return i == len(ch) and nb == 1

def remplir():
    global f1
    f1 = open('candidat.dat','wb')
    rep = ''
    while not(rep.upper() == 'N'):
        c = {}
        c['np'] = input('np : ')
        while not(('A'<= c['np'] <= 'Z') and (verif(c['np']))):
            c['np'] = input('erreur np : ')
        c['mc'] = chance()
        c['p'] = poids(c['mc'])
        dump(c,f1)
        print('Voulez vous continuez? O/N')
        rep = input()
        while not(rep.upper() in ['O','N']):
            rep = input()
    f1.close()

def remplir1():
    global f1, t, n
    f1 = open('candidat.dat','rb')
    n = 0
    ok = False
    while not ok:
        try :
            c = load(f1)
            if heureux(c['np']):
                t[n] = c['np']
                n += 1
        except:
            ok = True
    f1.close()

def afficher():
    for i in range(n):
        print(t[i]) 

#pp
remplir()
t = array([int()]*10)
remplir1()
afficher()