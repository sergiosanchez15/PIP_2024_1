import sys
from PyQt5 import uic, QtWidgets
import random
qtCreatorFile = "Juego_GatoyRaton.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.buttons = [
            [self.btn1, self.btn2, self.btn3],
            [self.btn4, self.btn5, self.btn6],
            [self.btn7, self.btn8, self.btn9]
        ]

        for i in range(3):
            for j in range(3):
                button = self.buttons[i][j]
                button.clicked.connect(self.on_button_clicked)

        self.reset_game()

    # Área de los Slots
    def reset_game(self):
        self.current_player = 'X'
        self.game_board = [['' for _ in range(3)] for _ in range(3)]
        self.update_display()

    def update_display(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText(self.game_board[i][j])


    def check_winner(self):
        for i in range(3):
            if (self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] != '' or
                    self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] != ''):
                return True


            # Verificar diagonales
        if (self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != '' or
                self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] != ''):
            return True
        return False
        pass

    def on_button_clicked(self):
        button = self.sender()
        row = int(button.objectName()[-1]) - 1
        col = int(button.objectName()[-2]) - 1

        if self.game_board[row][col] == '':
            self.game_board[row][col] = self.current_player
            self.update_display()

            # Verificar si hay un ganador
            if self.check_winner():
                self.statusBar().showMessage(f'¡{self.current_player} ganaste padrino!')
                return

            # Cambiar al siguiente jugador
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.statusBar().showMessage(f'Turno del jugador {self.current_player}')
    #try:
     #   except Exception as error:
    #print(error):


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())