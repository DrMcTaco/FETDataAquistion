# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Keithley.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.plot = GraphicsLayoutWidget(self.centralwidget)
        self.plot.setObjectName("plot")
        self.verticalLayout_14.addWidget(self.plot)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setObjectName("Run")
        self.horizontalLayout_3.addWidget(self.Run)
        self.save = QtWidgets.QCheckBox(self.centralwidget)
        self.save.setChecked(False)
        self.save.setObjectName("save")
        self.horizontalLayout_3.addWidget(self.save)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.trigDelayLabel = QtWidgets.QLabel(self.centralwidget)
        self.trigDelayLabel.setObjectName("trigDelayLabel")
        self.verticalLayout_2.addWidget(self.trigDelayLabel)
        self.trigDelay = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.trigDelay.setMaximum(1000.0)
        self.trigDelay.setProperty("value", 100.0)
        self.trigDelay.setObjectName("trigDelay")
        self.verticalLayout_2.addWidget(self.trigDelay)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.currProtLabel = QtWidgets.QLabel(self.centralwidget)
        self.currProtLabel.setObjectName("currProtLabel")
        self.verticalLayout.addWidget(self.currProtLabel)
        self.currProt = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.currProt.setDecimals(2)
        self.currProt.setMaximum(1000.0)
        self.currProt.setSingleStep(0.1)
        self.currProt.setProperty("value", 100.0)
        self.currProt.setObjectName("currProt")
        self.verticalLayout.addWidget(self.currProt)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.fixedVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.fixedVoltageLabel.setMinimumSize(QtCore.QSize(101, 0))
        self.fixedVoltageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fixedVoltageLabel.setObjectName("fixedVoltageLabel")
        self.verticalLayout_12.addWidget(self.fixedVoltageLabel)
        self.fixedV = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.fixedV.setDecimals(3)
        self.fixedV.setMinimum(-150.0)
        self.fixedV.setMaximum(150.0)
        self.fixedV.setObjectName("fixedV")
        self.verticalLayout_12.addWidget(self.fixedV)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_14.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.instAddressGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.instAddressGBox.setObjectName("instAddressGBox")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.instAddressGBox)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sDLabel = QtWidgets.QLabel(self.instAddressGBox)
        self.sDLabel.setObjectName("sDLabel")
        self.verticalLayout_4.addWidget(self.sDLabel)
        self.sourceDrainAddress = QtWidgets.QComboBox(self.instAddressGBox)
        self.sourceDrainAddress.setObjectName("sourceDrainAddress")
        self.sourceDrainAddress.addItem("")
        self.verticalLayout_4.addWidget(self.sourceDrainAddress)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gateLabel = QtWidgets.QLabel(self.instAddressGBox)
        self.gateLabel.setObjectName("gateLabel")
        self.verticalLayout_5.addWidget(self.gateLabel)
        self.gateAddress = QtWidgets.QComboBox(self.instAddressGBox)
        self.gateAddress.setObjectName("gateAddress")
        self.gateAddress.addItem("")
        self.verticalLayout_5.addWidget(self.gateAddress)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addWidget(self.instAddressGBox)
        self.modeGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.modeGBox.setFlat(False)
        self.modeGBox.setCheckable(False)
        self.modeGBox.setObjectName("modeGBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.modeGBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioIV = QtWidgets.QRadioButton(self.modeGBox)
        self.radioIV.setChecked(True)
        self.radioIV.setObjectName("radioIV")
        self.horizontalLayout_4.addWidget(self.radioIV)
        self.radioGateSweep = QtWidgets.QRadioButton(self.modeGBox)
        self.radioGateSweep.setObjectName("radioGateSweep")
        self.horizontalLayout_4.addWidget(self.radioGateSweep)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.modeGBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.sweepParamGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sweepParamGBox.setObjectName("sweepParamGBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.sweepParamGBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.startLabel = QtWidgets.QLabel(self.sweepParamGBox)
        self.startLabel.setObjectName("startLabel")
        self.verticalLayout_9.addWidget(self.startLabel)
        self.start = QtWidgets.QDoubleSpinBox(self.sweepParamGBox)
        self.start.setDecimals(3)
        self.start.setMinimum(-150.0)
        self.start.setMaximum(150.0)
        self.start.setProperty("value", -1.0)
        self.start.setObjectName("start")
        self.verticalLayout_9.addWidget(self.start)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.stopLabel = QtWidgets.QLabel(self.sweepParamGBox)
        self.stopLabel.setObjectName("stopLabel")
        self.verticalLayout_11.addWidget(self.stopLabel)
        self.stop = QtWidgets.QDoubleSpinBox(self.sweepParamGBox)
        self.stop.setDecimals(3)
        self.stop.setMinimum(-150.0)
        self.stop.setMaximum(150.0)
        self.stop.setProperty("value", 1.0)
        self.stop.setObjectName("stop")
        self.verticalLayout_11.addWidget(self.stop)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.numPointsLabel = QtWidgets.QLabel(self.sweepParamGBox)
        self.numPointsLabel.setObjectName("numPointsLabel")
        self.verticalLayout_10.addWidget(self.numPointsLabel)
        self.numPoints = QtWidgets.QSpinBox(self.sweepParamGBox)
        self.numPoints.setProperty("value", 10)
        self.numPoints.setObjectName("numPoints")
        self.verticalLayout_10.addWidget(self.numPoints)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addWidget(self.sweepParamGBox)
        self.verticalLayout_14.addLayout(self.horizontalLayout)
        self.outDirectoryGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.outDirectoryGBox.setEnabled(False)
        self.outDirectoryGBox.setObjectName("outDirectoryGBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.outDirectoryGBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selectFile = QtWidgets.QPushButton(self.outDirectoryGBox)
        self.selectFile.setObjectName("selectFile")
        self.horizontalLayout_2.addWidget(self.selectFile)
        self.outDirectory = QtWidgets.QLineEdit(self.outDirectoryGBox)
        self.outDirectory.setObjectName("outDirectory")
        self.horizontalLayout_2.addWidget(self.outDirectory)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_14.addWidget(self.outDirectoryGBox)
        self.saveFileGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.saveFileGBox.setEnabled(False)
        self.saveFileGBox.setObjectName("saveFileGBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.saveFileGBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.saveFile = QtWidgets.QLineEdit(self.saveFileGBox)
        self.saveFile.setObjectName("saveFile")
        self.horizontalLayout_8.addWidget(self.saveFile)
        self.autoName = QtWidgets.QCheckBox(self.saveFileGBox)
        self.autoName.setChecked(True)
        self.autoName.setObjectName("autoName")
        self.horizontalLayout_8.addWidget(self.autoName)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.verticalLayout_14.addWidget(self.saveFileGBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3 Terminal Device Analysis"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.save.setText(_translate("MainWindow", "Save on Aquisition"))
        self.trigDelayLabel.setText(_translate("MainWindow", "Trigger Delay"))
        self.trigDelay.setSuffix(_translate("MainWindow", " ms"))
        self.currProtLabel.setText(_translate("MainWindow", "Current Protection"))
        self.currProt.setSuffix(_translate("MainWindow", " mA"))
        self.fixedVoltageLabel.setText(_translate("MainWindow", "Gate Voltage"))
        self.fixedV.setSuffix(_translate("MainWindow", " V"))
        self.instAddressGBox.setTitle(_translate("MainWindow", "Instrument Addresses"))
        self.sDLabel.setText(_translate("MainWindow", "Source-Drain "))
        self.sourceDrainAddress.setItemText(0, _translate("MainWindow", "(Re)Scan"))
        self.gateLabel.setText(_translate("MainWindow", "Gate"))
        self.gateAddress.setCurrentText(_translate("MainWindow", "(Re)Scan"))
        self.gateAddress.setItemText(0, _translate("MainWindow", "(Re)Scan"))
        self.modeGBox.setTitle(_translate("MainWindow", "Mode"))
        self.radioIV.setText(_translate("MainWindow", "I-V Curve"))
        self.radioGateSweep.setText(_translate("MainWindow", "Gate Sweep"))
        self.sweepParamGBox.setTitle(_translate("MainWindow", "Sweep Parameters"))
        self.startLabel.setText(_translate("MainWindow", "Start V"))
        self.start.setSuffix(_translate("MainWindow", " V"))
        self.stopLabel.setText(_translate("MainWindow", " Stop V"))
        self.stop.setSuffix(_translate("MainWindow", " V"))
        self.numPointsLabel.setText(_translate("MainWindow", "#of Points"))
        self.outDirectoryGBox.setTitle(_translate("MainWindow", "Output Directory"))
        self.selectFile.setText(_translate("MainWindow", "Browse"))
        self.saveFileGBox.setTitle(_translate("MainWindow", "Output File Name"))
        self.autoName.setText(_translate("MainWindow", "Auto Name"))

from pyqtgraph import GraphicsLayoutWidget