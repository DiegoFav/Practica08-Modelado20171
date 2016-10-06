# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic 

formClass , baseClass = uic.loadUiType("servidor.ui")

class ServidorApp(formClass, baseClass):
	def __init__(self):
		formClass.__init__(self)
		baseClass.__init__(self)
		self.setupUi(self)
		self.table.horizontalHeader().setResizeMode(1)
		self.table.verticalHeader().setResizeMode(1)
		self.show()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = ServidorApp()
	sys.exit(app.exec_())
