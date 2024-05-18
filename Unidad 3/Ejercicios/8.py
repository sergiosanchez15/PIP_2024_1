import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cálculo de Costo de Viaje de Estudios")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_alumnos = QLabel("Número de alumnos:")
        self.input_alumnos = QLineEdit()
        layout.addWidget(self.label_alumnos)
        layout.addWidget(self.input_alumnos)

        self.calculate_button = QPushButton("Calcular Costo")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Costo para cada alumno:")
        layout.addWidget(self.result_label)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def calculate(self):
        try:
            num_alumnos = int(self.input_alumnos.text())
            costo_por_alumno, costo_total = self.calcular_costo(num_alumnos)
            self.result_text.setPlainText(f"Costo por alumno: ${costo_por_alumno:.2f}\nCosto total del viaje: ${costo_total:.2f}")
        except ValueError:
            self.result_text.setPlainText("Error: Por favor ingrese un número válido de alumnos.")

    def calcular_costo(self, num_alumnos):
        if num_alumnos >= 100:
            costo_por_alumno = 65.0
        elif 50 <= num_alumnos <= 99:
            costo_por_alumno = 70.0
        elif 30 <= num_alumnos <= 49:
            costo_por_alumno = 95.0
        else:
            costo_por_alumno = 4000.0 / num_alumnos
        
        costo_total = costo_por_alumno * num_alumnos
        return costo_por_alumno, costo_total


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
