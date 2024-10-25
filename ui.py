# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lib/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#
# ALERT: Lines 11 through 35 implement a BETA dark mode UI. For now they 
# have to be manualy re-added every time you run pyuic5. 

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor

app = QApplication([])

app.setStyle("Fusion")

palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 320, 47, 13))
        self.label.setObjectName("label")
        self.blockName = QtWidgets.QLineEdit(self.centralwidget)
        self.blockName.setGeometry(QtCore.QRect(70, 320, 113, 20))
        self.blockName.setObjectName("blockName")
        self.blockCMD = QtWidgets.QLineEdit(self.centralwidget)
        self.blockCMD.setGeometry(QtCore.QRect(130, 380, 113, 20))
        self.blockCMD.setObjectName("blockCMD")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 380, 101, 16))
        self.label_4.setObjectName("label_4")
        self.blockDisplayName = QtWidgets.QLineEdit(self.centralwidget)
        self.blockDisplayName.setGeometry(QtCore.QRect(110, 290, 113, 20))
        self.blockDisplayName.setObjectName("blockDisplayName")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 350, 61, 16))
        self.label_6.setObjectName("label_6")
        self.blockBase = QtWidgets.QLineEdit(self.centralwidget)
        self.blockBase.setGeometry(QtCore.QRect(90, 350, 161, 20))
        self.blockBase.setText("")
        self.blockBase.setObjectName("blockBase")
        self.buttonAddBlock = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAddBlock.setGeometry(QtCore.QRect(80, 460, 75, 23))
        self.buttonAddBlock.setObjectName("buttonAddBlock")
        self.blockList = QtWidgets.QListWidget(self.centralwidget)
        self.blockList.setGeometry(QtCore.QRect(620, 50, 256, 192))
        self.blockList.setObjectName("blockList")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(540, -10, 21, 761))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(720, 30, 47, 13))
        self.label_9.setObjectName("label_9")
        self.buttonRemoveBlock = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRemoveBlock.setGeometry(QtCore.QRect(700, 250, 75, 23))
        self.buttonRemoveBlock.setObjectName("buttonRemoveBlock")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 250, 551, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(160, 70, 47, 13))
        self.label_10.setObjectName("label_10")
        self.packName = QtWidgets.QLineEdit(self.centralwidget)
        self.packName.setGeometry(QtCore.QRect(200, 70, 113, 20))
        self.packName.setObjectName("packName")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(160, 100, 61, 16))
        self.label_11.setObjectName("label_11")
        self.packNamespace = QtWidgets.QLineEdit(self.centralwidget)
        self.packNamespace.setGeometry(QtCore.QRect(220, 100, 113, 20))
        self.packNamespace.setObjectName("packNamespace")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(160, 130, 61, 16))
        self.label_12.setObjectName("label_12")
        self.packDescription = QtWidgets.QLineEdit(self.centralwidget)
        self.packDescription.setGeometry(QtCore.QRect(220, 130, 181, 20))
        self.packDescription.setObjectName("packDescription")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(160, 160, 47, 13))
        self.label_13.setObjectName("label_13")
        self.packVersion = QtWidgets.QComboBox(self.centralwidget)
        self.packVersion.setGeometry(QtCore.QRect(220, 160, 69, 22))
        self.packVersion.setObjectName("packVersion")
        self.packVersion.addItem("")
        self.buttonGeneratePack = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGeneratePack.setGeometry(QtCore.QRect(690, 390, 91, 23))
        self.buttonGeneratePack.setObjectName("buttonGeneratePack")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(150, 10, 281, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(170, 30, 131, 16))
        self.label_15.setObjectName("label_15")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setEnabled(False)
        self.status.setGeometry(QtCore.QRect(720, 420, 47, 13))
        self.status.setText("")
        self.status.setObjectName("status")
        self.blockTextureLabel = QtWidgets.QLabel(self.centralwidget)
        self.blockTextureLabel.setEnabled(False)
        self.blockTextureLabel.setGeometry(QtCore.QRect(290, 320, 47, 13))
        self.blockTextureLabel.setObjectName("blockTextureLabel")
        self.blockTexturePath = QtWidgets.QLineEdit(self.centralwidget)
        self.blockTexturePath.setEnabled(False)
        self.blockTexturePath.setGeometry(QtCore.QRect(340, 320, 113, 20))
        self.blockTexturePath.setObjectName("blockTexturePath")
        self.blockResourceCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.blockResourceCheckBox.setGeometry(QtCore.QRect(290, 290, 141, 17))
        self.blockResourceCheckBox.setObjectName("blockResourceCheckBox")
        self.blockModelLabel = QtWidgets.QLabel(self.centralwidget)
        self.blockModelLabel.setEnabled(False)
        self.blockModelLabel.setGeometry(QtCore.QRect(290, 350, 47, 13))
        self.blockModelLabel.setObjectName("blockModelLabel")
        self.blockModel = QtWidgets.QComboBox(self.centralwidget)
        self.blockModel.setEnabled(False)
        self.blockModel.setGeometry(QtCore.QRect(340, 350, 69, 22))
        self.blockModel.setObjectName("blockModel")
        self.blockModel.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 410, 47, 13))
        self.label_2.setObjectName("label_2")
        self.blockDrop = QtWidgets.QLineEdit(self.centralwidget)
        self.blockDrop.setGeometry(QtCore.QRect(70, 410, 113, 20))
        self.blockDrop.setObjectName("blockDrop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mDirt - A Datapack Tool for custom blocks"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.blockName.setPlaceholderText(_translate("MainWindow", "ruby_ore"))
        self.blockCMD.setPlaceholderText(_translate("MainWindow", "84231"))
        self.label_4.setText(_translate("MainWindow", "Custom Model Data:"))
        self.blockDisplayName.setPlaceholderText(_translate("MainWindow", "Ruby Ore"))
        self.label_5.setText(_translate("MainWindow", "Display Name:"))
        self.label_6.setText(_translate("MainWindow", "Base Block:"))
        self.blockBase.setPlaceholderText(_translate("MainWindow", "minecraft:stone"))
        self.buttonAddBlock.setText(_translate("MainWindow", "Add Block"))
        self.label_9.setText(_translate("MainWindow", "All Blocks"))
        self.buttonRemoveBlock.setText(_translate("MainWindow", "Remove"))
        self.label_10.setText(_translate("MainWindow", "Name:"))
        self.packName.setPlaceholderText(_translate("MainWindow", "The Ruby Pack"))
        self.label_11.setText(_translate("MainWindow", "Namespace:"))
        self.packNamespace.setPlaceholderText(_translate("MainWindow", "ores"))
        self.label_12.setText(_translate("MainWindow", "Description:"))
        self.packDescription.setPlaceholderText(_translate("MainWindow", "Adds new ores to Minecraft!"))
        self.label_13.setText(_translate("MainWindow", "Version:"))
        self.packVersion.setItemText(0, _translate("MainWindow", "1.21.3"))
        self.buttonGeneratePack.setText(_translate("MainWindow", "Generate Pack"))
        self.label_14.setText(_translate("MainWindow", "mDirt - A Datapack Tool for custom blocks"))
        self.label_15.setText(_translate("MainWindow", "Made by Jupiter Dev 2024"))
        self.blockTextureLabel.setText(_translate("MainWindow", "Texture:"))
        self.blockTexturePath.setPlaceholderText(_translate("MainWindow", "D:/textures/main.png"))
        self.blockResourceCheckBox.setText(_translate("MainWindow", "Create a Resource Pack?"))
        self.blockModelLabel.setText(_translate("MainWindow", "Model:"))
        self.blockModel.setItemText(0, _translate("MainWindow", "Block"))
        self.label_2.setText(_translate("MainWindow", "Drop:"))
        self.blockDrop.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">The item dropped when the block is broken.<br/>When empty, it will drop itself.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())