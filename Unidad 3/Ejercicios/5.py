import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control de Existencia de Productos")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.input_a_label = QLabel("Vector A (separado por comas):")
        self.input_a = QLineEdit()
        layout.addWidget(self.input_a_label)
        layout.addWidget(self.input_a)

        self.input_b_label = QLabel("Vector B (separado por comas):")
        self.input_b = QLineEdit()
        layout.addWidget(self.input_b_label)
        layout.addWidget(self.input_b)

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)

        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def calculate(self):
        vector_a = list(map(int, self.input_a.text().split(',')))
        vector_b = list(map(int, self.input_b.text().split(',')))

        vector_c = []

        for a, b in zip(vector_a, vector_b):
            if a == b:
                vector_c.append(a)
            elif b > a:
                vector_c.append(b - a)
            else:
                vector_c.append(b * 2)

        self.result_text.setPlainText(','.join(map(str, vector_c)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
