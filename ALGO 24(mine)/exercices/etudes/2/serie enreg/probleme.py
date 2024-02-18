from numpy import array
from pickle import dump, load


def saisir():
    global n
    n = int(input('donner n : '))
    while not (n <= 5000 and n >0):
        n = int(input('donner n : '))


def valide(ch):
    ch = ch.upper()
    ch1 = ""
    j = 0    
    while (j < len(ch)) and (ch[j] in ["A", "F", "I", "P"]) and (ch1.find(ch[j]) == -1):
        ch1 += ch[j]
        j += 1  
    return len(ch) == 4 and j == len(ch)



def remplir():
    global f
    f = open('SMS.dat', 'wb')
    for i in range(n):
        e = {}
        e["sms"] = input('sms : ')
        while not (valide(e["sms"])):
            e["sms"] = input('sms : ')
        e["tel"] = input("donner le numero de telephone : ")
        dump(e, f)
    f.close()


def calcul_score(ch):
    ch = ch.upper()
    ch1 = "IFAP"
    s = 4
    for i in range(len(ch)):
        if ch[i] != ch1[i]:
            s -= 1
    return s*25


def former():
    global Foot
    f = open('SMS.dat', 'rb')
    for i in range(n):
        e = load(f)
        Foot[i]["numero"] = e["tel"]
        Foot[i]["classement"] = e["sms"]
        Foot[i]["score"] = calcul_score(e["sms"])


def meilleur_score(t, n):
    maxi = t[0]["score"]
    for i in range(1,n):
        if t[i]["score"] > maxi:
            maxi = t[i]["score"]
    return maxi


def dist(t,n,x):
    j = 0
    while((j<n)and(t[j]!=x)):
        j+=1
    return j == n
        
    

def creer():
    global n1
    n1 = 0
    maxi = meilleur_score(Foot, n)
    for i in range(n):
        if (Foot[i]["score"] == maxi) and dist(NT, n1, Foot[i]["numero"]):
            NT[i] = Foot[i]["numero"]
            n1 += 1

def afficher():
    f1 = open('abonnes.dat','rb')
    for i in range(n1):
        e = load(f1)
        if e["numtel"] == NT[i]:
            print(e["nom"]+" "+e["nom"])
    f1.close()
    
# pp
saisir()
remplir()
Foot = array([{}]*n)
former()
NT = array([str]*n)
creer()
afficher()
