from random import randint
from PyQt5.uic import *
from PyQt5.QtWidgets import *


def former():
    global t, n
    if (w.n.text().isdigit()):
        n = int(w.n.text())
        t = [int()]*n
        ch = "|"
        for i in range(n):
            t[i] = randint(10, 99)
            ch += str(t[i])+" |"
        w.label1.setText(ch)
    else:
        QMessageBox.critical(w,"alert",'n!!!')
        w.n.setText("")
    
def reset():
    w.label1.clear()
    w.label2.clear()
    w.label3.clear()
    w.label4.clear()
    w.label5.clear()
    w.n.clear()
    w.x.clear()


def somme():
    s = 0
    for i in range(n):
        s += t[i]
    w.label2.setText(str(s))
    
def maximum():
    maxi=t[0]
    for i in range(n):
        if t[i]>maxi:
            maxi=t[i]
    w.label2.setText(str(maxi))

def minimum():
    mini=t[0]
    for i in range(n):
        if mini>t[i]:
            mini=t[i]
    w.label2.setText(str(mini))
        
      
def rech_seq():
    if(w.x.text()!=''and w.x.text().isdecimal()):
        x=int(w.x.text())
        i=0
        while(i<=n-1)and(x!=t[i]):
            i+=1
        if(i==n):
            w.label3.setText("n'existe pas")
        else:
            w.label3.setText("existe")
    else:
        QMessageBox.critical(w,"attention","x entier!")
        
def tri_croissant():
    ch = "|"
    permut=True
    while permut:
        permut=False
        for i in range(n-1):
            if t[i]>t[i+1]:
                t[i],t[i+1]=t[i+1],t[i]
                permut=True
    for i in range(n):
        ch+=str(t[i])+"|"
    w.label4.setText(ch)
    
                
def tri_decroissant():
    ch = "|"
    permut=True
    while permut:
        permut=False
        for i in range(n-1):
            if t[i]<t[i+1]:
                t[i],t[i+1]=t[i+1],t[i]
                permut=True
    for i in range(n):
        ch+=str(t[i])+"|"
    w.label5.setText(ch)
    
app = QApplication([])
w = loadUi("mini_projet_4.ui")
w.show()
w.tab.clicked.connect(former)
w.somme.clicked.connect(somme)
w.maximum.clicked.connect(maximum)
w.minimum.clicked.connect(minimum)
w.resultat.clicked.connect(rech_seq)
w.croissant.clicked.connect(tri_croissant)
w.decroissant.clicked.connect(tri_decroissant)
w.reset.clicked.connect(reset)
app.exec_()
