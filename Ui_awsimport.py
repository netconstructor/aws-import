# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_awsimport.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_awsimport(object):
    def setupUi(self, awsimport):
        awsimport.setObjectName("awsimport")
        awsimport.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(awsimport)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(awsimport)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), awsimport.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), awsimport.reject)
        QtCore.QMetaObject.connectSlotsByName(awsimport)

    def retranslateUi(self, awsimport):
        awsimport.setWindowTitle(QtGui.QApplication.translate("awsimport", "awsimport", None, QtGui.QApplication.UnicodeUTF8))
