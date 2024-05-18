import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P15_DisplayControl.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.lcdNumber.setNumDigits(8)
        self.lcdNumber.display(1234567)

        #tarea: alarma_con display

        

    # Área de los Slots





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

