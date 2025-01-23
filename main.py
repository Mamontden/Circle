import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRect
from PyQt6 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(0, self.height() - d)
        paint = QPainter(self)
        paint.setBrush(QColor(255, 255, 0))
        paint.drawEllipse(QRect(x, y, d, d))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
