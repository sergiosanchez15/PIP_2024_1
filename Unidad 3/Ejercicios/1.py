import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Calcular Salario')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.horas_trabajadas_label = QLabel('Horas Trabajadas:')
        self.horas_text = QLineEdit()

        self.sueldo_hora_label = QLabel('Sueldo por hora:')
        self.sueldo_hora_text = QLineEdit()

        self.result_label = QLabel('Salario Semanal:')
        self.result_text = QLineEdit()
        self.result_text.setReadOnly(True)

        self.calculate_button = QPushButton('Calcular')
        self.calculate_button.clicked.connect(self.calculate)

        layout.addWidget(self.horas_trabajadas_label)
        layout.addWidget(self.horas_text)
        layout.addWidget(self.sueldo_hora_label)
        layout.addWidget(self.sueldo_hora_text)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate(self):
        try:
            horas = float(self.horas_text.text())
            sueldo_hora = float(self.sueldo_hora_text.text())
            result = (horas * sueldo_hora) *6
            self.result_text.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Please enter valid numbers.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
