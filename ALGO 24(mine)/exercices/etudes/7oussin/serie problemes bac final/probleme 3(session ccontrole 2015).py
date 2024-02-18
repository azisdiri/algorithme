from pickle import *
from numpy import array


def saisir():
    global n
    n=int(input("taille : "))
    while not (n <= 200 and n >= 3):
        n=int(input("taille : "))


def remplir():
    global f1
    f1=open("Processus.dat", "rb")
    for i in range(n):
        e={}
        e["code"]="P"+str(i+1)
        e["duree"]=int(input("duree:"))
        while not (e["duree"] >= 0):
            e["duree"]=int(input("duree:"))
        dump(e["f1"])
    f1.close()


def classer():
    t=array([{}]*200)
    transfert_1()
    tri()
    transfert_2()


def transfert_1():
    global t
    f1=open("Processus.dat", "rb")
    for i in range(n):
        e={}
        load(f, e)
        t[i]["code"]=e["code"]
        t[i]["duree"]=e["duree"]
    f1.close


def tri():
    global t
    for i in range(1, i):
        aux=t[i]
        j=i
        while (aux["duree"]< t[j-1]["duree"]) and (j > 0):
            t[j]=t[j-1]
            j -= 1
        t[j]=aux


def transfert_2():
    global f2
    f2=open("Ord_classer.dat", "wb")
    for i in range(n):
        dump(t[i], f2)
    f2.close()


def generer():
    global f3
    f1=open("Processus.dat", "rb")
    f2=open("Ord_classer.dat", "rb")
    f3=open("Ord_Nouv.txt", "w")
    eof1=False
    eof2=False
    while (not (eof1) and not(eof2)):
        e1=load(f1)
        e2=load(f2)
        if()
        f3.write(e1["code"])
    f2.close()
    f1.cose()
    f2=open("Ord_classer.dat","rb")
    eof2=False
    ch=load(f3)
    e=load(f2)
    while not(eof2 and ch!=e["nb"]):
        write(f3,ch+"\n")
    f2.close()
    f3.close()

# pp
saisir()
remplir()
classer()
generer()
