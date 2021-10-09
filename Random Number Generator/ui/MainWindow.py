# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 433)
        icon = QIcon()
        icon.addFile(u":/icons/app-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lcdNumber = QLCDNumber(MainWindow)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.000000000000000)

        self.verticalLayout.addWidget(self.lcdNumber)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnQuit = QPushButton(MainWindow)
        self.btnQuit.setObjectName(u"btnQuit")
        icon1 = QIcon()
        icon1.addFile(u":/icons/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnQuit.setIcon(icon1)
        self.btnQuit.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnQuit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEditFrom = QLineEdit(MainWindow)
        self.lineEditFrom.setObjectName(u"lineEditFrom")
        self.lineEditFrom.setMaxLength(99)

        self.horizontalLayout.addWidget(self.lineEditFrom)

        self.lineEditTo = QLineEdit(MainWindow)
        self.lineEditTo.setObjectName(u"lineEditTo")
        self.lineEditTo.setMaxLength(99)

        self.horizontalLayout.addWidget(self.lineEditTo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btnGenerate = QPushButton(MainWindow)
        self.btnGenerate.setObjectName(u"btnGenerate")
        icon2 = QIcon()
        icon2.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGenerate.setIcon(icon2)
        self.btnGenerate.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnGenerate)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.lineEditFrom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"From", None))
        self.lineEditTo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"To", None))
        self.btnGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

