def remplir():
    ch=f.nb.text()
    if ch.isdecimal()==False or ch=="" or ch=="0":
        QMessageBox.critical(f,"Error","l'entier doit être strictement positif!!!")
    else:
        n=int(ch)
        for l in range(n):
            for c in range(l+1):
                if(l==c)or(c==0):
                    m[l,c]=1
                else:
                    m[l,c]=m[l-1,c]+m[l-1,c-1]
        f.aff.clear()
        for l in range(n):
            ch=""
            for c in range(l+1):
                ch=ch+str(m[l,c])+" "
            f.aff.addItem(ch)
def annuler():
    f.nb.clear()
    f.aff.clear()
    
#connexion avec qt designer et appel des méthodes
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from numpy import*
m=array([[int]*20]*20)
app=QApplication([])
f=loadUi("projet70.ui")
f.b1.clicked.connect(remplir)
f.b2.clicked.connect(annuler)
f.show()
app.exec_()