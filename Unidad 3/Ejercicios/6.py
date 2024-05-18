import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reporte de Kilómetros Recorridos por Choferes")
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()

        self.input_label = QLabel("Ingrese el nombre del chofer y los kilómetros recorridos (separados por comas):")
        layout.addWidget(self.input_label)

        self.input_text = QLineEdit()
        layout.addWidget(self.input_text)

        self.add_button = QPushButton("Agregar")
        self.add_button.clicked.connect(self.add_entry)
        layout.addWidget(self.add_button)

        self.report_label = QLabel("Reporte:")
        layout.addWidget(self.report_label)

        self.report_text = QTextEdit()
        layout.addWidget(self.report_text)

        self.setLayout(layout)

        self.drivers = {}

    def add_entry(self):
        entry = self.input_text.text().split(',')
        driver_name = entry[0].strip()
        for i in range(7):
          kilometers = int(entry[i].strip())

        if driver_name not in self.drivers:
            self.drivers[driver_name] = {'Lunes': kilometers[1], 'Martes': kilometers[2], 'Miercoles': kilometers[3], 'Jueves': kilometers[4], 'Viernes': kilometers[5], 'Sabado': kilometers[6], 'Domingo': kilometers[7], 'Total': 0}

        self.drivers[driver_name]['Total'] += (float(self.drivers['Lunes'])+float(self.drivers['Martes'])+float(self.drivers['Miercoles'])+float(self.drivers['Jueves'])+float(self.drivers['Viernes'])+float(self.drivers['Sabado'])+float(self.drivers['Domingo']))

        day_index = len(self.drivers[driver_name]) - 1
        day = self.getDayOfWeek(day_index)
        self.drivers[driver_name][day] = kilometers

        self.update_report()

    def update_report(self):
        report = "Nombre del Chofer | Lunes | Martes | Miércoles | Jueves | Viernes | Sábado | Domingo | Total Semanal\n"
        for driver, data in self.drivers.items():
            report += f"{driver:<18} | {data['Monday']:<5} | {data['Tuesday']:<6} | {data['Wednesday']:<9} | {data['Thursday']:<6} | {data['Friday']:<7} | {data['Saturday']:<6} | {data['Sunday']:<7} | {data['Total']}\n"
        self.report_text.setPlainText(report)

    def getDayOfWeek(self, dayIndex):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[min(dayIndex, len(days)-1)]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
