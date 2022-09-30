import random

from PySide6 import QtWidgets
from PySide6.QtCore import QEvent

from ui_main import Ui_MainWindow


class MainWindonw(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindonw, self).__init__()
        self.setupUi(self)

        self.coracao.setVisible(False)

        self.button_yes.clicked.connect(self.moveButton)
        self.button_no.clicked.connect(self.yes_choice)
        self.frame_yes.installEventFilter(self)

    def moveButton(self):
        self.frame_yes.move(random.randint(0, 300), random.randint(0, 300))

    def yes_choice(self):
        self.pergunta.setText("Melhor opção")
        self.coracao.setVisible(True)
        self.button_yes.setVisible(False)
        self.button_no.setVisible(False)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter and obj == self.frame_yes:
            self.moveButton()
            return True
        else:
            return False

app = QtWidgets.QApplication([])

window = MainWindonw()
window.show()

app.exec()
