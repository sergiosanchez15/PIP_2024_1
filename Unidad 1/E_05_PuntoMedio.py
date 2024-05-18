import sys
import math
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_05_PuntoMedio.ui"  # Nombre del archivo aquí.
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
        Punto1 = []
        Punto2 = []
        Punto1.append(float(self.txtX1.text()))
        Punto1.append(float(self.txtY1.text()))
        Punto2.append(float(self.txtX2.text()))
        Punto2.append(float(self.txtY2.text()))
        Xmedia = (Punto1[0] + Punto2[0]) / 2
        Ymedia = (Punto1[1] + Punto2[1]) / 2
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText("({0}, {1})".format(Xmedia, Ymedia))
        messageBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())