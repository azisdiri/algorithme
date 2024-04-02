


def affchance():
    f = open("chance.txt", 'r')
    ch = f.readline()
    while ch != "":
        w.chan.addItem(ch)
        ch = f.readline()
    f.close()


def ajouter():
    id = w.id.text()
    ntel = w.ntel.text()
    ville = w.ville.currentText()
    genre = ""
    if w.m.isChecked():
        genre = "Masculin"
    else:
        genre = "Feminin"
    etat = ""
    if w.ins.isChecked():
        etat = "Inscrit"
    else:
        etat = "Non Inscrit"
    e = {}
    e["id"] = id
    e["ntel"] = ntel
    e["ville"] = ville
    e["genre"] = genre
    e["etat"] = etat
    f1 = open("clients.dat", "ab")
    dump(e, f1)
    


def affclient():
    w.c.setColumnCount(5)
    f1 = open("clients.dat", "rb")
    i = 0
    eof = False
    while not eof:
        try:
            e = load(f1)
            w.c.insertRow(i)
            w.c.setItem(i, 0, QTableWidgetItem(e["id"]))
            w.c.setItem(i, 1, QTableWidgetItem(e["ntel"]))
            w.c.setItem(i, 2, QTableWidgetItem(e["ville"]))
            w.c.setItem(i, 3, QTableWidgetItem(e["genre"]))
            w.c.setItem(i, 4, QTableWidgetItem(e["etat"]))
            i += 1
        except:
            eof =True 
    f1.close()
   
   
def calcul(ch):
    s=0
    for i in range(len(ch)):
        s+=int(ch[i])
    while s>9:
        ch=str(s)
        s=0
        for i in range(len(ch)):
            s+=int(ch[i])
    return str(s)
   
   
def existe(ch):
    f=open("chance.txt","r")
    ch1=f.readline()
    ok = False
    while ch1!="":
        if(ch1==ch):
            ok = True
        ch1=f.readline()
    return ok
            
    
   
def affgagnants():
    w.gag.addItem("les clients gagnants sont:")
    f1=open("clients.dat","rb")
    eof=False
    while not eof:
        try:
            e=load(f1)
            res=calcul(e["ntel"])
            if existe(res):
                w.gag.addItem("id:"+e["id"]+" ntel:"+e["ntel"])
        except:
            eof=True
    f1.close()
    

# pp
from pickle import load, dump
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
app = QApplication([])
w = loadUi("prototype.ui")
w.show()
w.aff_chan.clicked.connect(affchance)
w.ajouter.clicked.connect(ajouter)
w.aff_cli.clicked.connect(affclient)
w.aff_gag.clicked.connect(affgagnants)
app.exec_()
