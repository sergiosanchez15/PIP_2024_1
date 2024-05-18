import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
import random

class HangmanGame(QWidget):
    def __init__(self):
        super().__init__()

        self.wordlist = ['hangman', 'python', 'programming', 'computer', 'game', 'developer', 'learning', 'coding']
        self.palabra_secreta = random.choice(self.wordlist)
        self.adivinar_palabra = ['_' for _ in self.palabra_secreta]
        self.attempts = 6

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hangman Game')

        self.word_label = QLabel(' '.join(self.adivinar_palabra))
        self.word_label.setStyleSheet('''
            color: #FF5733;
            font-size: 100px;
            font-weight: bold;
            border: 1px solid #AC2641;
            padding: 1px;
            border-radius: 5px;''')
        self.attempts_label = QLabel('Intentos restantes: {self.attempts}')
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText('Introduzca letras...')
        self.input_box.setStyleSheet('''
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 5px;'''
        )
        self.input_button = QPushButton('Adivina')
        self.input_button.setStyleSheet('''background-color: #4CAF50;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;''')
        self.input_button.clicked.connect(self.checkGuess)

        vbox = QVBoxLayout()
        vbox.addWidget(self.word_label)
        vbox.addWidget(self.attempts_label)
        vbox.addWidget(self.input_box)
        vbox.addWidget(self.input_button)

        self.setLayout(vbox)

    def checkGuess(self):
        guess = self.input_box.text().strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            QMessageBox.warning(self, 'No es valido', 'Use una sola letra.')
            return

        if guess in self.palabra_secreta:
            for i, letter in enumerate(self.palabra_secreta):
                if letter == guess:
                    self.adivinar_palabra[i] = guess
            self.word_label.setText(' '.join(self.adivinar_palabra))
        else:
            self.attempts -= 1
            self.attempts_label.setText(f'Intentos restantes: {self.attempts}')

        self.input_box.clear()

        if '_' not in self.adivinar_palabra:
            QMessageBox.information(self, 'Felicidades!', 'Eres extrahuevordinario!')
            self.resetGame()

        if self.attempts == 0:
            QMessageBox.information(self, 'Decepcion', f'La palabra era "{self.palabra_secreta}". Pedazo de brocoli!')
            self.resetGame()

    def resetGame(self):
        self.palabra_secreta = random.choice(self.wordlist)
        self.adivinar_palabra = ['_' for _ in self.palabra_secreta]
        self.attempts = 6
        self.word_label.setText(' '.join(self.adivinar_palabra))
        self.attempts_label.setText(f'Intentos restantes: {self.attempts}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec())
