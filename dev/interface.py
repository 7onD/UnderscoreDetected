# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(556, 465)
        Form.setStyleSheet("background-color: black;")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 350, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: black; /* Цвет текста в кнопке */\n"
"background: white; /* Фоновый цвет */\n"
"padding: 10px; /* Отступ текста от границ - определяет размер кнопки */\n"
"font-size: 20px; /* Размер текста */\n"
"border-radius: 5px; /* Закругление уголков */\n"
"box-shadow: 0px 1px 3px; /* Тень */\n"
"border: 2px solid red; /* Параметры рамки */\n"
"}\n"
"\n"
"QPushButton:hover { /* Добавляем псевдокласс :hover */\n"
"background: red;/* Меняем фоновый цвет */\n"
"color: white; /* Меняем цвет текста */\n"
"box-shadow: inset 0 0 0 3px #3a7999; /* Меняем тень */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 350, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: black; /* Цвет текста в кнопке */\n"
"background: white; /* Фоновый цвет */\n"
"padding: 10px; /* Отступ текста от границ - определяет размер кнопки */\n"
"font-size: 20px; /* Размер текста */\n"
"border-radius: 5px; /* Закругление уголков */\n"
"box-shadow: 0px 1px 3px; /* Тень */\n"
"border: 2px solid red; /* Параметры рамки */\n"
"}\n"
"\n"
"QPushButton:hover { /* Добавляем псевдокласс :hover */\n"
"background: red;/* Меняем фоновый цвет */\n"
"color: white; /* Меняем цвет текста */\n"
"box-shadow: inset 0 0 0 3px #3a7999; /* Меняем тень */\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 20, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(60, 100, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color:white")
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(70, 200, 401, 111))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Удалить _"))
        self.pushButton_2.setText(_translate("Form", "Добавить _"))
        self.label.setText(_translate("Form", "UnderscoreDetected"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Утилита</span><span style=\" font-size:14pt;\">, которая умеет заменять все пробелы в тексте на подчеркивания, и наобарот.</span></p></body></html>"))
