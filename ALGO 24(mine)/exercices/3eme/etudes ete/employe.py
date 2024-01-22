def existe(T,ch,nt):
    i = 0
    ok = False
    while (i<nt)and(ok == False):
        if T[i]['nom'] == ch:
            ok = True
        else:
            i += 1
    return ok

def verif(T,chn):
    i = 0
    ok = True
    while (i<len(ch)) and (ok == True):
        if 'A'<=ch[i].upper()<='Z':
            i += 1
        else:
            ok = False
    return ok

def remplir(T,n):
    for i in range(n):
        ch = T[i]['nom']
        ch = input('le nom d employe: ')
        while not(('A'<=ch[0]<='Z') and (verif(T,ch) == True) and (len(ch)<=10) and(existe(T,T[i]['nom'],n) == False)):
            ch = input('le nom d employe: ')
            
        civil = T[i]['et']['civil']
        civil = int(input('etat civil : '))
        while not (0<=civil<=1):
            civil = int(input('etat civil : '))
        enf = T[i]['et']['enf']
        if civil == 0:
            enf = 0
        else:
            enf = int(input('nombre d enfants : '))
            while not (enf>0):
                enf = int(input('nombre d enfants : '))
        ind = T[i]['ind']
        if  civil == 0:
            ind = 4.5
        else:
            if 1<=enf<=3:
                ind = 15*enf
            elif 4<=enf<=6:
                ind = 10*enf
            else:
                ind = 5*enf

def afficher(T,n):
    for i in range(n):
        m = 0
        c = 0
        if T[i]['et']['civil'] == 1:
            print('emp no ',i+1,T[i]['nom'])
            m += 1
        else:
            c +=1
    print('pourcentage des employes maries',(m/n)*100)
    print('pourcentage des employes celibataire',(c/n)*100)
#############pp
from numpy import array
n = int(input('donner n : '))
while not 3<=n<=30:
    n = int(input('donner n : '))
etat = {'civil': int(), 'enf' : int()}
employe = {'nom': str, 'et': dict(etat), 'ind' : float()}
T = array([employe]*n)
remplir(T,n)
afficher(T,n)