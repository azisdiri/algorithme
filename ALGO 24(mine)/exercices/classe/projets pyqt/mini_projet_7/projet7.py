def pascal():
    n=int(w.nbl.text())
    m=array([[int()]*n]*n)
    for i in range(n):
        ch=""
        for j in range(i):
            if (j==0) or (i==j):
                m[i,j]=1
            else:
                m[i,j]=m[i-1,j]+m[i-1,j-1]
            ch+=str(m[i,j])
        w.matrice.addItem(ch)
from numpy import array
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
app = QApplication([])
w = loadUi ("projet7.ui")
w.show()
w.boutt.clicked.connect (pascal)
app.exec_()