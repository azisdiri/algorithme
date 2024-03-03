from pickle import *
from numpy import array


def conv_decimal(Hex):
    puiss = 1
    s = 0
    for i in range(len(Hex)-1, -1, -1):
        if ("A,B,C,D,E,F".find(Hex[i]) != -1):
            s += puiss * (ord(Hex[i]) - 55)
        else:
            s += int(Hex[i]) * puiss
        puiss *= 16
    return s


def transfert_1():
    global f, t, n
    n = 0
    f = open("ImgHexa.txt", "r")
    eof = False
    while not eof:
        try:
            ch = f.readline()
            t[n]["Hex"] = ch
            t[n]["Num"] = n
            t[n]["Dec"] = conv_decimal(ch)
            n += 1
        except:
            eof = True
    f.close()


def tri():
    global t
    for i in range(n-1):
        posmin = i
        for j in range(i+1, n):
            if (t[j]["Dec"] < t[posmin]["Dec"]):
                posmin = j
        if i != posmin:
            aux = t[i]
            t[i] = t[posmin]
            t[posmin] = aux


def genere(nb):
    mot = ""
    while nb != 0:
        r = nb % 3
        y = ""
        match r:
            case 0: y = "Ma"
            case 1: y = "Des"
            case 2: y = "Son"
        mot += y
        nb = nb//3
    return mot


def crypter():
    global f1
    f1 = open("Resultat.txt", "w")
    for i in range(n):
        ch = (genere(t[i]["Dec"])+str(t[i]["Num"]))
        f1.write(ch+"\n")
    f1.close()


# pp
t = array([{}]*200)
transfert_1()
tri()
crypter()
