import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.vbox = QVBoxLayout()
        #self.resize(250, 308)

        self.label = QLabel(self)
        self.button = QPushButton("Push me!", self)
        self.line = QLineEdit(self)


        self.vbox.addWidget(self.line)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)

        self.label.setText("")

        self.setLayout(self.vbox)

        self.button.clicked.connect(self.action)

    def action(self):
        answer = self.line.text()
        self.label.setText("Привет!")


app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())
