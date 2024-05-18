import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
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

        self.combo_persona.addItem("Angel", 1)
        self.combo_persona.addItem("Jorge", 2)
        self.combo_persona.addItem("Paniagua", 3)
        self.combo_persona.addItem("Sheko", 4)

        self.combo_persona.currentIndexChanged.connect(self.cambia)

    def cambia(self):
        print("Text: " + self.combo_persona.currentText())
        print("Index: " + str(self.combo_persona.currentIndex()))
        print("Data: " + str(self.combo_persona.currentData()))

        dataClave = self.combo_persona.currentData()
        imagen = self.datos_integrantes[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


