from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from functions import underscore_delete, underscore_add
from interface import Ui_Form
import pyautogui as pg
import pyperclip

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

def delete_bp():
	text = ui.textEdit.toPlainText()
	pr = underscore_delete(text)
	pyperclip.copy(f'{pr}')
	pg.alert(f"Следущий текст скопирован к вам в бувер обмена (ctrl+v): \n {pr}", "Done", button="Продолжить")

def add_bp():
	text = ui.textEdit.toPlainText()
	pr = underscore_add(text)
	pyperclip.copy(f'{pr}')
	pg.alert(f"Следущий текст скопирован к вам в бувер обмена (ctrl+v): \n {pr}", "Done", button="Продолжить")

ui.pushButton.clicked.connect(delete_bp)
ui.pushButton_2.clicked.connect(add_bp)

sys.exit(app.exec_())