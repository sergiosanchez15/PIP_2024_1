import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Calcular Mensualidades')
        self.setGeometry(100, 100, 800, 200)

        layout = QVBoxLayout()

        self.num_empleados = QLabel('Numero de empleados:')
        self.num_empleados_text = QLineEdit()

        self.horas_label = QLabel('Horas trabajadas:')
        self.horas_text = QLineEdit()
        
        self.pago_hora_label = QLabel('Pago por hora:')
        self.pago_hora = QLineEdit()
        
        self.resultado_label = QLabel('Resultado')
        self.resultado_text = QLineEdit()
        self.resultado_text.setReadOnly(True)

        self.calculate_button = QPushButton('Calcular')
        self.calculate_button.clicked.connect(self.calculate)

        layout.addWidget(self.num_empleados)
        layout.addWidget(self.num_empleados_text)
        layout.addWidget(self.horas_label)
        layout.addWidget(self.horas_text)
        layout.addWidget(self.pago_hora_label)
        layout.addWidget(self.pago_hora)
        layout.addWidget(self.resultado_label)
        layout.addWidget(self.resultado_text)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate(self):
        self.resultado_text.setText(str(float(self.horas_text.text())*float(self.num_empleados_text.text())*float(self.pago_hora.text())))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
