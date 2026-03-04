import sys
from PyQt6.QtWidgets import *

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.l = QGridLayout()
        self.expression = ''
        self.stroke = QLineEdit('')
        self.button_rem = QPushButton('⌫')
        self.button_c = QPushButton('C')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')
        self.button_division = QPushButton("÷")
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_multiply = QPushButton("×")
        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_minus = QPushButton("-")
        self.button_0 = QPushButton('0')
        self.button_dote = QPushButton('.')
        self.button_plus = QPushButton('+')
        self.button_equal = QPushButton("=")

        self.button_0.clicked.connect(lambda: self.add_to_expression("0"))
        self.button_1.clicked.connect(lambda: self.add_to_expression("1"))
        self.button_2.clicked.connect(lambda: self.add_to_expression("2"))
        self.button_3.clicked.connect(lambda: self.add_to_expression("3"))
        self.button_4.clicked.connect(lambda: self.add_to_expression("4"))
        self.button_5.clicked.connect(lambda: self.add_to_expression("5"))
        self.button_6.clicked.connect(lambda: self.add_to_expression("6"))
        self.button_7.clicked.connect(lambda: self.add_to_expression("7"))
        self.button_8.clicked.connect(lambda: self.add_to_expression("8"))
        self.button_9.clicked.connect(lambda: self.add_to_expression("9"))
        self.button_division.clicked.connect(lambda: self.add_to_expression("/"))
        self.button_multiply.clicked.connect(lambda: self.add_to_expression("*"))
        self.button_plus.clicked.connect(lambda: self.add_to_expression("+"))
        self.button_minus.clicked.connect(lambda: self.add_to_expression("-"))
        self.button_dote.clicked.connect(lambda: self.add_to_expression("."))
        
        self.button_equal.clicked.connect(self.calculate)

        self.button_rem.clicked.connect(self.remove_last_character)

        self.button_c.clicked.connect(self.clear_expression)

        self.l.addWidget(self.stroke, 0, 1, 1, 2)
        self.l.addWidget(self.button_7, 1, 1)
        self.l.addWidget(self.button_8, 1, 2)
        self.l.addWidget(self.button_9, 1, 3)
        self.l.addWidget(self.button_division, 1, 4)
        self.l.addWidget(self.button_rem, 0, 3)
        self.l.addWidget(self.button_c, 0, 4)
        
        self.l.addWidget(self.button_4, 2, 1)
        self.l.addWidget(self.button_5, 2, 2)
        self.l.addWidget(self.button_6, 2, 3)
        self.l.addWidget(self.button_multiply, 2, 4)

        self.l.addWidget(self.button_1, 3, 1)
        self.l.addWidget(self.button_2, 3, 2)
        self.l.addWidget(self.button_3, 3, 3)
        self.l.addWidget(self.button_minus, 3, 4)

        self.l.addWidget(self.button_0, 4, 1)
        self.l.addWidget(self.button_dote, 4, 2)
        self.l.addWidget(self.button_plus, 4, 3)
        self.l.addWidget(self.button_equal, 4, 4)

        self.setLayout(self.l)

    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
            self.stroke.setText(self.expression)
        except ZeroDivisionError:
            self.stroke.setText("Ошибка при делении на ноль")
            self.expression = ''
        except:
            self.stroke.setText("Ошибка ввода значений")
            self.expression = ''
    
    def add_to_expression(self, value):
        self.expression += value
        self.stroke.setText(self.expression)

    def remove_last_character(self):
        self.expression = self.expression[:len(self.expression)-1]
        self.stroke.setText(self.expression)

    def clear_expression(self):
        self.expression = ''
        self.stroke.setText('')

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())