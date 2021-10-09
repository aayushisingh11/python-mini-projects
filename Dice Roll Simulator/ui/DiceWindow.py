# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DiceWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import resources_rc

class Ui_DiceWindow(object):
    def setupUi(self, DiceWindow):
        if not DiceWindow.objectName():
            DiceWindow.setObjectName(u"DiceWindow")
        DiceWindow.resize(476, 433)
        icon = QIcon()
        icon.addFile(u":/icons/app-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        DiceWindow.setWindowIcon(icon)
        DiceWindow.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.gridLayout = QGridLayout(DiceWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 49, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnQuit = QPushButton(DiceWindow)
        self.btnQuit.setObjectName(u"btnQuit")
        icon1 = QIcon()
        icon1.addFile(u":/icons/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnQuit.setIcon(icon1)
        self.btnQuit.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnQuit)

        self.btnRoll = QPushButton(DiceWindow)
        self.btnRoll.setObjectName(u"btnRoll")
        icon2 = QIcon()
        icon2.addFile(u":/icons/dice.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRoll.setIcon(icon2)
        self.btnRoll.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnRoll)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 49, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(89, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.labelDice = QLabel(DiceWindow)
        self.labelDice.setObjectName(u"labelDice")
        self.labelDice.setPixmap(QPixmap(u":/dice/six.png"))
        self.labelDice.setScaledContents(True)
        self.labelDice.setMargin(10)

        self.gridLayout.addWidget(self.labelDice, 1, 1, 1, 1)


        self.retranslateUi(DiceWindow)

        QMetaObject.connectSlotsByName(DiceWindow)
    # setupUi

    def retranslateUi(self, DiceWindow):
        DiceWindow.setWindowTitle(QCoreApplication.translate("DiceWindow", u"Form", None))
        self.btnQuit.setText(QCoreApplication.translate("DiceWindow", u"Quit", None))
        self.btnRoll.setText(QCoreApplication.translate("DiceWindow", u"Roll", None))
        self.labelDice.setText("")
    # retranslateUi

