from pickle import*
from math import*
def saisir():
    global n
    n = int(input('donner n : '))
    while not (1<n<40):
        n = int(input('erreur donner n : '))
        
def remplir():
    f = open('Donnees.dat','wb')
    for i in range(n):
        e ={}
        e["np"] = input('nom et prenom eleve n'+str(i+1)+' : ')
        while not(len(e["np"])<=30):
            e["np"] = input('erreur nom et prenom eleve n'+str(i+1)+' : ')
        
        e["age"] = int(input("age eleve n"+str(i+1)+" : "))
        while not(10<=e["age"]<=20):
            e["age"] = int(input("erreur age eleve n"+str(i+1)+" : "))
        
        e['res'] = input("resultat eleve n"+str(i+1)+" : ")
        while not(e['res'] in ('A','C','R') ):
            e['res'] = input("erreur resultat eleve n"+str(i+1)+" : ")
        dump(e,f)
    f.close()

def afficher():
    f = open('Donnees.dat','rb')
    nba = 0
    nbc = 0
    nbr = 0
    ok = False
    while not ok:
        try:
            e = load(f)
            if(e['res'] == "A"):
                nba +=1
            elif(e['res'] == "C"):
                nbc += 1
            else:
                nbr += 1
        except:
            ok=True
    print("la pourcentage des admis",round(nba*100/n,2),'%')
    print("la pourcentage des controles",round(nbc*100/n,2),'%')
    print("la pourcentage des refuses",round(nbr*100/n,2),'%')
    f.close()
#pp
saisir()
remplir()
afficher()