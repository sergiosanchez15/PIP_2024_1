import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Presupuesto de Banquete")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_personas = QLabel("Número de personas:")
        self.input_personas = QLineEdit()
        layout.addWidget(self.label_personas)
        layout.addWidget(self.input_personas)

        self.calculate_button = QPushButton("Calcular Presupuesto")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Presupuesto:")
        layout.addWidget(self.result_label)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def calculate(self):
        try:
            num_personas = int(self.input_personas.text())
            costo_por_platillo = self.calcular_costo(num_personas)
            presupuesto_total = num_personas * costo_por_platillo
            self.result_text.setPlainText(f"Presupuesto para {num_personas} personas: ${presupuesto_total:.2f}")
        except ValueError:
            self.result_text.setPlainText("Error: Por favor ingrese un número válido de personas.")

    def calcular_costo(self, num_personas):
        if num_personas <= 200:
            return 95.0
        elif num_personas <= 300:
            return 85.0
        else:
            return 75.0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
