from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem


def vider():
    w.a.clear()
    w.b.clear()
    w.nb_premier.clear()
    w.facteur_premier.clear()
    w.label1.setText("")
    w.label2.setText("")
    w.label3.setText("")


def pgcd(a, b):
    while (a != b):
        if a < b:
            b -= a
        else:
            a -= b
    return a


def ppcm(a, b):
    a1 = a
    b1 = b
    while (a1 != b1):
        if a1 > b1:
            b1 += b
        else:
            a1 += a
    return a


def resultat():
    a = w.a.text()
    b = w.b.text()
    if (a != "" and b != "" and a >= "0" and a <= "9" and b >= "0" and b <= "9"):
        a = int(w.a.text())
        b = int(w.b.text())
        if w.liste.currentText() == "pgcd":
            w.label1.setText(str(pgcd(a, b)))
        else:
            w.label1.setText(str(ppcm(a, b)))
    else:
        QMessageBox.critical(
            w, "Attention", "a et b doivent être remplis correctement")


def premier():
    ch = w.nb_premier.text()
    x = int(w.nb_premier.text())
    if (ch != "" and x > 0):
        i = 2
        while (i <= x//2) and (x % i != 0):
            i += 1
        if i > x//2:
            w.label2.setText(("vrai"))
        else:
            w.label2.setText(("faux"))
    else:
        QMessageBox.critical(w, "Attention", "donner un nombre positif")


def facteurs_premiers():
    ch1 = w.facteurs_premiers.text()
    x = int(w.facteurs_premiers.text())
    if (ch1 != "" and x > 0):
        ch = ""
        i = 2
        while (x != 1):
            if (x % i == 0):
                ch = ch+str(i)+"*"
                x = x//i
            else:
                i += 1
        w.label3.setText(ch[:len(ch)-1])
    else:
        QMessageBox.critical(w, "Attention", "donner un nombre positif")


app = QApplication([])
w = loadUi("mini_projet_3.ui")
w.show()
w.annuler.clicked.connect(vider)
w.quitter.clicked.connect(w.close)
w.res1.clicked.connect(resultat)
w.res2.clicked.connect(premier)
w.res3.clicked.connect(facteurs_premiers)
app.exec_()
