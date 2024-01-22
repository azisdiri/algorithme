
##sp

def verif(ch):

    i = 0
    ok = True
    while (i<len(ch)) and (ok == True):
        if 'A'<=ch[i].upper()<='Z':
            i += 1
        else:
            ok = False
    return ok

def recherche(T,ch,nt):
    i = 0
    ok = False
    while (i<nt)and(ok == False):
        if T[i]['nom'] == ch:
            ok = True
        else:
            i += 1
    return ok

def remplir(T,n):
    
    for i in range(n):
        T[i] = {}
        T[i]['nom'] = input('nom employe: ')
        while not (verif(T[i]['nom']) and (len(T[i]['nom'])<=10) and (recherche(T,T[i]['nom'],i) == False) and ('A'<=T[i]['nom'][0]<='Z')):
                T[i]['nom'] = input('nom employe: ')
                
        T[i]['et'] = {}
        T[i]['et']['civil'] = int(input('etat civil: '))
        while not (0<=T[i]['et']['civil']<=1):
            T[i]['et']['civil'] = int(input('etat civil: '))
        if T[i]['et']['civil'] == 0:
            T[i]['et']['enf'] = 0
        else:
            T[i]['et']['enf'] = int(input("nbr d'enfents: "))
            while not(T[i]['et']['enf']>=0):
                    T[i]['et']['enf'] = int(input("nbr d'enfents: "))
        if T[i]['et']['civil'] == 0:
            T[i]['ind'] = 2.5
        else:
            if T[i]['et']['enf'] == 0:
                T[i]['ind'] = 4.5
            elif 1<=T[i]['et']['enf']<=3:
                T[i]['ind'] = 15*T[i]['et']['enf']
            elif 4<=T[i]['et']['enf']<=6:
                T[i]['ind'] = 10*T[i]['et']['enf']
            else:
                T[i]['ind'] = 6*T[i]['et']['enf']

def afficher(T,n):
    nm = 0
    for i in range(n):
        if T[i]['et']['civil'] == 1:
            print('employe no ',i+1,T[i]['nom'])
            nm += 1
        nc = n - nm        
    print('Le pourcentage des employes maries est: '+ str(nm/n*100))
    print('Le pourcentage des employes celibataires est: '+ str(nc/n*100))
        
        
#pp

from numpy import array
n = int(input('saisir n'))
while not (3<=n<=30):
    n = int(input('saisir n'))
etat = {'civil': int(), 'enf': int()}
employe = {'nom': str, 'et': dict(etat), 'ind': float()}
T = array([dict(employe)]*n)
remplir(T,n)
afficher(T,n)
                
                
                
               
        