from pickle import *
from numpy import array
from random import randint
#fonctions
def saisir():
    global n
    n = int(input('nobmre es employes : '))
    while not (2<=n<=15) :
        n = int(input('nobmre es employes : '))

def verif(ch):
    espcs = 0
    i = 0
    while (i < len(ch)) and (espcs < 2):
        if ch[i] == ' ':
            espcs += 1
        i += 1
    j = 0
    while (j < len(ch)) and (("A"<=ch[j].upper()<="Z") or (ch[j] == ' ')):
        j += 1   
    return (espcs == 1) and ('A'<=ch[0]<='Z') and ('A'<=ch[ch.find(' ')+1]<='Z') and (j == len(ch)) 

    
def cr_email(ch):
    mail = ch[:ch.find(' ') ] + '.' +  ch[ch.find(' ') +1:]
    if 0<=abs(ord(mail[0]) - ord(mail[mail.find('.')+1]))<=6:
        mail += '@Planet.tn'
    elif 7<=abs(ord(mail[0]) - ord(mail[mail.find('.')+1]))<=12:
        mail += '@Topnet.tn'
    elif 13<=abs(ord(mail[0]) - ord(mail[mail.find('.')+1]))<=18:
        mail += '@Google.fr'
    else:
        mail += '@Yahoo.fr'
    return mail

#procedures
def remplir():
    global f1
    f1 = open('NOMPR.dat','wb')
    for i in range(n):
        ch = input('nom et prenom emp n°'+str(i)+' : ')
        while not(verif(ch)):
            ch = input('erreur nom et prenom emp n°'+str(i)+' : ')
        dump(ch,f1)
    f1.close()
    

def former():
    global f2
    f1 = open('NOMPR.dat','rb')
    t = array([str()]*n)
    for i in range(n):
        ch = load(f1)
        t[i] = ch
    f1.close()
    f2  = open('EMAIL.dat','wb')
    for i in range(n):
        e = {}
        e['np'] = t[i]
        e['email'] = cr_email(t[i])
        e['mp'] = e['email'][e['email'].find('.')+1]+str(ord(e['email'][0]))+chr(randint(65,90))
        dump(e,f2)
    f2.close()
    
def afficher():
        f2  = open('EMAIL.dat','rb')
        ok = False
        while not ok:
            try:
                 e = load(f2)
                 if (e['email'][e['email'].find('@'):] == '@Planet.tn'):
                    print(e['email'])      
            except:
                ok = True

#pp
saisir()
remplir()
former()
afficher()