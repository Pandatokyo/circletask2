import random
import sys
from PyQt5 import uic
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from ui_file import Ui_Dialog


class CircleApp(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pushButton.clicked.connect(self.paint_circle)
        self.setWindowTitle('Circle')
        self._image = QPixmap('background.png')
        self.should_paint_circle = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            colors = [Qt.white, Qt.black, Qt.red, Qt.darkRed,
                      Qt.green, Qt.darkGreen, Qt.blue, Qt.darkBlue,
                      Qt.cyan, Qt.darkCyan, Qt.magenta, Qt.darkMagenta,
                      Qt.yellow, Qt.darkYellow, Qt.gray, Qt.darkGray, Qt.lightGray]
            painter.setPen(QPen(random.choice(colors), 5, Qt.SolidLine))
            radius = random.randint(50, 200)
            a, b = random.randint(0, 500), random.randint(0, 500)
            painter.drawEllipse(a, b, radius, radius)

    def paint_circle(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleApp()
    ex.show()
    sys.exit(app.exec())
