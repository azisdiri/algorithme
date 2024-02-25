0lfrom pickle import *

def rech(f1,chn):
    f1 = open("Codes_braille.dat","rb")
    e = load(f1)
    fin_fichier = False
    while (fin_fichier == False) and (e["codage"] != chn):
        try:
            e = load(f1)
        except:
            fin_fichier =True

def convert(f1,phrase):
    res = ''
    phrase1=phrase
    while (phrase1!=''):
        res = res + rech(f1,phrase1[0:7])
        phrase1 = phrase1[7:]
    return res+""
    

def afficher():
    f2 = open("Braille.txt","r")
    mot = ""
    ch = f2.readline()
    while ch!='':
        ch1 = ch1+convert(f1,ch)
        ch = f2.readline()
    f1.close()
    f2.close()
    print(ch1)

#PP
afficher()