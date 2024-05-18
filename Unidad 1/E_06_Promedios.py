import sys

import numpy
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_06_Promedios.ui"  # Nombre del archivo aquí.
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
        calificaciones = []
        calificaciones.append(float(self.txtCAL1.text()))
        calificaciones.append(float(self.txtCAL2.text()))
        calificaciones.append(float(self.txtCAL3.text()))
        calificaciones.append(float(self.txtCAL4.text()))
        calificaciones.append(float(self.txtCAL5.text()))
        promedio = numpy.average(calificaciones)
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText(str(promedio))
        messageBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())