import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.l = QGridLayout()
        self.lab1 = QLabel("Weight")
        self.lab2 = QLabel("Height")
        self.lab1_m = QLabel("kg")
        self.lab2_m = QLabel("cm")
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.button = QPushButton("Calculate")
        self.result = QLabel("Result:")

        self.underweight = QLabel("""Underweight
< 18.5""")
        self.normalweight = QLabel("""Normal weight
18.5 - 25""")
        self.overweight = QLabel("""Overweight
25 - 30""")
        self.obese = QLabel("""Obese
> 30""")


        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear)
        file_menu.addAction(clear_action)
        help_menu = menu_bar.addMenu("Help")
        help_action = QAction("Get Help", self)
        help_action.triggered.connect(self.help)
        help_menu.addAction(help_action)
        self.button.clicked.connect(self.calculate)

        self.l.addWidget(self.lab1, 0, 0)
        self.l.addWidget(self.lab2, 1, 0)
        self.l.addWidget(self.input1, 0, 1)
        self.l.addWidget(self.input2, 1, 1)
        self.l.addWidget(self.lab1_m, 0, 2)
        self.l.addWidget(self.lab2_m, 1, 2)
        self.l.addWidget(self.button, 2, 0)
        self.l.addWidget(self.result, 3, 0)
        self.l.addWidget(self.underweight, 4, 0)
        self.l.addWidget(self.normalweight, 4, 1)
        self.l.addWidget(self.overweight, 4, 2)
        self.l.addWidget(self.obese, 4, 3)
        self.l.setMenuBar(menu_bar)
        self.setLayout(self.l)

    def calculate(self):
        try:
            self.variable = None
            a = float(self.input1.text())
            b = float(self.input2.text())
            c = a / (b/100)**2
            if c < 18.5:
                self.variable = "Underweight"
            elif c >= 18.5 and c <= 25:
                self.variable = "Normal Weight" 
            elif c > 25 and c <= 30:
                self.variable = "Overweight"
            elif c > 30:
                self.variable = "Obese"
            else:
                self.variable = "???"

            self.result.setText(f"Result: {round(c, 1)} \n{self.variable}")
        except:
            self.result.setText("Ошибка ввода")

    def clear(self):
        self.result.setText("Result:")
    def help(self):
        self.help_window = HelpWindow()
        self.help_window.show()

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("about BMI Calculator")
        self.l = QGridLayout()
        self.label = QLabel("Это приложение о подсчёте BMI")
        self.l.addWidget(self.label, 0, 0)
        self.setLayout(self.l)
    
app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())