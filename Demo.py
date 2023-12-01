
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class Demo(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.label = QLabel("Enter your name:")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Submit")

        # Create layouts
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        # Add widgets to layouts
        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.line_edit)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.button)

        # Set main layout
        self.setLayout(self.v_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
