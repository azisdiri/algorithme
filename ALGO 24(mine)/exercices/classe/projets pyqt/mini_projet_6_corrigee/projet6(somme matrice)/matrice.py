"""Remarque pour vous:pour cette solution on a remplir directe widget tablewidget sans l'utilisation de type array de la bibliothèque numpy"""
def Former_Matrice():
    global l,c
    ch1=window.t1.text()
    ch2=window.t2.text()
    if ch1=="" or ch2=="" or not(ch1.isdecimal()) or not(ch2.isdecimal()):
        window.msg.setText("Verifiez les valeurs saisies :'Nombre de lignes ou de colnnes invalide'")
    else:
        l=int(ch1)
        c=int(ch2)
        window.matrice.setRowCount(l)
        window.matrice.setColumnCount(c)
        
        for i in range (l):
            for j in range(c):
                window.matrice.setItem(i,j,QTableWidgetItem(str(randint(10,100))))

   
def remplir_t():
    window.tableau.setRowCount(1)
    window.tableau.setColumnCount(l)
    for i in range(l):
        s=somme(i,c)
        window.tableau.setItem(0,i,QTableWidgetItem(str(s)))
            
def somme(l,c):
    s=0
    for i in range(c):
        s=s+int(window.matrice.item(l,i).text())
    return(s)
    
        
def initialiser():
    window.msg.clear()
    window.t1.clear()
    window.t2.clear()
    window.matrice.setRowCount(0)
    window.matrice.setColumnCount(0)
    window.tableau.setRowCount(0)
    window.tableau.setColumnCount(0)
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from random import *
app=QApplication([])
window=loadUi("matrice.ui")

window.former.clicked.connect(Former_Matrice)
window.afficher.clicked.connect(remplir_t)
window.reset.clicked.connect(initialiser)
window.show()
app.exec()