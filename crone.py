import sys

from random import randint, sample
from PyQt5.QtGui import QPainter, QColor
from crg import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Grugg.clicked.connect(self.draw)
        self.col = [i for i in range(256)]

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        r, g, b = sample(self.col, 3)
        rad = randint(1, 100)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(150 - rad // 2, 150 - rad // 2, rad, rad)
        qp.end()

    def draw(self):
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())