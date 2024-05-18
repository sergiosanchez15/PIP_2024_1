import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.uic import loadUi
import random

class CalculadoraApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Juego_Operaciones.ui", self)

        self.generar_operacion()

        # Conectar señales a los botones
        self.pushButton_generar.clicked.connect(self.generar_operacion)
        self.pushButton_verificar.clicked.connect(self.verificar_respuesta)
        self.btn_borrar.clicked.connect(self.borrar_datos)

    def generar_operacion(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operadores = ['+', '-', '*', '/']
        operador = random.choice(operadores)

        self.label_operacion.setText(f"{num1} {operador} {num2} = ")
        self.respuesta_correcta = eval(f"{num1} {operador} {num2}")

    def verificar_respuesta(self):
        respuesta_usuario = self.lineEdit_respuesta.text()

        try:
            respuesta_usuario = float(respuesta_usuario)
            if respuesta_usuario == self.respuesta_correcta:
                self.label_resultado.setText("¡Sacaste 10!")

            else:
                self.label_resultado.setText("Sacaste 0")
        except ValueError:
            self.label_resultado.setText("Por favor, ingresa un número válido.")

    def borrar_datos(self):
        self.lineEdit_respuesta.clear()
        self.label_resultado.clear()
        self.label_operacion.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraApp()
    ventana.show()
    sys.exit(app.exec_())
