import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P6_HorizontalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_integrantes = {
            1: ["Angel", "Futbol", 20, "O+", ":/logos/Angel.jpeg"],
            2: ["Jorge", "Juegos", 20, "O+", ":/logos/Jorge.png"],
            3: ["Paniagua", "Chambear", 20, "O+", ":/logos/Paniagua.jpeg"],
            4: ["Sheko", "Gym", 22, "O+", ":/logos/Sheko.jpeg"]
        }

        self.hs_integrantes.setMinimum(1)
        self.hs_integrantes.setMaximum(4)
        self.hs_integrantes.setSingleStep(1)
        self.hs_integrantes.setValue(1)
        self.hs_integrantes.valueChanged.connect(self.cambia)

    def cambia(self):
        dataClave = self.hs_integrantes.value()
        print(dataClave)
        imagen = self.datos_integrantes[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

