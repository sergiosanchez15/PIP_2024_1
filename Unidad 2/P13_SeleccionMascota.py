import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P13_SeleccionMascota.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_angel.clicked.connect(self.clic_angel)
        self.rb_angel.toggled.connect(self.toggle_angel)


    # Área de los Slots
    def clic_angel(self):
        print ("hiciste print a angel")
    def toggle_angel(self):

        estado = self.rb_angel.isChecked()
        print("angel cambio de estado(toggle). Nuevo Estado: {estado}")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

