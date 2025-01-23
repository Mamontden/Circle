import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt6.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt6.QtCore import Qt, QRect
from PyQt6 import uic
from random import randint


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.spisok_krugov = []
        self.pushButton.clicked.connect(self.run)

    def run(self):
        diameter = randint(5, 150)
        x = randint(0, self.width() - diameter)
        y = randint(0, self.height() - diameter)
        self.spisok_krugov.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        for (x, y, diameter) in self.spisok_krugov:
            painter.drawEllipse(QRect(x, y, diameter, diameter))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())