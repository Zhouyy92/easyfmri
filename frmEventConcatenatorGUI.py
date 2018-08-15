# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEventConcatenatorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmEventConcatenator(object):
    def setupUi(self, frmEventConcatenator):
        frmEventConcatenator.setObjectName("frmEventConcatenator")
        frmEventConcatenator.resize(813, 232)
        self.label = QtWidgets.QLabel(frmEventConcatenator)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(frmEventConcatenator)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 101, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(frmEventConcatenator)
        self.label_3.setGeometry(QtCore.QRect(630, 16, 141, 17))
        self.label_3.setObjectName("label_3")
        self.btnFFile = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnFFile.setGeometry(QtCore.QRect(560, 10, 51, 32))
        self.btnFFile.setObjectName("btnFFile")
        self.txtFFile = QtWidgets.QLineEdit(frmEventConcatenator)
        self.txtFFile.setGeometry(QtCore.QRect(119, 15, 431, 21))
        self.txtFFile.setStatusTip("")
        self.txtFFile.setText("")
        self.txtFFile.setObjectName("txtFFile")
        self.btnSFile = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnSFile.setGeometry(QtCore.QRect(561, 55, 51, 32))
        self.btnSFile.setObjectName("btnSFile")
        self.txtSFile = QtWidgets.QLineEdit(frmEventConcatenator)
        self.txtSFile.setGeometry(QtCore.QRect(120, 60, 431, 21))
        self.txtSFile.setStatusTip("")
        self.txtSFile.setText("")
        self.txtSFile.setObjectName("txtSFile")
        self.txtfDim = QtWidgets.QSpinBox(frmEventConcatenator)
        self.txtfDim.setGeometry(QtCore.QRect(690, 10, 111, 29))
        self.txtfDim.setMinimum(0)
        self.txtfDim.setMaximum(1000000000)
        self.txtfDim.setProperty("value", 1)
        self.txtfDim.setObjectName("txtfDim")
        self.btnClose = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnClose.setGeometry(QtCore.QRect(520, 190, 131, 29))
        self.btnClose.setObjectName("btnClose")
        self.btnConcatenate = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnConcatenate.setGeometry(QtCore.QRect(670, 190, 131, 29))
        self.btnConcatenate.setObjectName("btnConcatenate")
        self.btnOFile = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnOFile.setGeometry(QtCore.QRect(561, 101, 51, 32))
        self.btnOFile.setObjectName("btnOFile")
        self.txtOFile = QtWidgets.QLineEdit(frmEventConcatenator)
        self.txtOFile.setGeometry(QtCore.QRect(120, 106, 431, 21))
        self.txtOFile.setStatusTip("")
        self.txtOFile.setText("")
        self.txtOFile.setObjectName("txtOFile")
        self.label_4 = QtWidgets.QLabel(frmEventConcatenator)
        self.label_4.setGeometry(QtCore.QRect(20, 106, 101, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(frmEventConcatenator)
        self.label_5.setGeometry(QtCore.QRect(630, 66, 141, 17))
        self.label_5.setObjectName("label_5")
        self.txtsDim = QtWidgets.QSpinBox(frmEventConcatenator)
        self.txtsDim.setGeometry(QtCore.QRect(690, 60, 111, 29))
        self.txtsDim.setMinimum(0)
        self.txtsDim.setMaximum(1000000000)
        self.txtsDim.setProperty("value", 1)
        self.txtsDim.setObjectName("txtsDim")
        self.label_6 = QtWidgets.QLabel(frmEventConcatenator)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 101, 17))
        self.label_6.setObjectName("label_6")
        self.txtHDR = QtWidgets.QLineEdit(frmEventConcatenator)
        self.txtHDR.setGeometry(QtCore.QRect(120, 150, 681, 21))
        self.txtHDR.setStatusTip("")
        self.txtHDR.setText("")
        self.txtHDR.setObjectName("txtHDR")

        self.retranslateUi(frmEventConcatenator)
        QtCore.QMetaObject.connectSlotsByName(frmEventConcatenator)

    def retranslateUi(self, frmEventConcatenator):
        _translate = QtCore.QCoreApplication.translate
        frmEventConcatenator.setWindowTitle(_translate("frmEventConcatenator", "Event Concatenator"))
        self.label.setText(_translate("frmEventConcatenator", "First File:"))
        self.label_2.setText(_translate("frmEventConcatenator", "Second File:"))
        self.label_3.setText(_translate("frmEventConcatenator", "Offset:"))
        self.btnFFile.setText(_translate("frmEventConcatenator", "..."))
        self.txtFFile.setToolTip(_translate("frmEventConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.btnSFile.setText(_translate("frmEventConcatenator", "..."))
        self.txtSFile.setToolTip(_translate("frmEventConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.btnClose.setText(_translate("frmEventConcatenator", "Close"))
        self.btnConcatenate.setText(_translate("frmEventConcatenator", "Concatenate"))
        self.btnOFile.setText(_translate("frmEventConcatenator", "..."))
        self.txtOFile.setToolTip(_translate("frmEventConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.label_4.setText(_translate("frmEventConcatenator", "Output:"))
        self.label_5.setText(_translate("frmEventConcatenator", "Offset:"))
        self.label_6.setText(_translate("frmEventConcatenator", "Header:"))
        self.txtHDR.setToolTip(_translate("frmEventConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))

