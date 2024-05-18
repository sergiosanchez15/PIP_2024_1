import math
import sys

import numpy
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_08_Calificacion.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnCalcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        calificacion = float(self.txtNumero.text())
        if calificacion == 10:
            nota = 'A'
        elif calificacion >= 9:
            nota = 'B'
        elif calificacion >= 8:
            nota = 'C'
        elif calificacion >= 7:
            nota = 'D'
        elif calificacion >= 6:
            nota = 'E'
        else:
            nota = 'F'
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText(nota)
        messageBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())