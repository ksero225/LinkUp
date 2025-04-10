# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionSign_in = QAction(MainWindow)
        self.actionSign_in.setObjectName(u"actionSign_in")
        self.actionSign_up = QAction(MainWindow)
        self.actionSign_up.setObjectName(u"actionSign_up")
        self.actionLog_out = QAction(MainWindow)
        self.actionLog_out.setObjectName(u"actionLog_out")
        self.actionAbout_me = QAction(MainWindow)
        self.actionAbout_me.setObjectName(u"actionAbout_me")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        self.actionAbout_me.setIcon(icon)
        self.actionAdd_new_contact = QAction(MainWindow)
        self.actionAdd_new_contact.setObjectName(u"actionAdd_new_contact")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.actionAdd_new_contact.setIcon(icon1)
        self.actionDelete_contact = QAction(MainWindow)
        self.actionDelete_contact.setObjectName(u"actionDelete_contact")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.actionDelete_contact.setIcon(icon2)
        self.actionDoc = QAction(MainWindow)
        self.actionDoc.setObjectName(u"actionDoc")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpFaq))
        self.actionDoc.setIcon(icon3)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionAbout.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(255)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuKonto = QMenu(self.menubar)
        self.menuKonto.setObjectName(u"menuKonto")
        self.menuManage_contacts = QMenu(self.menubar)
        self.menuManage_contacts.setObjectName(u"menuManage_contacts")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuKonto.menuAction())
        self.menubar.addAction(self.menuManage_contacts.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuKonto.addAction(self.actionSign_in)
        self.menuKonto.addAction(self.actionSign_up)
        self.menuKonto.addAction(self.actionLog_out)
        self.menuKonto.addAction(self.actionAbout_me)
        self.menuManage_contacts.addAction(self.actionAdd_new_contact)
        self.menuManage_contacts.addAction(self.actionDelete_contact)
        self.menuHelp.addAction(self.actionDoc)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LinkUp", None))
        self.actionSign_in.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.actionSign_up.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.actionLog_out.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.actionAbout_me.setText(QCoreApplication.translate("MainWindow", u"About me", None))
        self.actionAdd_new_contact.setText(QCoreApplication.translate("MainWindow", u"Add contact", None))
        self.actionDelete_contact.setText(QCoreApplication.translate("MainWindow", u"Delete contact", None))
        self.actionDoc.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
#if QT_CONFIG(shortcut)
        self.actionDoc.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Status: Offline", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.menuKonto.setTitle(QCoreApplication.translate("MainWindow", u"Account", None))
        self.menuManage_contacts.setTitle(QCoreApplication.translate("MainWindow", u"Manage contacts", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

