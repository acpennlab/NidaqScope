import sip
sip.setapi('QString',2)
sip.setapi('QVariant',2)
import sys
from pyqtgraph.Qt import QtCore, QtGui,  uic
#from PyQt4 import QtCore, QtGui, uic
import pyqtgraph as pg
#from PyQt4.QtCore import *
#from PyQt4.QtGui import QMessageBox, 
import os
import nidaq_scope

qtCreatorFile = "C:\Users\Public\Documents\Samuel\gui2.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.directory_button.clicked.connect(self.browse)
        self.excecute_button.clicked.connect(self.leave)
        self.amplifier_box.currentIndexChanged.connect(self.grey)
        ############################################################
        # Setting up Values
        global update_values 
        def update_values():
            global save
            save =(self.save_check.isChecked())
            global rate
            rate =(self.rate_spinner.value())
            global fc
            fc =(self.fc_box.value())
            global win_size
            win_size =(self.window_size_spinner.value())/float(1000.00) # win_size = number
            global ai_channel
            ai_channel ='/Dev1/ai0' # ai_channel = what they put
            global save_dir
            save_dir =(self.current_directory.text())# save_dir = the cd
            if save_dir == "":
                save_dir = "."
            global config
            config =(self.config_combo.currentText()) # config = what they chose
            if  config =="Differential":
                config ="DIFFERENTIAL"
            global limits
            limits =(self.ai_limit_box.value()) # limits = single integer
            global unit
            unit =(self.volts_radio.isChecked()) # unit = True if volts is checked, unit = False if amps is checked
            if  unit ==True:
                unit ='V'
            if  unit ==False:
                unit ='A'
            global scale
            scale =(self.scale_box.value()) # scale = integer
            global gain
            gain =(self.gain_spinner.value()) # gain = integer
            global notes
            notes =(self.notes_box.toPlainText()) # notes
            if  notes =="":
                notes ="None"
            global amplifier
            amplifier =(self.amplifier_box.currentText()) # amplifier = what they chose
            if amplifier == "Generic":
                global scope
                scope = "nidaq_scope.scope("
            if amplifier == "MultiClamp700":
                scope = "nidaq_scope.mc700scope("
            global limits_format
            limits_format ="[-" + str(limits) + "," + str(limits) + "]"


    def browse(self):
        cd=QtGui.QFileDialog.getExistingDirectory(self, 'Set Directory')
        self.current_directory.setText(cd)
    
    def leave (self):
        sys.exit()
    
    def grey(self):
        amplifier = (self.amplifier_box.currentText())
        if amplifier == "Generic":
            self.fc_box.setEnabled(False)
        if amplifier == "MultiClamp700":
            self.fc_box.setEnabled(True)
        if amplifier == "Axopatch200":
            self.fc_box.setEnabled(True)
            
    def excecute(self):
        save = (self.save_check.isChecked()) # save is 1 if checked, 0 if not
        rate = (self.rate_spinner.value()) # rate = integer
        fc = (self.fc_box.value()) # fc for when using multiclamp700
        win_size = (self.window_size_spinner.value())/float(1000.00) # win_size = number
        ai_channel = (self.ai_channel_box.displayText()) # ai_channel = what they put
        save_dir = (self.current_directory.text()) # save_dir = the cd
        config = (self.config_combo.currentText()) # config = what they chose
        limits = (self.ai_limit_box.value()) # limits = single integer
        unit = (self.volts_radio.isChecked()) # unit = True if volts is checked, unit = False if amps is checked
        scale = (self.scale_box.value()) # scale = integer
        gain = (self.gain_spinner.value()) # gain = integer
        notes = (self.notes_box.toPlainText()) # notes
        amplifier = (self.amplifier_box.currentText()) # amplifier = what they chose
        limits_format = "[-" + str(limits) + "," + str(limits) + "]"
        if  unit == True:
            unit = "V"
        if  unit == False:
            unit = "A"
        if  notes == "":
            notes = "None"
        if  config == "Differential":
            config = "DIFFERENTIAL"

        if ai_channel == "" : # THIS IS NEW, REPLACE OLD ONE
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("The following variables were left blank:\nAI channel type")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        elif save == True and save_dir == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("There was no save directory chosen.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            
        
        else:
            if  save_dir == "":
                save_dir = "."
            if amplifier == "Generic":
                output = "nidaq_scope.scope(" + str(save) + ", " + str(rate) + ", " + str(win_size) + ", '" + str(ai_channel) + "', '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", " + str(unit)+ ", " + str(scale)+ ", " + str(gain)+ ", " + str(notes) + ")"
            if amplifier == "MultiClamp700":
                output = "nidaq_scope.mc700scope(" + str(save) + ", " + str(rate) + ", " + str(fc) + ", " + str(win_size) + ", '" + str(ai_channel) + "', '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", " + str(unit)+ ", " + str(scale)+ ", " + str(gain)+ ", " + str(notes) + ")"
            #print output
            exec(output)



        
        



if __name__ == "__main__":
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update_values)
    timer.start(100)
    while (1):
        raw_input('Press Enter to start.\n')
        #scope = "nidaq_scope.scope("
        output = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", '" + str(ai_channel) + "', '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", " + str(notes) + ")"
        print output
        exec(output)
    sys.exit(app.exec_())