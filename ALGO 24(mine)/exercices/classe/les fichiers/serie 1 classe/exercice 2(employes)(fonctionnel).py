from pickle import *
def saisir():
    global n
    n = int(input('donner n : '))
    while not (2<=n<=100):
        n = int(input('erreur donner n : '))
        
        
#todo def verif_alph(ch):
def verif_alph(ch):
    i = 0
    while  (i<=len(ch)-1) and ('A'<=ch[i].upper()<='Z') :
        i += 1
    return i == len(ch)
    


def remplir():
    global f
    f  = open("employes.dat",'wb')
    for i in range(n):
        e = {}
        
        e['id'] = int(input("donner l'identifiant du l'employe n°"+str(i)+" : "))
        
        e['nom'] = input("donner le nom du l'employe n°"+str(i)+" : ")
        while not(verif_alph(e['nom'])):
            e['nom'] = input("erreur donner le nom du l'employe n°"+str(i)+" : ")
        
        e["ntel"] = input("donner le numero du telephone du l'employe n°"+str(i)+" : ")
        while not(len(e["ntel"])==8):
            e["ntel"] = input("erreur donner le numero du telephone du l'employe n°"+str(i)+" : ")
        
        e["grd"] = input("donner le grade du l'employe n°"+str(i)+" : ")
        while not(e["grd"] in ["A","B","C","D"]):
            e["grd"] = input("erreur donner le grade du l'employe n°"+str(i)+" : ")
            
        dump(e,f)
    f.close()
        
def afficher1():
    f = open("employes.dat","rb")
    ok = False
    while not ok:
        try:
            e = load(f)
            print(e["id"])
            print(e["nom"])
            print(e["ntel"])
            print(e["grd"])
        except:
            ok = True
    f.close()
            
def afficher2():
    f = open("employes.dat","rb")
    ch = input("donner un grade :  ")
    while not (ch in ["A","B","C","D"]):
            ch = input("erreur donner un grade :  ")
    s = 0
    ok = False
    while not ok:
        try:
            e = load(f)
            if e['grd'] == ch:
                s+=1
        except:
            ok = True 
    print("Le nombre d'employes : ",s)
    print("pourcentage par rapport au numbre total des employes :  ",(s*100)/n)


#pp
saisir()
remplir()
afficher1()
afficher2()