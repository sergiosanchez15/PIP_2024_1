import sys
from PyQt5 import uic, QtWidgets
import random

qtCreatorFile = "Juego_Memorama.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.cards = [
            self.btn1, self.btn2, self.btn3, self.btn4,
            self.btn5, self.btn6, self.btn7, self.btn8
        ]
        self.btn_reset.clicked.connect(self.reset_game)
        self.setup_game()

    # Área de los Slots
    def setup_game(self):
        self.images = [":/twice/angelito.jpg", ":/twice/paniawa.jpg", ":/twice/sheko.jpg", ":/twice/yo.jpg"] * 2
        random.shuffle(self.images)  # Corregido aquí
        self.flipped = [False] * len(self.images)
        self.first_card_index = None
        for i, card in enumerate(self.cards):
            card.clicked.connect(lambda _, i=i: self.flip_card(i))
            card.setEnabled(True)

    def flip_card(self, index):
        if not self.flipped[index]:
            self.flipped[index] = True
            self.cards[index].setStyleSheet(f"background-image: url({self.images[index]});")
            if self.first_card_index is None:
                self.first_card_index = index
            else:
                if self.images[self.first_card_index] == self.images[index]:
                    self.cards[self.first_card_index].setEnabled(False)
                    self.cards[index].setEnabled(False)
                else:
                    self.cards[self.first_card_index].setStyleSheet("")
                    self.cards[index].setStyleSheet("")
                self.first_card_index = None

    def reset_game(self):
        self.first_card_index = None
        self.flipped = [False] * len(self.images)
        self.setup_game()

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())