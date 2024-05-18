import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer

class TemporizadorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Juego_Temporizador.ui", self)  # Carga la interfaz desde el archivo .ui
        self.btn_iniciar.clicked.connect(self.iniciar_temporizador)

    def iniciar_temporizador(self):
        duracion_temporizador = int(self.lineEdit.text())
        tiempo_inicial = time.time()
        tiempo_final = tiempo_inicial + duracion_temporizador

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.actualizar_temporizador(tiempo_final))
        self.timer.start(1000)  # Actualizar cada segundo

    def actualizar_temporizador(self, tiempo_final):
        tiempo_restante = int(tiempo_final - time.time())
        self.label.setText(f"Tiempo restante: {tiempo_restante} segundos")

        if tiempo_restante <= 0:
            self.timer.stop()
            self.label.setText("¡Tiempo terminado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TemporizadorApp()
    ventana.show()
    sys.exit(app.exec_())
