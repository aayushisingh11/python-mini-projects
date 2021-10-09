# -*- coding: utf-8 -*-
"""
__author__ = "Rizwan Hasan"
__email__ = "rizwan.hasan486@gmail.com"
__github__ = "https://github.com/Rizwan-Hasan"

"""

import sys
import time
import random
import typing
from PySide6.QtCore import Qt, QThread, Slot
from PySide6.QtGui import QCloseEvent, QGuiApplication, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMessageBox,
    QStyleFactory,
    QWidget,
    QGraphicsOpacityEffect,
)

from ui.DiceWindow import Ui_DiceWindow


class DiceWindow(QWidget):
    def __init__(self):
        super(DiceWindow, self).__init__()
        self.ui = Ui_DiceWindow()
        self.ui.setupUi(self)
        self.__diceRollerThread: QThread

        # Setting fixed window size to disable full screen ↓
        self.setFixedWidth(self.minimumSizeHint().width())
        self.setFixedHeight(self.minimumSizeHint().height())

        # ↓
        self.__main()

    def __main(self):
        # Making window centered ↓
        self.__makeWindowCenter()

        # Window customizing ↓
        self.setWindowTitle("Dice Simulator")

        # Default Button's Behaviour Set ↓
        self.ui.btnQuit.clicked.connect(lambda _: self.close())
        self.ui.btnRoll.clicked.connect(lambda _: self.__buttonRoll_Func())

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

    def __buttonRoll_Func(self):
        effect = QGraphicsOpacityEffect(self.ui.labelDice)
        self.ui.labelDice.setGraphicsEffect(effect)

        self.__diceRollerThread = DiceRoller_Thread()
        self.__diceRollerThread.setObjects(labelDice=self.ui.labelDice, effect=effect)

        self.__diceRollerThread.start()


class DiceRoller_Thread(QThread):

    __labelDice: QLabel
    __effect: QGraphicsOpacityEffect

    def run(self):
        dice_images: tuple = (
            ":/dice/one.png",
            ":/dice/two.png",
            ":/dice/three.png",
            ":/dice/four.png",
            ":/dice/five.png",
            ":/dice/six.png",
        )

        opacityVal: int = 1
        n: int = 25
        for _ in range(n):
            dice_pixmap = QPixmap(random.choice(dice_images))
            self.__labelDice.setPixmap(dice_pixmap)
            self.__effect.setOpacity(opacityVal)
            self.__labelDice.show()
            time.sleep(1 / n)
            opacityVal -= 1 / n

        self.__effect.setOpacity(1)

        self.quit()

    def setObjects(
        self, labelDice: QLabel, effect: QGraphicsOpacityEffect
    ) -> typing.NoReturn:
        self.__labelDice = labelDice
        self.__effect = effect


def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = DiceWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
