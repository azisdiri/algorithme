from numpy import array
def maximum(x,y,z):
    m = 0
    if(x>y) and (x>z):
        m = x
    elif (y>x) and (y>z):
        m = y
    else:
        m = z
    return m

def remplir():
    global t
    for i in range(n):
        e["nom"] = input("nom : ")
        e["prenom"] = input("prenom : ")
        e["age"] = int(input("age : "))
        e["essai1"] = float(input("essai1 : "))
        e["essai2"] = float(input("essai2: "))
        e["essai3"] = float(input("essai3: "))
        t[i] = e

def afficher():
    for i in range(n):
        e = t[i]
        m = maximum(e["essai1"],e["essai2"],e["essai3"])
        if (m == e["essai1"]):
            n_essai = "1"
        elif (m == e["essai2"]):
            n_essai = "2"
        else: 
            n_essai = "3"
        print(e["nom"]+" "+e["prenom"]+" meilleur essai :"+str(m)+" m essai n°"+n_essai)

#pp
n = int(input("donner n : "))
e = {}
t  = array([e]*n)
remplir()
afficher()