from numpy import array
def saisir():
    global n
    n = int(input("donner n : "))
    while not(2<=n<=150):
        n = int(input("erreur donner n : "))

def unique(T,n,x):
    i = 0
    ok = True
    while(ok == True) and (i<n):
        if T[i] == x:
            ok = False
        i += 1
    return ok
        
    
def verif_nom(ch):
    i = 0
    while(i<len(ch)) and ("A"<=ch[i].upper()<="Z"):
        i += 1
    return i == len(ch)

def remplir(T,n):
    for i in range(n):
        T[i] = {}
        T[i]["code"] = input('code du contact n°'+str(i+1)+': ')
        while not(unique(T,n,T[i]["code"]) and (T[i]["code"].isdecimal())):
            T[i]["code"] = input('erreur code du contact n°'+str(i+1)+': ')
        T[i]["code"] = T[i]["code"]
        #nom
        T[i]["nom"] = input("nom du contact n°"+str(i+1)+': ')
        while not(verif_nom(T[i]["nom"])):
            T[i]["nom"] = input("erreur nom du contact n°"+str(i+1)+': ')
        T[i]["nom"] = T[i]["nom"]
        #n1
        T[i]["n1"] = int(input('nombre des numeros : '))
        while not(1<=T[i]["n1"]<=9):
            T[i]["n1"] = int(input('erreur nombre des numeros : '))
        n1 = T[i]["n1"]
        #Tnum
        Tnum = array([int()]*n1)
        for j in range(n1 ):
            numero = int(input("tapez numero de tel : "))
            while not(len(str(numero))==6):
                numero = int(input("erreur tapez numero de tel : "))
            Tnum[j] = numero
        T[i]["Tnum"] = Tnum

def transferer(T,T1,T2,T3,n):
    for i in range(n):
        T1[i]= {}
        T2[i]= {}
        T3[i]= {}
        for j in range(T[i]['n1']):
            n1 = T[i]['n1']
            ch = str(T[i]["Tnum"][j])
            ch1 = ch[:2]
            Tnum = array([int()]*n1)
            if '20'<=ch1<='29':
                T1[i]["code"] = T[i]["Code"]
                T1[i]["n1"] = T[i]["n1"]
                T1[i]["Tnum"] = T[i]["Tnum"]
            elif  '90'<=ch1<='99' or ch1 == '40':
                T2[i]["code"] = T[i]["Code"]
                T2[i]["n1"] = T[i]["n1"]
                T2[i]["Tnum"] = T[i]["Tnum"] 
            elif '50'<=ch1<='58':
                T3[i]["code"] = T[i]["Code"]
                T3[i]["n1"] = T[i]["n1"]
                T3[i]["Tnum"] = T[i]["Tnum"]
#pp
saisir()
Tnum = array([str]*9)
T = array([{}]*n)
remplir(T,n)
T1 = array([{}]*n)
T2 = array([{}]*n)
T3 = array([{}]*n)
transferer(T,T1,T2,T3,n)
print(T)
print(T1,T2,T3)