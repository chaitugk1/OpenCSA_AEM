# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionElement_Block = QAction(MainWindow)
        self.actionElement_Block.setObjectName(u"actionElement_Block")
        self.actionMaterial = QAction(MainWindow)
        self.actionMaterial.setObjectName(u"actionMaterial")
        self.actionSteel = QAction(MainWindow)
        self.actionSteel.setObjectName(u"actionSteel")
        self.actionBoundary_Condition = QAction(MainWindow)
        self.actionBoundary_Condition.setObjectName(u"actionBoundary_Condition")
        self.actionLoading = QAction(MainWindow)
        self.actionLoading.setObjectName(u"actionLoading")
        self.actionContact_Us = QAction(MainWindow)
        self.actionContact_Us.setObjectName(u"actionContact_Us")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(11, 10, 121, 381))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Vertical)
        self.pushButton_block = QPushButton(self.splitter)
        self.pushButton_block.setObjectName(u"pushButton_block")
        sizePolicy.setHeightForWidth(self.pushButton_block.sizePolicy().hasHeightForWidth())
        self.pushButton_block.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.pushButton_block)
        self.pushButton_steel = QPushButton(self.splitter)
        self.pushButton_steel.setObjectName(u"pushButton_steel")
        sizePolicy.setHeightForWidth(self.pushButton_steel.sizePolicy().hasHeightForWidth())
        self.pushButton_steel.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.pushButton_steel)
        self.pushButton_bc = QPushButton(self.splitter)
        self.pushButton_bc.setObjectName(u"pushButton_bc")
        sizePolicy.setHeightForWidth(self.pushButton_bc.sizePolicy().hasHeightForWidth())
        self.pushButton_bc.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.pushButton_bc)
        self.pushButton_load = QPushButton(self.splitter)
        self.pushButton_load.setObjectName(u"pushButton_load")
        sizePolicy.setHeightForWidth(self.pushButton_load.sizePolicy().hasHeightForWidth())
        self.pushButton_load.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.pushButton_load)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label)
        self.checkBox_eleno = QCheckBox(self.splitter)
        self.checkBox_eleno.setObjectName(u"checkBox_eleno")
        sizePolicy.setHeightForWidth(self.checkBox_eleno.sizePolicy().hasHeightForWidth())
        self.checkBox_eleno.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.checkBox_eleno)
        self.checkBox_steel = QCheckBox(self.splitter)
        self.checkBox_steel.setObjectName(u"checkBox_steel")
        sizePolicy.setHeightForWidth(self.checkBox_steel.sizePolicy().hasHeightForWidth())
        self.checkBox_steel.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.checkBox_steel)
        self.checkBox_bc = QCheckBox(self.splitter)
        self.checkBox_bc.setObjectName(u"checkBox_bc")
        sizePolicy.setHeightForWidth(self.checkBox_bc.sizePolicy().hasHeightForWidth())
        self.checkBox_bc.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.checkBox_bc)
        self.checkBox_load = QCheckBox(self.splitter)
        self.checkBox_load.setObjectName(u"checkBox_load")
        sizePolicy.setHeightForWidth(self.checkBox_load.sizePolicy().hasHeightForWidth())
        self.checkBox_load.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.checkBox_load)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(140, 10, 551, 641))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuManage = QMenu(self.menubar)
        self.menuManage.setObjectName(u"menuManage")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuManage.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExit)
        self.menuManage.addAction(self.actionElement_Block)
        self.menuManage.addAction(self.actionMaterial)
        self.menuManage.addAction(self.actionSteel)
        self.menuManage.addAction(self.actionBoundary_Condition)
        self.menuManage.addAction(self.actionLoading)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionContact_Us)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionElement_Block.setText(QCoreApplication.translate("MainWindow", u"Element Block", None))
        self.actionMaterial.setText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.actionSteel.setText(QCoreApplication.translate("MainWindow", u"Steel", None))
        self.actionBoundary_Condition.setText(QCoreApplication.translate("MainWindow", u"Boundary Condition", None))
        self.actionLoading.setText(QCoreApplication.translate("MainWindow", u"Loading ", None))
        self.actionContact_Us.setText(QCoreApplication.translate("MainWindow", u"Contact Us", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_block.setText(QCoreApplication.translate("MainWindow", u"Add Element Block", None))
        self.pushButton_steel.setText(QCoreApplication.translate("MainWindow", u"Add Steel Rod", None))
        self.pushButton_bc.setText(QCoreApplication.translate("MainWindow", u"Add Boundary", None))
        self.pushButton_load.setText(QCoreApplication.translate("MainWindow", u"Add Loading", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.checkBox_eleno.setText(QCoreApplication.translate("MainWindow", u"Element Number", None))
        self.checkBox_steel.setText(QCoreApplication.translate("MainWindow", u"Steel Rod", None))
        self.checkBox_bc.setText(QCoreApplication.translate("MainWindow", u"Boundary Condition", None))
        self.checkBox_load.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuManage.setTitle(QCoreApplication.translate("MainWindow", u"Manage", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

class Ui_Dialog_AddBlock(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(318, 144)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(9, 9, 299, 125))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.Xcoord = QLineEdit(self.formLayoutWidget)
        self.Xcoord.setObjectName(u"Xcoord")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Xcoord)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.Ycoord = QLineEdit(self.formLayoutWidget)
        self.Ycoord.setObjectName(u"Ycoord")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Ycoord)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.nBlockX = QLineEdit(self.formLayoutWidget)
        self.nBlockX.setObjectName(u"nBlockX")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.nBlockX)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.nBlockY = QLineEdit(self.formLayoutWidget)
        self.nBlockY.setObjectName(u"nBlockY")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.nBlockY)

        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.pushButton)

        self.buttonBox = QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.buttonBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Element Block", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Block bottom-left X coord", None))
        self.Xcoord.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Block bottom-left Y coord", None))
        self.Ycoord.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"No.of Blocks in X Direction", None))
        self.nBlockX.setText(QCoreApplication.translate("Dialog", u"10", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"No.of Blocks in Y Direction", None))
        self.nBlockY.setText(QCoreApplication.translate("Dialog", u"10", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Add Element Block", None))

class Ui_Dialog_AddSteel(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(318, 144)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(9, 9, 299, 125))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.InitXcoord = QLineEdit(self.formLayoutWidget)
        self.InitXcoord.setObjectName(u"InitXcoord")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.InitXcoord)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.InitYcoord = QLineEdit(self.formLayoutWidget)
        self.InitYcoord.setObjectName(u"InitYcoord")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.InitYcoord)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.FinXcoord = QLineEdit(self.formLayoutWidget)
        self.FinXcoord.setObjectName(u"FinXcoord")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.FinXcoord)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.FinYcoord = QLineEdit(self.formLayoutWidget)
        self.FinYcoord.setObjectName(u"FinYcoord")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.FinYcoord)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.Young = QLineEdit(self.formLayoutWidget)
        self.Young.setObjectName(u"Young")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.Young)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.Yield = QLineEdit(self.formLayoutWidget)
        self.Yield.setObjectName(u"Yield")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.Yield)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.Dia = QLineEdit(self.formLayoutWidget)
        self.Dia.setObjectName(u"Dia")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.Dia)

        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.pushButton)

        self.buttonBox = QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.buttonBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Steel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Steel Initial X coord", None))
        self.InitXcoord.setText(QCoreApplication.translate("Dialog", u"0.5", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Steel Initial Y coord", None))
        self.InitYcoord.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Steel Final X coord", None))
        self.FinXcoord.setText(QCoreApplication.translate("Dialog", u"0.5", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Steel Final Y coord", None))
        self.FinYcoord.setText(QCoreApplication.translate("Dialog", u"10.0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Steel Young's Modulus", None))
        self.Young.setText(QCoreApplication.translate("Dialog", u"2.0E+11", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Steel Yield Strength", None))
        self.Yield.setText(QCoreApplication.translate("Dialog", u"415.0E+06", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Steel Diameter", None))
        self.Dia.setText(QCoreApplication.translate("Dialog", u"0.01", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Add Steel", None))