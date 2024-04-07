# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class secondwindow(QWidget):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.initUI()
    def initUI(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        name = QLabel('Введите имя')
        inputnamen = QLineEdit()
        inputnamen.setPlaceholderText('Имя Фамилия')
        Yearsold = QLabel('Введите свой возраст')
        inputold = QLineEdit()
        inputold.setPlaceholderText('67')
        labelinstrykt1 = QLabel('Инструкция')
        firsttest = QPushButton('Начать первый тест')
        inputest1 = QLineEdit()
        inputest1.setPlaceholderText('0')
        labelinstrykt2 = QLabel('Инструкция2')
        secondtest = QPushButton('Начать второй тест')
        inputest2 = QLineEdit()
        inputest2.setPlaceholderText('0')
        labelinstrykt3 = QLabel('Инструкция3')
        tritest = QPushButton('Начать третий тест')
        inputest3 = QLineEdit()
        inputest3.setPlaceholderText('0')
        buttonfinal = QPushButton('Отправить результаты')
        timer = QLabel('oo:oo')

        left_layout.addWidget(name, alignment=Qt.AlignLeft)
        left_layout.addWidget(inputnamen, alignment=Qt.AlignLeft)
        left_layout.addWidget(Yearsold, alignment=Qt.AlignLeft)
        left_layout.addWidget(inputold, alignment=Qt.AlignLeft)
        left_layout.addWidget(labelinstrykt1, alignment=Qt.AlignLeft)
        left_layout.addWidget(firsttest, alignment=Qt.AlignLeft)
        left_layout.addWidget(labelinstrykt2, alignment=Qt.AlignLeft)
        left_layout.addWidget(secondtest, alignment=Qt.AlignLeft)
        left_layout.addWidget(inputest2, alignment=Qt.AlignLeft)
        left_layout.addWidget(labelinstrykt3, alignment=Qt.AlignLeft)
        left_layout.addWidget(tritest, alignment=Qt.AlignLeft)
        left_layout.addWidget(inputest3, alignment=Qt.AlignLeft)
        left_layout.addWidget(buttonfinal, alignment=Qt.AlignLeft)
        right_layout.addWidget(timer, alignment=Qt.AlignRight)
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)
        self.setLayout(left_layout)
        self.setLayout(right_layout)


app = QApplication([])
okno = secondwindow()
okno.setFont(QFont('calibri', 17))
okno.show()
app.exec_()