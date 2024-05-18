import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QMessageBox,QVBoxLayout,QPushButton
from PyQt6.QtCore import Qt, QTimer,QRect
from PyQt6.QtGui import QPainter, QColor,QDesktopServices,QPixmap
import random

# Global variables
player_health = 50
player_position = (0, 0)  # Initialize player position
enemy_positions = []

def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        self.setGeometry(QRect(screen_geometry.width() // 2 - self.width() // 2,
                               screen_geometry.height() // 2 - self.height() // 2,
                               self.width(), self.height()))

class StartScreen(QWidget):
    def __init__(self, game_widget):
        super().__init__()
        self.game_widget = game_widget
        self.initUI()

    def initUI(self):
        pixmap = QPixmap("vampire_survivors.jpeg")  # Adjust the path to your image file
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)
        
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        #self.setGeometry(QRect(QApplication.primaryScreen().geometry))
        self.setStyleSheet("background-color: grey")
        center(self)
        
        
        #title_label = QLabel("Proyecto Interfaces")
        #title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #title_label.setStyleSheet("background-color: grey")
        
        
        start_button = QPushButton("Start Game")
        start_button.setStyleSheet("background-color: green")
        start_button.clicked.connect(self.start_game)
        
        
        layout.addWidget(background_label)
        #layout.addWidget(title_label)
        layout.addWidget(start_button)

    def start_game(self):
        self.game_widget.showFullScreen()
        self.hide()
class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.rows, self.columns = 17, 30
        self.player_position = (self.rows // 2, self.columns // 2)
        self.enemy_positions = self.generate_enemy_positions(80)
        self.finish_line_position = (self.rows - 1, self.columns - 1)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Proyecto Interfaces')
        self.grid_layout = QGridLayout(self)
        self.setLayout(self.grid_layout)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.keyPressEvent = self.handle_key_press
        self.timer = QTimer()
        #self.start_time = QTimer()
        #self.start_time.timeout.connect(self.update_timer2)
        #self.start_time = None
        self.start_time = time.time()
        self.timer.timeout.connect(self.check_enemy_interactions)
        self.timer.start(300)
        #self.resize(800, 800) 
        #self.setGeometry(QRect(QApplication.primaryScreen().geometry))
        #self.create_map()
        self.show()
    def create_quit_button(self):
        quit_button = QPushButton("Salir")
        quit_button.setStyleSheet("background-color: red")
        quit_button.clicked.connect(self.close())
        self.grid_layout.addWidget(quit_button, self.rows, 0, 1, self.columns)
    def update_timer2(self):
        pass
    def generate_enemy_positions(self, num_positions):
        positions = []
        middle_row = self.rows // 2
        middle_column = self.columns // 2
        middle_area_size = 1

        while len(positions) < num_positions:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)

            if not (middle_row - middle_area_size <= x <= middle_row + middle_area_size and
                    middle_column - middle_area_size <= y <= middle_column + middle_area_size):
                pos = (x, y)
                if pos not in positions:
                    positions.append(pos)

        return positions

    def create_map(self):
        for i in range(self.rows):
            for j in range(self.columns):
                label = QLabel()
                label.setStyleSheet('border: 1px solid blue; padding: 1px; background-color: white')
                self.grid_layout.addWidget(label, i, j)

        for pos in self.enemy_positions:
            x, y = pos
            label = QLabel('>:(')  
            label.setStyleSheet('border: 1px solid yellow; padding: 5px; background-color: red; color: white;')
            self.grid_layout.addWidget(label, x, y)

        self.spawn_player()

    def spawn_player(self):
        x, y = self.player_position
        label = QLabel(f'{player_health}')
        label.setStyleSheet("border: 1px solid cyan; background-color: green; color: white")
        self.grid_layout.addWidget(label, x, y)

    def handle_key_press(self, event):
        global player_position
        x, y = player_position

        # Update coordinates based on direction
        if event.key() == Qt.Key.Key_Up:
            x = max(0, x - 1)
        elif event.key() == Qt.Key.Key_Down:
            x = min(self.rows - 1, x + 1)
        elif event.key() == Qt.Key.Key_Left:
            y = max(0, y - 1)
        elif event.key() == Qt.Key.Key_Right:
            y = min(self.columns - 1, y + 1)

        player_position = (x, y)
        self.update()
        
        if player_position == self.finish_line_position:
            self.finish_game()

    def check_enemy_interactions(self):
        global player_health, player_position

        if player_position in self.enemy_positions:
            damage = random.randint(10, 50)
            player_health -= damage
            if player_health <= 0:
                self.game_over()
            else:
                print(f"Salud:{player_health}")
                print(f"Daño:{damage}")

    def game_over(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Game Over")
        msg_box.setText("Perdiste PIPIPIPI. Game Over.")
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.exec()
        sys.exit()
        
    def finish_game(self):
        self.end_time = time.time()
        elapsed_time = self.start_time-self.end_time
        msg_box = QMessageBox()
        msg_box.resize(400,400)
        msg_box.setWindowTitle("ExtrahuevoOrdinario")
        msg_box.setText(f"Tiempo logrado{elapsed_time}")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.exec()
        sys.exit()

    def paintEvent(self, event):
        painter = QPainter(self)

        #*************Dibujar Jugador**************
        painter.setBrush(QColor('cyan'))
        painter.drawRect(player_position[1] * 50, player_position[0] * 50, 50, 50)

        #******** Enemigos***********
        for enemy_pos in self.enemy_positions:
            painter.setBrush(QColor('red'))
            painter.drawRect(enemy_pos[1] * 50, enemy_pos[0] * 50, 50, 50)
        
        
        #********* Barra Salud ***********
        painter.setPen(QColor("green"))
        painter.drawText(20,40,"Barra de salud:")
        painter.setBrush(QColor('green'))
        painter.drawRect(125, 20, player_health, 20)
        
        #******** Finish line ********
        painter.drawRect(self.finish_line_position[1] * 50, self.finish_line_position[0] * 50, 50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_widget = GameWidget()
    start_screen = StartScreen(game_widget=game_widget)
    start_screen.showFullScreen()
    sys.exit(app.exec())
