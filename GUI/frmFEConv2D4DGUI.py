# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmFEConv2D4DGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmFEConv2D4D(object):
    def setupUi(self, frmFEConv2D4D):
        frmFEConv2D4D.setObjectName("frmFEConv2D4D")
        frmFEConv2D4D.resize(758, 729)
        self.btnInFile = QtWidgets.QPushButton(frmFEConv2D4D)
        self.btnInFile.setGeometry(QtCore.QRect(690, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmFEConv2D4D)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmFEConv2D4D)
        self.btnOutFile.setGeometry(QtCore.QRect(690, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmFEConv2D4D)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 521, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmFEConv2D4D)
        self.btnConvert.setGeometry(QtCore.QRect(590, 680, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmFEConv2D4D)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmFEConv2D4D)
        self.txtOutFile.setGeometry(QtCore.QRect(160, 60, 521, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmFEConv2D4D)
        self.btnClose.setGeometry(QtCore.QRect(30, 680, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmFEConv2D4D)
        self.tabWidget.setGeometry(QtCore.QRect(30, 100, 701, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtOTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTask.setGeometry(QtCore.QRect(420, 330, 113, 21))
        self.txtOTask.setObjectName("txtOTask")
        self.txtmLabel = QtWidgets.QComboBox(self.tab)
        self.txtmLabel.setGeometry(QtCore.QRect(260, 250, 121, 26))
        self.txtmLabel.setEditable(True)
        self.txtmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtmLabel.setObjectName("txtmLabel")
        self.cbmLabel = QtWidgets.QCheckBox(self.tab)
        self.cbmLabel.setGeometry(QtCore.QRect(140, 250, 111, 20))
        self.cbmLabel.setObjectName("cbmLabel")
        self.txtScan = QtWidgets.QComboBox(self.tab)
        self.txtScan.setGeometry(QtCore.QRect(260, 490, 121, 26))
        self.txtScan.setEditable(True)
        self.txtScan.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtScan.setObjectName("txtScan")
        self.txtTask = QtWidgets.QComboBox(self.tab)
        self.txtTask.setGeometry(QtCore.QRect(260, 330, 121, 26))
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.txtSubject = QtWidgets.QComboBox(self.tab)
        self.txtSubject.setGeometry(QtCore.QRect(260, 210, 121, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.txtOmLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOmLabel.setGeometry(QtCore.QRect(420, 250, 113, 21))
        self.txtOmLabel.setObjectName("txtOmLabel")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 60, 16))
        self.label_2.setObjectName("label_2")
        self.txtODM = QtWidgets.QLineEdit(self.tab)
        self.txtODM.setGeometry(QtCore.QRect(420, 290, 113, 21))
        self.txtODM.setObjectName("txtODM")
        self.cbTask = QtWidgets.QCheckBox(self.tab)
        self.cbTask.setGeometry(QtCore.QRect(140, 330, 81, 20))
        self.cbTask.setChecked(True)
        self.cbTask.setObjectName("cbTask")
        self.txtDM = QtWidgets.QComboBox(self.tab)
        self.txtDM.setGeometry(QtCore.QRect(260, 290, 121, 26))
        self.txtDM.setEditable(True)
        self.txtDM.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtDM.setObjectName("txtDM")
        self.cbNScan = QtWidgets.QCheckBox(self.tab)
        self.cbNScan.setGeometry(QtCore.QRect(140, 490, 91, 20))
        self.cbNScan.setChecked(False)
        self.cbNScan.setObjectName("cbNScan")
        self.cbCond = QtWidgets.QCheckBox(self.tab)
        self.cbCond.setGeometry(QtCore.QRect(140, 450, 101, 20))
        self.cbCond.setChecked(True)
        self.cbCond.setObjectName("cbCond")
        self.cbDM = QtWidgets.QCheckBox(self.tab)
        self.cbDM.setGeometry(QtCore.QRect(140, 290, 121, 20))
        self.cbDM.setChecked(False)
        self.cbDM.setObjectName("cbDM")
        self.txtCol = QtWidgets.QComboBox(self.tab)
        self.txtCol.setGeometry(QtCore.QRect(260, 90, 121, 26))
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
        self.txtOCond = QtWidgets.QLineEdit(self.tab)
        self.txtOCond.setGeometry(QtCore.QRect(420, 450, 113, 21))
        self.txtOCond.setObjectName("txtOCond")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(300, 20, 61, 16))
        self.label.setObjectName("label")
        self.txtOLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOLabel.setGeometry(QtCore.QRect(420, 170, 113, 21))
        self.txtOLabel.setObjectName("txtOLabel")
        self.txtCounter = QtWidgets.QComboBox(self.tab)
        self.txtCounter.setGeometry(QtCore.QRect(260, 410, 121, 26))
        self.txtCounter.setEditable(True)
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.txtLabel = QtWidgets.QComboBox(self.tab)
        self.txtLabel.setGeometry(QtCore.QRect(260, 170, 121, 26))
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtLabel.setObjectName("txtLabel")
        self.txtOScan = QtWidgets.QLineEdit(self.tab)
        self.txtOScan.setGeometry(QtCore.QRect(420, 490, 113, 21))
        self.txtOScan.setObjectName("txtOScan")
        self.cbCounter = QtWidgets.QCheckBox(self.tab)
        self.cbCounter.setGeometry(QtCore.QRect(140, 410, 81, 20))
        self.cbCounter.setChecked(False)
        self.cbCounter.setObjectName("cbCounter")
        self.txtOCol = QtWidgets.QLineEdit(self.tab)
        self.txtOCol.setGeometry(QtCore.QRect(420, 90, 113, 21))
        self.txtOCol.setObjectName("txtOCol")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(450, 20, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtData = QtWidgets.QComboBox(self.tab)
        self.txtData.setGeometry(QtCore.QRect(260, 50, 121, 26))
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.txtRun = QtWidgets.QComboBox(self.tab)
        self.txtRun.setGeometry(QtCore.QRect(260, 370, 121, 26))
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(260, 450, 121, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.txtOCounter = QtWidgets.QLineEdit(self.tab)
        self.txtOCounter.setGeometry(QtCore.QRect(420, 410, 113, 21))
        self.txtOCounter.setObjectName("txtOCounter")
        self.txtOSubject = QtWidgets.QLineEdit(self.tab)
        self.txtOSubject.setGeometry(QtCore.QRect(420, 210, 113, 21))
        self.txtOSubject.setObjectName("txtOSubject")
        self.cbRun = QtWidgets.QCheckBox(self.tab)
        self.cbRun.setGeometry(QtCore.QRect(140, 370, 81, 20))
        self.cbRun.setChecked(True)
        self.cbRun.setObjectName("cbRun")
        self.txtOData = QtWidgets.QLineEdit(self.tab)
        self.txtOData.setGeometry(QtCore.QRect(420, 50, 113, 21))
        self.txtOData.setObjectName("txtOData")
        self.txtORun = QtWidgets.QLineEdit(self.tab)
        self.txtORun.setGeometry(QtCore.QRect(420, 370, 113, 21))
        self.txtORun.setObjectName("txtORun")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(140, 90, 101, 16))
        self.label_4.setObjectName("label_4")
        self.cbLabel = QtWidgets.QCheckBox(self.tab)
        self.cbLabel.setGeometry(QtCore.QRect(140, 170, 111, 20))
        self.cbLabel.setObjectName("cbLabel")
        self.cbSubject = QtWidgets.QCheckBox(self.tab)
        self.cbSubject.setGeometry(QtCore.QRect(140, 210, 111, 20))
        self.cbSubject.setObjectName("cbSubject")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(140, 130, 101, 16))
        self.label_6.setObjectName("label_6")
        self.txtOImgShape = QtWidgets.QLineEdit(self.tab)
        self.txtOImgShape.setGeometry(QtCore.QRect(420, 130, 113, 21))
        self.txtOImgShape.setObjectName("txtOImgShape")
        self.txtImgShape = QtWidgets.QComboBox(self.tab)
        self.txtImgShape.setGeometry(QtCore.QRect(260, 130, 121, 26))
        self.txtImgShape.setEditable(True)
        self.txtImgShape.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtImgShape.setObjectName("txtImgShape")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.cbNormalize = QtWidgets.QCheckBox(self.tab_2)
        self.cbNormalize.setGeometry(QtCore.QRect(30, 30, 361, 21))
        self.cbNormalize.setCheckable(True)
        self.cbNormalize.setChecked(True)
        self.cbNormalize.setObjectName("cbNormalize")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 70, 651, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rb4DShape = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb4DShape.setGeometry(QtCore.QRect(20, 40, 181, 21))
        self.rb4DShape.setObjectName("rb4DShape")
        self.rb4DShape2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb4DShape2.setGeometry(QtCore.QRect(210, 40, 181, 21))
        self.rb4DShape2.setChecked(True)
        self.rb4DShape2.setObjectName("rb4DShape2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(frmFEConv2D4D)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmFEConv2D4D)
        frmFEConv2D4D.setTabOrder(self.txtInFile, self.btnInFile)
        frmFEConv2D4D.setTabOrder(self.btnInFile, self.txtOutFile)
        frmFEConv2D4D.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmFEConv2D4D.setTabOrder(self.btnOutFile, self.tabWidget)
        frmFEConv2D4D.setTabOrder(self.tabWidget, self.cbmLabel)
        frmFEConv2D4D.setTabOrder(self.cbmLabel, self.cbDM)
        frmFEConv2D4D.setTabOrder(self.cbDM, self.cbTask)
        frmFEConv2D4D.setTabOrder(self.cbTask, self.cbRun)
        frmFEConv2D4D.setTabOrder(self.cbRun, self.cbCounter)
        frmFEConv2D4D.setTabOrder(self.cbCounter, self.cbCond)
        frmFEConv2D4D.setTabOrder(self.cbCond, self.cbNScan)
        frmFEConv2D4D.setTabOrder(self.cbNScan, self.txtData)
        frmFEConv2D4D.setTabOrder(self.txtData, self.txtLabel)
        frmFEConv2D4D.setTabOrder(self.txtLabel, self.txtSubject)
        frmFEConv2D4D.setTabOrder(self.txtSubject, self.txtmLabel)
        frmFEConv2D4D.setTabOrder(self.txtmLabel, self.txtCol)
        frmFEConv2D4D.setTabOrder(self.txtCol, self.txtDM)
        frmFEConv2D4D.setTabOrder(self.txtDM, self.txtTask)
        frmFEConv2D4D.setTabOrder(self.txtTask, self.txtRun)
        frmFEConv2D4D.setTabOrder(self.txtRun, self.txtCounter)
        frmFEConv2D4D.setTabOrder(self.txtCounter, self.txtScan)
        frmFEConv2D4D.setTabOrder(self.txtScan, self.txtOData)
        frmFEConv2D4D.setTabOrder(self.txtOData, self.txtOLabel)
        frmFEConv2D4D.setTabOrder(self.txtOLabel, self.txtOSubject)
        frmFEConv2D4D.setTabOrder(self.txtOSubject, self.txtOmLabel)
        frmFEConv2D4D.setTabOrder(self.txtOmLabel, self.txtOCol)
        frmFEConv2D4D.setTabOrder(self.txtOCol, self.txtODM)
        frmFEConv2D4D.setTabOrder(self.txtODM, self.txtOTask)
        frmFEConv2D4D.setTabOrder(self.txtOTask, self.txtORun)
        frmFEConv2D4D.setTabOrder(self.txtORun, self.txtOCounter)
        frmFEConv2D4D.setTabOrder(self.txtOCounter, self.txtOCond)
        frmFEConv2D4D.setTabOrder(self.txtOCond, self.txtOScan)
        frmFEConv2D4D.setTabOrder(self.txtOScan, self.txtCond)
        frmFEConv2D4D.setTabOrder(self.txtCond, self.btnConvert)
        frmFEConv2D4D.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmFEConv2D4D):
        _translate = QtCore.QCoreApplication.translate
        frmFEConv2D4D.setWindowTitle(_translate("frmFEConv2D4D", "Convert 2D data to 4D"))
        self.btnInFile.setText(_translate("frmFEConv2D4D", "..."))
        self.label_33.setText(_translate("frmFEConv2D4D", "Input Data"))
        self.btnOutFile.setText(_translate("frmFEConv2D4D", "..."))
        self.btnConvert.setText(_translate("frmFEConv2D4D", "Convert"))
        self.label_35.setText(_translate("frmFEConv2D4D", "Output Data"))
        self.btnClose.setText(_translate("frmFEConv2D4D", "Close"))
        self.txtOTask.setText(_translate("frmFEConv2D4D", "task"))
        self.cbmLabel.setText(_translate("frmFEConv2D4D", "Label (matrix)"))
        self.txtOmLabel.setText(_translate("frmFEConv2D4D", "mlabel"))
        self.label_2.setText(_translate("frmFEConv2D4D", "Data"))
        self.txtODM.setText(_translate("frmFEConv2D4D", "design"))
        self.cbTask.setText(_translate("frmFEConv2D4D", "Task"))
        self.cbNScan.setText(_translate("frmFEConv2D4D", "NScan"))
        self.cbCond.setText(_translate("frmFEConv2D4D", "Condition"))
        self.cbDM.setText(_translate("frmFEConv2D4D", "Design Matrix"))
        self.txtOCond.setText(_translate("frmFEConv2D4D", "condition"))
        self.label.setText(_translate("frmFEConv2D4D", "Input"))
        self.txtOLabel.setText(_translate("frmFEConv2D4D", "label"))
        self.txtOScan.setText(_translate("frmFEConv2D4D", "nscan"))
        self.cbCounter.setText(_translate("frmFEConv2D4D", "Counter"))
        self.txtOCol.setText(_translate("frmFEConv2D4D", "coordinate"))
        self.label_5.setText(_translate("frmFEConv2D4D", "Output"))
        self.txtOCounter.setText(_translate("frmFEConv2D4D", "counter"))
        self.txtOSubject.setText(_translate("frmFEConv2D4D", "subject"))
        self.cbRun.setText(_translate("frmFEConv2D4D", "Run"))
        self.txtOData.setText(_translate("frmFEConv2D4D", "data"))
        self.txtORun.setText(_translate("frmFEConv2D4D", "run"))
        self.label_4.setText(_translate("frmFEConv2D4D", "Coordinate"))
        self.cbLabel.setText(_translate("frmFEConv2D4D", "Label"))
        self.cbSubject.setText(_translate("frmFEConv2D4D", "Subject"))
        self.label_6.setText(_translate("frmFEConv2D4D", "imgShape"))
        self.txtOImgShape.setText(_translate("frmFEConv2D4D", "imgShape"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFEConv2D4D", "Data"))
        self.cbNormalize.setText(_translate("frmFEConv2D4D", "Normilize Data X~N(0, 1)"))
        self.groupBox_2.setTitle(_translate("frmFEConv2D4D", "<Data Shape>"))
        self.rb4DShape.setText(_translate("frmFEConv2D4D", "4D (Tensor)"))
        self.rb4DShape2.setText(_translate("frmFEConv2D4D", "Boxed 4D (Tensor)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFEConv2D4D", "Parameters"))
