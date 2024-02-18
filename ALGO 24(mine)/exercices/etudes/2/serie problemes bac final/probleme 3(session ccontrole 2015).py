from pickle import *
from numpy import array


def saisir():
    global n
    n = int(input("taille : "))
    while not (n <= 200 and n >= 3):
        n = int(input("taille : "))


def remplir():
    global f1
    f1 = open("Processus.dat", "rb")
    for i in range(n):
        e = {}
        e["code"] = "P"+str(i+1)
        e["duree"] = int(input("duree:"))
        while not (e["duree"] >= 0):
            e["duree"] = int(input("duree:"))
        dump(e.f1)
    f1.close()


def sjf():
    t = array([{}]*200)
    transfert_1()
    tri()
    transfert_2()


def transfert_1():
    global t
    f1 = open("Processus.dat", "rb")
    for i in range(n):
        e = {}
        load(f, e)
        t[i]["code"] = e["code"]
        t[i]["duree"] = e["duree"]
    f1.close


def tri():
    global t
    for i in range(1, i):
        aux = t[i]["duree"]
        aux1 = t[i]["code"]
        j = i
        while (aux < t[j-1]["duree"]) and (j > 0):
            t[j]["duree"] = t[j-1]["duree"]
            t[j]["code"] = t[j-1]["code"]
            j -= 1
        t[j]["duree"] = aux
        t[j]["code"] = aux1


def transfert_2():
    global f2
    f2 = open("Ord_SJF.dat", "wb")
    for i in range(n):
        dump(t[i], f2)
    f2.close()


def generer():
    global f3
    f1 = open("Processus.dat", "rb")
    f2 = open("Ord_SJF.dat", "rb")
    f3 = open("Ord_Nouv.txt", "w")
    ff1 = False
    ff2 = False
    e1 = load(f1)
    e2 = load(f2)
    while (not (ff1) and not(ff2) and (e1 = e2)):
        f3.write(e1["code"])
    f2.close()
    f1.cose()
    f2 = open("Ord_SJF.dat","rb")
    while 


# pp
saisir()
remplir()
sjf()
generer()
