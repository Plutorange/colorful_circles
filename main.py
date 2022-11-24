import random
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pushButton.clicked.connect(self.paint)

    def initUI(self):
        self.setGeometry(300, 200, 650, 650)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 150, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('Press me')

    def paint(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        n1, n2 = random.randrange(650), random.randrange(650)
        s = random.randrange(1, 650)
        c = [random.randrange(255), random.randrange(255), random.randrange(255)]
        qp.setBrush(QColor(*c))
        qp.drawEllipse(n1, n2, s, s)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
