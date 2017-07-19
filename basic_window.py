# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:28:51 2017

@author: Dan
"""

import sys
import visa
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QComboBox, QLabel

class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Keithley')
        self.lbl = QLabel("Inst1", self)
        rm = visa.ResourceManager()
        instruments = rm.list_resources()
        inst1 = QComboBox(self)
        
        for instrument in instruments:
            inst1.addItem(instrument)
        
        inst1.move(50,50)
        self.lbl.move(50,150)
        inst1.activated[str].connect(self.onActivated)
        
        self.show()
        
    def onActivated(self, text):
      
        self.lbl.setText(text)
        self.lbl.adjustSize()  
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = 0
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    
if __name__ == '__main__':
    main()