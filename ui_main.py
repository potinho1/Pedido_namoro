# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainxHjsaK.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 438)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.00995025 rgba(224, 27, 36, 255), stop:0.98 rgba(237, 51, 59, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QLabel#pergunta{\n"
"	font-size : 35px;\n"
"	font-weight : bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	font-size: 20px;\n"
"	color: red;\n"
"	min-height: 45px;\n"
"	border-radius: 20px;\n"
"	background-color: white;\n"
"	\n"
"}")
        self.pergunta = QLabel(self.centralwidget)
        self.pergunta.setObjectName(u"pergunta")
        self.pergunta.setGeometry(QRect(10, 0, 431, 91))
        self.pergunta.setAlignment(Qt.AlignCenter)
        self.frame_yes = QFrame(self.centralwidget)
        self.frame_yes.setObjectName(u"frame_yes")
        self.frame_yes.setGeometry(QRect(30, 230, 131, 111))
        self.frame_yes.setFrameShape(QFrame.NoFrame)
        self.frame_yes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_yes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_yes = QPushButton(self.frame_yes)
        self.button_yes.setObjectName(u"button_yes")

        self.horizontalLayout.addWidget(self.button_yes)

        self.frame_no = QFrame(self.centralwidget)
        self.frame_no.setObjectName(u"frame_no")
        self.frame_no.setGeometry(QRect(290, 230, 121, 111))
        self.frame_no.setFrameShape(QFrame.NoFrame)
        self.frame_no.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_no)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_no = QPushButton(self.frame_no)
        self.button_no.setObjectName(u"button_no")

        self.horizontalLayout_2.addWidget(self.button_no)

        self.coracao = QLabel(self.centralwidget)
        self.coracao.setObjectName(u"coracao")
        self.coracao.setGeometry(QRect(130, 90, 191, 141))
        self.coracao.setPixmap(QPixmap(u":/imagens/coracao.png"))
        self.coracao.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pergunta.setText(QCoreApplication.translate("MainWindow", u"Quer namorar comigo?", None))
        self.button_yes.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.button_no.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.coracao.setText("")
    # retranslateUi

