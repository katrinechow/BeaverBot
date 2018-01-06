import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class BeaverGUI(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Beaver Bot'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('beaver.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BeaverGUI()
    sys.exit(app.exec_())