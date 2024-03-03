def saisir_eleve():
    ch1=f.zone2.text()
    ch2=f.zone3.text()
    ch3=f.zone4.text()
    if len(ch1)!=10 or ch1.isdecimal()==False:
        QMessageBox.critical(f,"ERROR","saisir un identifiant valide(10 chiffres)!!!")
        f.zone2.clear()
    elif ch2=="":
        QMessageBox.critical(f,"ERROR","saisir un nom valide!!!")
        f.zone3.clear()
    elif ch3=="" or not(0.0<=float(ch3)<=20.0):
        QMessageBox.critical(f,"ERROR","saisir une moyenne valide!!!")
        f.zone4.clear()
    else:
        n=f.table.rowCount()
        f.table.insertRow(n)
        f.table.setItem(n,0,QTableWidgetItem(str(n+1)))
        f.table.setItem(n,1,QTableWidgetItem(ch1))
        f.table.setItem(n,2,QTableWidgetItem(ch2))
        f.table.setItem(n,3,QTableWidgetItem(f.comboBox.currentText()))
        f.table.setItem(n,4,QTableWidgetItem(ch3))
        ch1=f.zone2.clear()
        ch2=f.zone3.clear()
        ch3=f.zone4.clear()


#programme principal
from PyQt5.uic import*
from PyQt5.QtWidgets import *
app=QApplication([])
f=loadUi("projet9.ui")
f.ajouter.clicked.connect(saisir_eleve)
f.show()
app.exec()