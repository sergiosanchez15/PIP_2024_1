import sys
import math
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_03_Distancia2Puntos.ui"  # Nombre del archivo aquí.
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
        print(Punto1)
        print(Punto2)
        distancia = math.sqrt((Punto2[0] - Punto1[0])**2 + (Punto2[1] - Punto1[1])**2)
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText(str(distancia))
        messageBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())