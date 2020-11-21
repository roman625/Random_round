import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import random, randrange
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 260, 171, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Нажми"))

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.fl = False

    def run(self):
        self.fl = True
        self.update()

    def paintEvent(self, event):
        if self.fl:
            d, x, y = round(random() * self.width()), round(random() * self.width() / 2), round(
                random() * self.width() / 2)
            l = [x, y, d, d]
            color = QColor(randrange(256), randrange(256), randrange(256))
            qp = QPainter()
            qp.begin(self)

            qp.setBrush(color)
            qp.drawEllipse(*l)

            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())


