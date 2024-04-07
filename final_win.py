# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Rezyltatokna(QWidget):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.initUI()
    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.name_text = QLabel("ФИO")
        self.index_lable = QLabel('Индекс руфье')
        self.Rezyltatlable = QLabel('работоспособность')

        self.main_layout.addWidget(self.name_text, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.index_lable, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.Rezyltatlable, alignment=Qt.AlignCenter)
        self.setLayout(self.main_layout)