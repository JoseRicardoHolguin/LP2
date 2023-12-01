import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts')
        self.setLayout(self.get_layout())
        self.show()

    def get_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.get_layout1())
        layout.addLayout(self.get_layout2())
        layout.addLayout(self.get_layout3())
        return layout

    def get_layout1(self):
        layout1 = QVBoxLayout()
        for i in range(4):
            layout1.addWidget(QPushButton(f"{i+1}"))
        return layout1

    def get_layout2(self):
        layout1 = QHBoxLayout()
        layout1.addWidget(QPushButton("5"))
        layout1.addWidget(QPushButton("6"))
        layout1.addWidget(QPushButton("7"))
        return layout1

    def get_layout3(self):
        layout1 = QVBoxLayout()
        layout1.addWidget(QPushButton("8"))
        layout1.addWidget(QPushButton("9"))
        layout1.addWidget(QPushButton("10"))
        return layout1
    


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
