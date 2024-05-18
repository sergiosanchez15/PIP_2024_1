import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.txt_equipo.setPlainText ("hola \n mundo")
        #self.cb_angel.clicked.connect(self.sel_angel)
        self.cb_angel.toggled.connect(self.sel_angel)
        self.cb_jorge.toggled.connect(self.sel_jorge)
        self.cb_paniagua.toggled.connect(self.sel_paniagua)
        self.cb_sheko.toggled.connect(self.sel_sheko)

        self.angel = ""
        self.jorge = ""
        self.paniagua = ""
        self.sheko = ""


    # Área de los Slots

    def sel_angel(self):
        if self.cb_angel.isChecked():
            print ("angel true")
            self.angel = "angel\n"
        else:
            print ("angel False")
            self.angel = ""
        self.txt_equipo.setPlainText(self.angel + self.jorge + self.paniagua + self.sheko )
    def sel_jorge(self):
        if self.cb_jorge.isChecked():
            print("jorge true")
            self.jorge = "jorge\n"
        else:
            print("jorge False")
            self.jorge = ""
        self.txt_equipo.setPlainText(self.angel + self.jorge + self.paniagua + self.sheko)
    def sel_paniagua(self):
        if self.cb_paniagua.isChecked():
            print("paniagua true")
            self.paniagua = "paniagua\n"
        else:
            print("paniagua False")
            self.paniagua = ""
        self.txt_equipo.setPlainText(self.angel + self.jorge + self.paniagua + self.sheko)
    def sel_sheko(self):
        if self.cb_sheko.isChecked():
            print("sheko true")
            self.sheko = "sheko\n"
        else:
            print("sheko False")
            self.sheko = ""
        self.txt_equipo.setPlainText(self.angel + self.jorge + self.paniagua + self.sheko)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

