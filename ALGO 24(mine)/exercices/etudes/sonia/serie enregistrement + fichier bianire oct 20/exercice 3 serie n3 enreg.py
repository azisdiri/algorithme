from pickle import dump
from numpy import array

def alpha_min_esp(ch):
    
    i = 0
    while (i<len(ch) and (('a'<=ch[i]<='z') or (ch[i] == ' '))):
        i += 1
    return i == len(ch)


def alpha_min(ch):
    
    i = 0
    while (i<len(ch) and ('a'<=ch[i]<='z')):
        i += 1
    return i == len(ch)

def nbr_occurences(phr,mot):
    nocc = 0
     ph += ' '
     while ph!='':
         
        
    

def remplir():
    global f1,n
    f1 = open('initial.dat','wb')
    e = {}
    e.phr = input('donner phrase : ')
    while not (len(e.phr) > 8)  and (alpha_min_esp(e.phr)):
        e.phr = input('erreur donner phrase : ')
   e.mot = input('donner un mot : ')
   while not alpha_min(e.mot):
       e.mot = input('erruer donner un mot valide : ')
    dump(e,f1)
    n = 1 
    rep = input('Quitter O/N')
    while not (rep in('O','N')):
        rep = input('erreur : reponse invalide')
    while not(rep.upper() == "N"):
        e = {}
        e.phr = input('donner phrase : ')
        while not (len(e.phr) > 8)  and (alpha_min_esp(e.phr)):
            e.phr = input('erreur donner phrase : ')
        e.mot = input('donner un mot : ')
        while not alpha_min(e.mot):
           e.mot = input('erruer donner un mot valide : ')
        dump(e,f)
        close(f)
        n+=1

def former():
    global f2
    f1 = open('initial.dat','rb')
    tab1 = array([str()]*n)
    tab2 = array([str()]*n)
    for i in range(n):
        e = load(f)
        tab1[i] = e.phrase
        tab2[i] = e.mot
    close(f1)
    f2 = open('initial.dat','wb')
    for i in range(n):
        e = {}
        e.nocc = nbr_occurences(tab1[i],tab2[i],n)
        

def afficher():
    f2 = open('initial.dat','rb')
    ok  = False
    while not ok:
        try:
            e = load(f)
            for i in range(e.occ):
                print(t[i])
            print(e.occ)
        except:
            ok = True
#pp
remplir()
former()
afficher()