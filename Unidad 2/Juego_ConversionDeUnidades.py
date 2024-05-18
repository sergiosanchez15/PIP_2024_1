import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

class UnitConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertidor de unidades")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Mtros Input
        self.value_metros = QLineEdit()
        self.value_metros.setPlaceholderText("Ingrese metros")
        self.metros_label = QLabel("Metros:")
        self.metros_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #Layout metros input
        input_layout_metros = QHBoxLayout()
        input_layout_metros.addWidget(self.metros_label)
        input_layout_metros.addWidget(self.value_metros)
        
        #Celsius Input
        self.celsius_value = QLineEdit()
        self.celsius_value.setPlaceholderText("Ingrese grados Fahrenheit")
        self.celsius_label = QLabel("Grados Fahrenheit")
        self.celsius_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #Layout celsius input
        input_layout_celsius = QHBoxLayout()
        input_layout_celsius.addWidget(self.celsius_label)
        input_layout_celsius.addWidget(self.celsius_value)
        
        #Millas input
        self.value_millas = QLineEdit()
        self.value_millas.setPlaceholderText("Ingrese millas")
        self.millas_label = QLabel("Millas:")
        self.millas_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #Layout Input Millas
        input_layout_millas = QHBoxLayout()
        input_layout_millas.addWidget(self.millas_label)
        input_layout_millas.addWidget(self.value_millas)
        
        #Dolares input
        self.value_dolares = QLineEdit()
        self.value_dolares.setPlaceholderText("Ingrese numero de dolares")
        self.dolares_label = QLabel("Dolares:")
        self.dolares_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #Layout dolares input
        input_layout_dolares = QHBoxLayout()
        input_layout_dolares.addWidget(self.dolares_label)
        input_layout_dolares.addWidget(self.value_dolares)
        
        

        

        # Output widgets
        #Output Metros
        self.output_value_metros = QLabel("")
        self.output_metros_label = QLabel("Pies:")
        self.output_metros_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        output_layout_metros = QHBoxLayout()
        output_layout_metros.addWidget(self.output_metros_label)
        output_layout_metros.addWidget(self.output_value_metros)
        
        #Outut Celsius
        self.output_value_celsius = QLabel("")
        self.output_celsius_label = QLabel("Celsius:")
        self.output_celsius_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        output_layout_celsius = QHBoxLayout()
        output_layout_celsius.addWidget(self.output_celsius_label)
        output_layout_celsius.addWidget(self.output_value_celsius)
        
        #Output Millas
        self.output_value_kilometros = QLabel("")
        self.output_kilometros_label = QLabel("Kilometros:")
        self.output_kilometros_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        output_layout_kilometros = QHBoxLayout()
        output_layout_kilometros.addWidget(self.output_kilometros_label)
        output_layout_kilometros.addWidget(self.output_value_kilometros)
        
        #Output Celsius
        self.output_value_pesos = QLabel("")
        self.output_pesos_label = QLabel("Pesos:")
        self.output_pesos_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        output_layout_pesos = QHBoxLayout()
        output_layout_pesos.addWidget(self.output_pesos_label)
        output_layout_pesos.addWidget(self.output_value_pesos)



        # Conversion button
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert)
        
        #Input
        layout.addLayout(input_layout_metros)
        layout.addLayout(input_layout_celsius)
        layout.addLayout(input_layout_millas)
        layout.addLayout(input_layout_dolares)
        #Output
        layout.addLayout(output_layout_metros)
        layout.addLayout(output_layout_celsius)
        layout.addLayout(output_layout_kilometros)
        layout.addLayout(output_layout_pesos)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)
        
    def convert(self):
        self.convert_metros()
        self.convert_dolares()
        self.convert_fahrenheit()
        self.convert_millas()

    def convert_metros(self):
        try:
            print("hola mundo")
            value = float(self.value_metros.text())
            feet = value * 3.28084
            self.output_value_metros.setText(str(feet))
        except ValueError:
            self.output_value_metros.setText("Informacion Invalida")
            
    def convert_fahrenheit(self):
        try:
            value = float(self.celsius_value.text())
            celsius = (value - 32)*0.556
            self.output_value_celsius.setText(str(celsius))
        except ValueError:
            self.output_value_celsius.setText("Informacion Invalida")
    
    def convert_millas(self):
        try:
            value = float(self.value_millas.text())
            kilometros = value*1.69
            self.output_value_kilometros.setText(str(kilometros))
        except ValueError:
            self.output_value_kilometros.setText("Informacion Invalida")
            
    def convert_dolares(self):
        try:
            value = float(self.value_dolares.text())
            pesos = value*16.95
            self.output_value_pesos.setText(str(pesos))
        except ValueError:
            self.output_value_pesos.setText("Informacion Invalida")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = UnitConverter()
    converter.show()
    sys.exit(app.exec())
