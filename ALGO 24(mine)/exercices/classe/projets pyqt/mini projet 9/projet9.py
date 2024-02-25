from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
def annuler():
    w.id.clear()
    w.np.clear()
    w.moy.clear()


app = QApplication([])
w = loadUi ("projet9.ui")
w.show()
w.supprimer.clicked.connect(annuler)
app.exec_()