# -*- coding: utf-8 -*-
"""
__author__ = "Rizwan Hasan"
__email__ = "rizwan.hasan486@gmail.com"
__github__ = "https://github.com/Rizwan-Hasan"

"""

import sys
import math
import time
import random
import typing
from PySide6.QtCore import Qt, QThread, Slot
from PySide6.QtGui import (
    QCloseEvent,
    QGuiApplication,
    QPixmap,
    QValidator,
    QIntValidator,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMessageBox,
    QStyleFactory,
    QWidget,
    QGraphicsOpacityEffect,
    QLCDNumber,
)

from ui.MainWindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__randomNumberGeneratorThread: QThread

        # Setting fixed window size to disable full screen ↓
        # self.setFixedWidth(self.minimumSizeHint().width())
        # self.setFixedHeight(self.minimumSizeHint().height())

        # ↓
        self.__main()

    def __main(self):
        # Making window centered ↓
        self.__makeWindowCenter()

        # Window customizing ↓
        self.setWindowTitle("Random Number Generator")

        # QLineEdit Only Accept Integer
        self.ui.lineEditFrom.setValidator(QIntValidator())
        self.ui.lineEditTo.setValidator(QIntValidator())

        # Default Button's Behaviour Set ↓
        self.ui.btnQuit.clicked.connect(lambda _: self.close())
        self.ui.btnGenerate.clicked.connect(lambda _: self.__buttonGenerate_Func())

    # For launching windows in center ↓
    def __makeWindowCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    # Close button behaviour ↓
    @Slot(QCloseEvent)
    def closeEvent(self, event: QCloseEvent):
        buttonReply = QMessageBox.question(
            self,
            "Confirmation",
            "Are you sure to quit?",
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Cancel,
        )
        if buttonReply == QMessageBox.Ok:
            event.accept()
        else:
            event.ignore()

    def __buttonGenerate_Func(self):
        n_from = self.ui.lineEditFrom.text()
        n_to = self.ui.lineEditTo.text()

        if n_from and n_to:
            n_from = int(n_from)
            n_to = int(n_to)

        else:
            QMessageBox.information(self, "Info", "Fill all the blanks")
            return

        effect = QGraphicsOpacityEffect(self.ui.lcdNumber)
        self.ui.lcdNumber.setGraphicsEffect(effect)

        self.__randomNumberGeneratorThread = RandomNumberGenerator_Thread()
        self.__randomNumberGeneratorThread.setObjects(
            n_from=n_from, n_to=n_to, lcd=self.ui.lcdNumber, effect=effect
        )
        self.__randomNumberGeneratorThread.start()


class RandomNumberGenerator_Thread(QThread):
    __n_from: int
    __n_to: int
    __lcd: QLCDNumber
    __numOfDigit: int
    __effect: QGraphicsOpacityEffect

    def setObjects(
        self, n_from: int, n_to: int, lcd: QLCDNumber, effect: QGraphicsOpacityEffect
    ) -> typing.NoReturn:
        self.__n_from = n_from
        self.__n_to = n_to
        self.__lcd = lcd
        self.__effect = effect
        self.__numOfDigit = math.floor(math.log10(max(n_from, n_to))) + 1

    def run(self):
        self.__lcd.setDigitCount(self.__numOfDigit)
        tmp: list = sorted([self.__n_from, self.__n_to + 1])
        n_of_sample: int = tmp[1] - tmp[0]
        n_list: list = random.sample(
            range(tmp[0], tmp[1]), n_of_sample if n_of_sample < 500 else 500
        )

        n: int = 25
        opacityVal: int = 1
        for _ in range(n):
            self.__lcd.display(random.choice(n_list))
            self.__effect.setOpacity(opacityVal)
            tmp_val = 1 / n
            opacityVal -= tmp_val
            time.sleep(tmp_val)

        self.__effect.setOpacity(1)
        self.quit()


def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
