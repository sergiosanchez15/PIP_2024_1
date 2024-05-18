import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class MyWidget(QWidget):
    def __init__(self):
        self.lista = {'Cat A': [],'Cat B':[],'Cat C':[]}
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Calcular Compras')
        self.setGeometry(100, 100, 400, 150)

        layout = QVBoxLayout()

        self.ventas_label = QLabel('Monto de venta:')
        self.ventas_text = QLineEdit()
        
        self.total_label = QLabel('Total de compras:')
        self.total_text = QLineEdit()
        self.total_text.setReadOnly(True)
        
        self.numero_label = QLabel('Numero de compras:')
        self.numero_text = QLineEdit()
        self.numero_text.setReadOnly(True)
        
        self.agregar_button = QPushButton('Agregar Venta')
        self.agregar_button.clicked.connect(self.agregar)

        self.calculate_button = QPushButton('Calcular')
        self.calculate_button.clicked.connect(self.calculate)

        layout.addWidget(self.ventas_label)
        layout.addWidget(self.ventas_text)
        layout.addWidget(self.total_label)
        layout.addWidget(self.total_text)
        layout.addWidget(self.numero_label)
        layout.addWidget(self.numero_text)
        layout.addWidget(self.agregar_button)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)
        
    def agregar(self):
        
        valor = float(self.ventas_text.text())
        try:
            if valor >= 1000:
                self.lista['Cat A'].append(valor)
            elif valor >= 500 and valor <= 1000:
                self.lista['Cat B'].append(valor)
            elif valor <500:
                self.lista['Cat C'].append(valor)  
            self.ventas_text.setText("")          
        except ValueError:
            QMessageBox.warning(self,"Error","Ingrese numeros")

    def calculate(self):
        total = 0
        contador = [0,0,0]
        try:
            for k,v in self.lista.items():
                for compras in v:
                    total = compras + total
                if k == 'Cat A':
                    for compras in v:
                      contador[0]+=1
                elif k == 'Cat B':
                    for compras in v:
                       contador[1]+=1
                elif k == 'Cat C':
                    for compras in v:
                        contador[2]+=1
            self.total_text.setText(f"Total de compras {total}")
            self.numero_text.setText(f"Numero de compras de cada categoria son: Cat A: {contador[0]}, Cat B: {contador[1]}, Cat C: {contador[2]}")
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Ingrese numeros.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
