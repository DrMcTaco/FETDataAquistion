 # -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:09:01 2017

@author: Dan
"""

import sys, visa
from ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from scipy import signal
import numpy as np

class APP(QtWidgets.QMainWindow):
   
#TODO: Multithreading    
#TODO: Save Data
    def __init__(self):
        ####Setup GUI and draw elements from UI file#########
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ###Connect all interactive UI elements to functions###        
        self.ui.gateAddress.activated.connect(self.updateGateAddress)
        self.ui.sourceDrainAddress.activated.connect(self.updateSourceDrainAddress)       
        self.ui.Run.clicked.connect(self.run)
        self.ui.radioIV.toggled.connect(self.modeChange)
        self.ui.radioIV.toggled.connect(self.autoName)
        self.ui.fixedV.valueChanged.connect(self.autoName)
        self.ui.selectFile.clicked.connect(self.setSaveDir)
        self.ui.save.stateChanged.connect(self.saveState)
#        self.ui.autoName.
        
        ###Initialize Variables###
        self.outputFileName = ''
        self.mode = 0 #I-V(0) or Gate Sweep(1)
        self.messageDuration = 5000#ms
        self.rm = visa.ResourceManager()
        self.gateAddress='None'
        self.gateKeithley=0
        self.sourceDrainAddress='None'
        self.sourceDrainKeithley=0
        self.voltages=[]
        self.currents=[]
        self.gateLeak=[]
        self.fixedValue=0
        
        ###Initial Population of Instrument lists and other elements###
        self.initUI()
        
        
    #Toggle ui based on save state 
    def saveState(self):
        if not self.ui.save.isChecked():
            self.ui.outDirectoryGBox.setEnabled(False)
            self.ui.saveFileGBox.setEnabled(False)
        elif self.ui.save.isChecked():
            self.ui.outDirectoryGBox.setEnabled(True)
            self.ui.saveFileGBox.setEnabled(True)
        
        
     #generate auto savefile name   
    def autoName(self):
        if self.ui.autoName.isChecked():
            if self.mode == 0:
                self.outputFileName = 'I-V Vg=' + str(self.ui.fixedV.value()) + 'V'
                self.ui.saveFile.setText(self.outputFileName)
            elif self.mode == 1:
                self.outputFileName ='Gate Sweep Vsd=' + str(self.ui.fixedV.value()) + 'V'
                self.ui.saveFile.setText(self.outputFileName)
        
        
    #set save file directory    
    def setSaveDir(self):
        folderName = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.outDirectory.setText(folderName)
        
    #Handle switching between I-V curves and Gate Sweeps
    def modeChange(self):
        if self.ui.radioIV.isChecked():
            self.mode = 0
            self.ui.fixedVoltageLabel.setText('Gate Voltage')
        elif self.ui.radioGateSweep.isChecked():
            self.mode = 1
            self.ui.fixedVoltageLabel.setText('Source-Drain Voltage')
        
        
    #Updated the address of the Gate Sourcing Keithley
    def updateGateAddress(self):
        if self.ui.gateAddress.currentText() == '(Re)Scan':
            self.refreshInstList()
        else:
            self.gateAddress = self.ui.gateAddress.currentText()
        
        
    #Updated the address of the Source Drain Sourcing Keithley
    def updateSourceDrainAddress(self):
        if self.ui.sourceDrainAddress.currentText() == '(Re)Scan':
            self.refreshInstList()
        else:
            self.sourceDrainAddress = self.ui.sourceDrainAddress.currentText()
        
        
   #Starts the data collection for both modes of opperation
    def run(self):
        #TODO: make sure addresses are valid Keithley adresses before interfacing with them
        try:
            self.checkAddress()                     
            self.gateKeithley.timeout = 90000
            self.sourceDrainKeithley.timeout = 90000
            
            if self.mode == 1:
                #Initialize and run GateSweep
                self.ui.statusbar.showMessage('Preforming Gate Sweep Measurement')
                self.gateSweep()
                self.ui.statusbar.clearMessage()
            elif self.mode == 0:
                #Initialize and Run I-V Curve
                self.ui.statusbar.showMessage('Preforming I-V curve')
                self.iVCurve()
                self.ui.statusbar.clearMessage()
                
        except (DeviceError) as err:
            self.ui.statusbar.showMessage('Bad Instrument Address or Parameter', self.messageDuration)
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle('Incorrect Instrument Selected')
            message = 'You have selected a(n) ' + err.args[1] + '\n This is an incompatable device to take measurements with.\n Please Select a Keithley 2400 Source Meter.'
            msgBox.setText(message)
            msgBox.exec_()
            
        
        #ensure all device addresses are different and it is safe to collect data
    def checkAddress(self):
        #TODO: Rewrite and reimpliment to check for valid address on selection. When both are valid enable 'Run'button.
        modelString = 'MODEL 2400'
        self.sourceDrainKeithley = self.rm.open_resource(self.sourceDrainAddress)
        self.gateKeithley = self.rm.open_resource(self.gateAddress)
        
        ident = self.sourceDrainKeithley.query('*IDN?')
        if ident.__contains__(modelString):
            pass
        else:
            self.sourceDrainKeithley.close()
            self.gateKeithley.close()
            raise DeviceError(self.sourceDrainAddress, ident )
            
        ident = self.gateKeithley.query('*IDN?')
        if ident.__contains__(modelString):
            self.ui.Run.setEnabled(True)
        else:
            self.sourceDrainKeithley.close()
            self.gateKeithley.close()
            raise DeviceError(self.gateAddress, ident )
    
    
    #preform I-v curve Measurement
    def iVCurve(self):
        self.voltages = self.triangleWave(self.ui.start.value(), self.ui.stop.value(), self.ui.numPoints.value())
        myList = ','.join(map(str, ['{:.4f}'.format(x) for x in self.voltages]))
        try:
            self.sendCMD(self.sourceDrainKeithley,'*RST')
            self.sendCMD(self.gateKeithley,'*RST')
            self.sendCMD(self.sourceDrainKeithley,':SYST:BEEP:STAT OFF')
            self.sendCMD(self.gateKeithley,':SYST:BEEP:STAT OFF')
            self.sendCMD(self.sourceDrainKeithley, ':sens:func:conc off')
            self.sendCMD(self.sourceDrainKeithley, ':sour:func volt')
            self.sendCMD(self.gateKeithley, ':sour:func volt')
            self.sendCMD(self.sourceDrainKeithley, ':sens:func "curr:dc"')
            self.sendCMD(self.sourceDrainKeithley, ':SENS:CURR:PROT ' + str(self.ui.currProt.value()/1000))
            self.sendCMD(self.gateKeithley, ':SENS:CURR:PROT ' + str(self.ui.currProt.value()/1000))
            self.sendCMD(self.sourceDrainKeithley, ':SOUR:VOLT:MODE LIST')
            self.sendCMD(self.gateKeithley, ':SOUR:VOLT:MODE FIXED')
            self.sendCMD(self.sourceDrainKeithley,':SOUR:LIST:VOLT ' + myList)
            self.sendCMD(self.gateKeithley,':SOUR:VOLT:LEV ' + str(self.ui.fixedV.value()))
            self.sendCMD(self.sourceDrainKeithley, ':TRIG:COUN ' + str(2 * self.ui.numPoints.value()))
            self.sendCMD(self.sourceDrainKeithley, ':sour:del ' + str(self.ui.trigDelay.value()/1000))
            self.sendCMD(self.sourceDrainKeithley,'outp ON')
            self.sendCMD(self.gateKeithley,'outp ON')
            temp = self.sourceDrainKeithley.query_ascii_values(':READ?')
            self.sendCMD(self.sourceDrainKeithley, 'OUTP OFF')
            self.sendCMD(self.gateKeithley,'OUTP OFF')
            self.currents = temp[1::5]
            self.p1.clear()
            self.p1.setTitle('I-V Curve: Vg = ' + str(self.ui.fixedV.value()) + 'V')
            self.p1.plot(self.voltages, self.currents, pen=None, symbol='o')
            
            if self.ui.save.isChecked():
                self.saveData()
            
        except(CommandError) as err:
            print(err.args)


    def saveData(self):
         with open(self.ui.outDirectory.text() + '\\' + self.ui.saveFile.text() + '.txt', 'w') as fHandle:
             fHandle.write('Voltage \t Current \t ')
        

    #preform Gate sweep measurement
    def gateSweep(self):
        self.voltages = self.triangleWave(self.ui.start.value(), self.ui.stop.value(), self.ui.numPoints.value())
        self.currents = np.zeros(len(self.voltages))
        self.gateLeak = np.zeros(len(self.voltages))
        i = 0
        
        try:
            self.sendCMD(self.sourceDrainKeithley,'*RST')
            self.sendCMD(self.gateKeithley,'*RST')
            self.sendCMD(self.sourceDrainKeithley,':SYST:BEEP:STAT OFF')
            self.sendCMD(self.gateKeithley,':SYST:BEEP:STAT OFF')
            self.sendCMD(self.sourceDrainKeithley, ':SOUR:VOLT:MODE FIXED')
            self.sendCMD(self.gateKeithley, ':SOUR:VOLT:MODE FIXED')
            self.sendCMD(self.sourceDrainKeithley, ':SENS:CURR:PROT ' + str(self.ui.currProt.value()/1000))
            self.sendCMD(self.gateKeithley, ':SENS:CURR:PROT ' + str(self.ui.currProt.value()/1000))
            self.sendCMD(self.sourceDrainKeithley, ':sens:func "curr:dc"')
            self.sendCMD(self.gateKeithley, ':sens:func "curr:dc"')
            self.sendCMD(self.sourceDrainKeithley,':SOUR:VOLT:LEV 0')
            self.sendCMD(self.gateKeithley,':SOUR:VOLT:LEV ' + str(self.ui.fixedV.value()))
            self.sendCMD(self.sourceDrainKeithley, ':sour:del ' + str(self.ui.trigDelay.value()/1000))
            self.sendCMD(self.gateKeithley, ':sour:del ' + str(self.ui.trigDelay.value()/1000))
            self.sendCMD(self.sourceDrainKeithley, ':FORM:ELEM CURR')
            self.sendCMD(self.gateKeithley, ':FORM:ELEM CURR')
            self.sendCMD(self.sourceDrainKeithley,'outp ON')
            self.sendCMD(self.gateKeithley,'outp ON')
            self.p1.clear()
            self.p1.setTitle('Gate Sweep Curve: Vsd = ' + str(self.ui.fixedV.value()) + 'V')
            
            for i in range(len(self.voltages)):
                self.sendCMD(self.sourceDrainKeithley,':SOUR:VOLT:LEV ' + str(self.voltages[i]))
                self.currents[i] = self.sourceDrainKeithley.query_ascii_values(':READ?')[0]
                self.gateLeak[i] = self.gateKeithley.query_ascii_values(':READ?')[0]
                self.p1.plot([self.voltages[i]], [self.currents[i]], pen=None, symbol='o')
                i= i + 1
                
            self.sendCMD(self.sourceDrainKeithley, 'OUTP OFF')
            self.sendCMD(self.gateKeithley,'OUTP OFF')

            if self.ui.save.isChecked():
                self.saveData()
            
        except(CommandError) as err:
            print(err.args)
   
    
    #create voltage values for sweeps
    def triangleWave(self, start, stop, numPoints):
        try:
            x = np.linspace(start, stop, 2.0*numPoints)
            voltages = ((stop - start)/2.0) * (signal.sawtooth((2.0 * np.pi * (x - (stop- start) * start / (2.0 * (stop-start))) / (stop - start)) , 0.5)) + (start + stop) / 2.0
            return voltages
        except ZeroDivisionError:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle('Start and Stop Values are the Same')
            message = 'You have selected idnetical Start and Stop values for the sweep. This results in a divide by zero error. Please check you inputs.'
            msgBox.setText(message)
            msgBox.exec_()
    
    
   #rescan for avalable instruments
    def refreshInstList(self):        
        self.instruments = self.rm.list_resources()
        self.ui.gateAddress.clear()
        self.ui.sourceDrainAddress.clear()
        self.ui.gateAddress.addItem('(Re)Scan')
        self.ui.sourceDrainAddress.addItem('(Re)Scan')
        
        for instrument in self.instruments:#add instruments to list
            if instrument.split('::')[0].__contains__('GPIB'):
                self.ui.gateAddress.addItem(instrument)
                self.ui.sourceDrainAddress.addItem(instrument)
    
    
   #Initialize the UI features
    def initUI(self):
        self.refreshInstList()
        self.p1 = self.ui.plot.addPlot()
        self.p1.setLabel('bottom', text='Voltage', units='V')
        self.p1.setLabel('left', text='Current', units='A')
        self.p1.enableAutoRange(axis = 'x')
        
        
   #safe command sending to the Keithleys
    def sendCMD(self, inst, cmdString):  
        inst.write(cmdString)
        temp = inst.query(':SYST:ERR:ALL?')
        if not(temp[0] == '0'):
            raise CommandError(str(inst), cmdString, temp)
            
            
  #Error handling Classes      
class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class CommandError(Error):
    """Exception raised for errors sending commands to the Keithley.

    Attributes:
        address -- address of violating device
        command -- input expression in which the error occurred
        message -- explanation of the error
    """


    def __init__(self,address, command, message):
        self.address = address
        self.command = command
        self.message = message
   
     
class DeviceError(Error):
    """Exception raised for errors trying to connect to a non Keithley instrument.

    Attributes:
        address -- address of violating device
        ID -- ID of violating device
    """

    
    def __init__(self, address, ID):
        self.address = address
        self.ID = ID

   
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = APP()
    myapp.show()
    sys.exit(app.exec_())