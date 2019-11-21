import io
import binascii
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from mydesign import Ui_Dialog  # импорт нашего сгенерированного файла
from PyQt5.QtCore import pyqtSlot
import sys

class Mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(Mywindow, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.qrexp = QRegExp('([A-Fa-f0-9][A-Fa-f0-9](\ )?){0,16}')
		self.validator = QRegExpValidator(self.qrexp)
		self.ui.lineEdit.setValidator(self.validator)
		self.ui.pushButton.clicked.connect(self._work)

	def bin_format(self, integer, length):
		return f'{integer:0>{length}b}'

	def bit_ord(self, str_came):
		i = 0
		str_out = ''
		while (i < len(str_came)):
			str_in = str_came[i] + str_came[i + 1]
			bin_out = self.bin_format(int(str_in, 16), len(str_in))
			one_amount = 0
			for j in bin_out:
				if j is '1':
					one_amount += 1
			flag = False
			if (one_amount % 2) == 0:
				if bin_out[len(bin_out) - 1] == '0':
					bin_out = bin_out[:len(bin_out) - 1]
					bin_out += '1'
					flag = True
				if bin_out[len(bin_out) - 1] == '1' and flag != True:
					bin_out = bin_out[:len(bin_out) - 1]
					bin_out += '0'
			a = hex(int(bin_out, 2))
			if len(a) != 4:
				b = '0x0'
				b += a[2:]
				a = b
			str_out += a[2:]
			
			i += 2
		return str_out

	@pyqtSlot()
	def _work(self):
		str = self.ui.lineEdit.text()
		str_2 = ''
		for i in str:
			if i == ' ':
				continue
			else:
				str_2 += i
		if len(str_2) % 2 != 0:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error")
			#msg.setInformativeText(self._error)
			msg.setWindowTitle("Error")
			try:
				sys.exit(msg.exec())
			except:
				return
		
		str_out = self.bit_ord(str_2)
		str_out_2 = ''
		j = 0
		for i in str_out:
			if j == 0:
				str_out_2 += i
				j += 1
				continue
			if j == 1:
				str_out_2 += i
				str_out_2 += ' '
				j = 0
				continue
		self.ui.lineEdit.setText(str_out_2)


app = QtWidgets.QApplication([])
application = Mywindow()
application.show()
try:
	sys.exit(app.exec())
except  SystemExit:
	pass
