from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(927, 506)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(927, 506))
        MainWindow.setMaximumSize(QtCore.QSize(927, 506))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/fb-icon-9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(210, 330, 511, 111))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 250, 93, 28))
        self.pushButton.clicked.connect(self.button_click)
        self.pushButton.setObjectName("pushButton")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(198, 140, 541, 31))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setFocusPolicy(Qt.NoFocus)
        self.horizontalSlider_2.setRange(1, 150)

        self.horizontalSlider_2.valueChanged.connect(self.valu2)


        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(760, 130, 101, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.textChanged.connect(self.value4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(760, 50, 101, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.value3)



        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(200, 50, 541, 31))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setFocusPolicy(Qt.NoFocus)
        self.horizontalSlider.setRange(1, 200)

        self.horizontalSlider.valueChanged.connect(self.valu)
        self.horizontalSlider.setObjectName("horizontalSlider")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def valu2(self):
        self.k = str(self.horizontalSlider_2.value())
        self.lineEdit_2.setText(self.k)


    def valu(self):
        self.a = str(self.horizontalSlider.value())
        self.lineEdit.setText(self.a)

    def value3(self):
        self.j=str(self.lineEdit.text())
        self.horizontalSlider.setSliderPosition(int(self.j))
        if int(self.j)==0:
            self.horizontalSlider.setSliderPosition(int(1))

    def value4(self):
        self.j=str(self.lineEdit_2.text())
        self.horizontalSlider_2.setSliderPosition(int(self.j))
        if int(self.j)==0:
            self.horizontalSlider.setSliderPosition(int(1))


    def button_click(self):
        self.j = int(self.lineEdit_2.text())
        self.k = int(self.lineEdit.text())
        self.bmi =self.j/((self.k/100)**2)
        self.string="your body mass index is "+str(self.bmi)
        print (self.string)
        self.plainTextEdit.setPlainText(self.string)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BMI"))
        self.pushButton.setText(_translate("MainWindow", "calculate"))
        self.label_2.setText(_translate("MainWindow", "weight"))
        self.label.setText(_translate("MainWindow", "height"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())