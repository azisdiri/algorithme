#fesd l fichier sal7o wela mat5admouch makench ya3ml fichier texte taille mte3o yzid automatiquement 
f
rom pickle import *

from numpy import array


def saisir():
    global n
    n = int(input("taille : "))
    while not (n <= 200 and n >= 3):
        n = int(input("taille : "))


def remplir():
    global f1
    f1 = open("Processus.dat", "wb")
    for i in range(n):
        e = {}
        e["code"] = "P"+str(i+1)
        e["duree"] = int(input(e["code"]+" duree:"))
        while not (e["duree"] >= 0):
            e["duree"] = int(input("duree:"))
        dump(e, f1)
    f1.close()


def classer():
    global t
    t = array([{}]*200)
    transfert_1()
    tri()
    transfert_2()


def transfert_1():
    global t
    f1 = open("Processus.dat", "rb")
    for i in range(n):
        e = {}
        e = load(f1)
        t[i]["code"] = e["code"]
        t[i]["duree"] = e["duree"]
    f1.close()


def tri():
    global t
    for i in range(1, n):
        aux = t[i]
        j = i
        while (aux["duree"] < t[j-1]["duree"]) and (j > 0):
            t[j] = t[j-1]
            j -= 1
        t[j] = aux


def transfert_2():
    global f2
    f2 = open("Ord_SJF.dat", "wb")
    for i in range(n):
        dump(t[i], f2)
    f2.close()


def dist(t, n, x):
    j = 0
    while (j <= n-1) and (t[j] != x):
        j += 1
    return j == n


def generer():
    global f3
    f1 = open("Processus.dat", "rb")
    f2 = open("Ord_SJF.dat", "rb")
    f3 = open("Ord_Nouv.txt", "w")
    eof1 = False
    eof2 = False
    while (not (eof1) and not (eof2)):
        try:
            i = 0
            t1 = array([str()]*200)
            e1 = load(f1)
            e2 = load(f2)
            if (e1["duree"] == e2["duree"]):
                f3.write(e1["code"]+"\n")
                t1[i] = e1["code"]
                i += 1
        except:
            eof1 = True
            eof2 = True
    f2.close()
    f1.close()
    f2 = open("Ord_SJF.dat", "rb")
    eof2 = False
    e = load(f2)
    while not (eof2) and (dist(t1, i, e["code"])):
        f3.write(e["code"]+"\n")
    f2.close()
    f3.close()


# pp
saisir()
remplir()
classer()
generer()
