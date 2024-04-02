from pickle import load, dump
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *


def creer():
    f = open("employes.dat", "wb")
    f.close()


def alpha(ch):
    i = 0
    while (i <= len(ch)-1) and ("A" <= ch[i].upper() <= "Z"):
        i += 1
    return i == len(ch)


def ajouter():
    id = w.id.text()
    nomp = w.nomp.text()
    ville = w.ville.currentText()
    sco = int(w.sco.text())
    if not (len(id) == 4 and id.isdecimal()):
        QMessageBox.warning(w, "erreur", "id invalide")
    elif not (sco >= 20 and sco <= 150):
        QMessageBox.warning(w, "erreur", "score invalide")
    elif w.m.isChecked() == False and w.f.isChecked() == False:
        QMessageBox.warning(w, "erreur", "choisir un genre")
    elif (not alpha(w.nomp)):
        QMessageBox.warning(w, "erreur", "nom et prenom invalides")
    else:
        f = open("employes.dat", "ab")
        if w.m.isChecked():
            genre = "Masculin"
        else:
            genre = "Feminin"
        e = dict(id=id, nomp=nomp, genre=genre, ville=ville, sco=sco)
        dump(e, f)
        QMessageBox.information(w, "ajout", "employee ajoute avec succes")
        f.close()


def aff_employes():
    f = open("employes.dat", "rb")
    eof = False
    i = 0
    while not eof:
        try:
            w.table.insertRow(i)
            e = load(f)
            w.table.setItem(i, 0, QTableWidgetItem(e["id"]))
            w.table.setItem(i, 1, QTableWidgetItem(e["nomp"]))
            w.table.setItem(i, 2, QTableWidgetItem(e["genre"]))
            w.table.setItem(i, 3, QTableWidgetItem(e["ville"]))
            w.table.setItem(i, 4, QTableWidgetItem(e["sco"]))
            i+=1

        except:
            eof = True
    f.close()

def gagnants():
    f=open("employes.dat","rb")
    eof = False
    n=0
    t=array([int()]*10)
    while not eof:
        try :
            e=load(f)
            t[n]=e["sco"]
            n+=1
        except :
            eof=True
    f.close()
    trier(t,n)
    f=open("employes.dat","rb")


# pp
from pickle import load,dump
from numpy import array
app = QApplication([])
w = loadUi("projet10.ui")
w.show()
w.bt1.clicked.connect(creer)
w.bt3.clicked.connect(ajouter)
w.bt6.clicked.connect(aff_employes)
w.bt7.clicked.connect(gagnants)
app.exec_()
