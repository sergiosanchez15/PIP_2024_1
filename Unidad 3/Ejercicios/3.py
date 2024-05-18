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

        self.meses_label = QLabel('Meses a pagar:')
        self.meses_text = QLineEdit()

        self.result_label = QLabel('Total Pagado:')
        self.result_text = QLineEdit()
        self.result_text.setReadOnly(True)
        
        self.pago_mensual_label = QLabel('Pagos Mensuales:')
        self.pago_mensual_text = QLineEdit()
        self.pago_mensual_text.setReadOnly(True)

        self.calculate_button = QPushButton('Calcular')
        self.calculate_button.clicked.connect(self.calculate)

        layout.addWidget(self.meses_label)
        layout.addWidget(self.meses_text)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)
        layout.addWidget(self.pago_mensual_label)
        layout.addWidget(self.pago_mensual_text)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate(self):
        lista_meses = {}
        mes = 10
        try:
            meses = int(self.meses_text.text())
            for i in range(meses):
                lista_meses[f'Mes: {i}'] = mes
                mes = mes*2
            self.pago_mensual_text.setText(f"Pago Mensual:{lista_meses}")
            self.result_text.setText(f"Pago Total: {mes}")
        except ValueError:
            print(ValueError.with_traceback())
            QMessageBox.warning(self, 'Error', 'Ingrese numeros.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
