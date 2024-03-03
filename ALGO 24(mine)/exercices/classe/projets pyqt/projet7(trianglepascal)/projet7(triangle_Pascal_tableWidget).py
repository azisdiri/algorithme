def remplir():
    ch=f.nb.text()
    if ch.isdecimal()==False or ch=="" or ch=="0":
        QMessageBox.critical(f,"Error","l'entier doit être strictement positif!!!")
    else:
        n=int(ch)
        f.table.setColumnCount(n)
        f.table.setRowCount(n)
        for l in range(n):
            for c in range(l+1):
                if(l==c)or(c==0):
                    f.table.setItem(l,c,QTableWidgetItem("1"))
                else:
                    v1=int(f.table.item(l-1,c).text())
                    v2=int(f.table.item(l-1,c-1).text())
                    f.table.setItem(l,c,QTableWidgetItem(str(v1+v2)))
#connexion avec qt designer et appel des méthodes
from PyQt5.uic import*
from PyQt5.QtWidgets import *
app=QApplication([])
f=loadUi("projet71.ui")
f.b1.clicked.connect(remplir)
f.show()
app.exec()