import sip
sip.setapi('QString',2)
sip.setapi('QVariant',2)
import sys
import os
from pyqtgraph.Qt import QtCore, QtGui,  uic
import pyqtgraph as pg
import nidaq_scope
#from PyQt4 import QtCore, QtGui, uic
#from PyQt4.QtCore import *
#from PyQt4.QtGui import QMessageBox

qtCreatorFile = "C:\Users\Public\Documents\Samuel\Gui_v1\gui_v1.6.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Settings dictionary
settings = {'save':[],
                        'rate':[],
                        'fc':[],
                        'win_size':[],
                        'ai_channel':[],
                        'ai_channel2':[],
                        'ai_channel_format':[],
                        'save_dir':[None], 
                        'config':[], 
                        'limits':[], 
                        'limits_format':[],
                        'unit':[], 
                        'scale':[], 
                        'gain':[], 
                        'notes':[], 
                        'amplifier':[], 
                        'scope':[],
                        'output':[]}
                        
# Gui                        
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint 
        )
        self.directory_button.clicked.connect(self.browse)
        self.excecute_button.clicked.connect(self.leave)
        self.amplifier_box.currentIndexChanged.connect(self.grey)
        self.action_Default1.triggered.connect(self.default1)
        self.action_Default2.triggered.connect(self.default2)
        ############################################################
        # Setting up Values
        global update_values 
        def update_values():
            save = settings['save'] =(self.save_check.isChecked())
            rate = settings['rate'] =(self.rate_spinner.value())
            fc = settings['fc'] =(self.fc_box.value())
            win_size =settings['win_size'] =(self.window_size_spinner.value())/float(1000.00) 
            ai_channel = settings['ai_channel'] =(self.ai_channel_box.displayText())
            ai_channel2 = settings['ai_channel2'] = (self.ai_channel2_box.displayText())
            if ai_channel2 == "None" or ai_channel2 == "":
                ai_channel_format = settings['ai_channel_format'] = str( "'" + ai_channel + "'")
            else:
                ai_channel_format = str("['" + ai_channel + "','" + ai_channel2 + "']")
            save_dir = settings['save_dir'] =(self.current_directory.text())
            if save_dir == "":
                save_dir = "."
            config = settings['config'] =(self.config_combo.currentText()) 
            if  config =="Differential":
                config ="DIFFERENTIAL"
            limits = settings['limits'] =(self.ai_limit_box.value()) 
            unit = settings['unit'] =(self.volts_radio.isChecked()) 
            if  unit ==True:
                unit ='V'
            if  unit ==False:
                unit ='A'
            scale = settings['scale'] =(self.scale_box.value()) 
            gain = settings['gain'] =(self.gain_spinner.value()) 
            notes = settings['notes'] =(self.notes_box.toPlainText()) 
            if  notes =="":
                notes ="None"
            amplifier = settings['amplifier'] =(self.amplifier_box.currentText()) 
            limits_format = settings['limits_format'] ="[-" + str(limits) + "," + str(limits) + "]"            
            if amplifier == "Generic":
                scope = "nidaq_scope.scope("
                settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", " + str(ai_channel_format) + ", '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", '" + str(notes) + "')"
            if settings['amplifier'] == "MultiClamp700":
                scope = "nidaq_scope.mc700scope("
                settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(fc) + ", " + str(win_size) + ", " + str(ai_channel_format) + ", '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", '" + str(notes) + "')"

    def browse(self): # Dialog to set save directory
        cd=QtGui.QFileDialog.getExistingDirectory(self, 'Set Directory')
        self.current_directory.setText(cd)
    
    def leave (self): # Exit button
        os._exit(1)
    
    def grey(self): # Greys out boxes upon choosing amplifier
        amplifier = (self.amplifier_box.currentText())
        if amplifier == "Generic":
            self.fc_box.setEnabled(False)
        if amplifier == "MultiClamp700":
            self.fc_box.setEnabled(True)
        if amplifier == "Axopatch200":
            self.fc_box.setEnabled(True)
     
    def default1(self): #Preprogrammed default 1
        self.window_size_spinner.setValue(1000)
        self.rate_spinner.setValue(10000)
        self.ai_channel_box.setText('/Dev1/ai0')
        self.ai_channel2_box.setText('None')
        self.config_combo.setCurrentIndex(0)
        self.ai_limit_box.setValue(1.1)
        self.amplifier_box.setCurrentIndex(0)
        self.fc_box.setValue(1000)
        self.amps_radio.click()
        self.scale_box.setValue(1)
        self.gain_spinner.setValue(1)

    def default2(self): #Preprogrammed default 1
        self.window_size_spinner.setValue(2000)
        self.rate_spinner.setValue(20000)
        self.ai_channel_box.setText('/Dev1/ai0')
        self.ai_channel2_box.setText('/Dev1/ai2')
        self.config_combo.setCurrentIndex(1)
        self.ai_limit_box.setValue(2.2)
        self.amplifier_box.setCurrentIndex(1)
        self.fc_box.setValue(2000)
        self.volts_radio.click()
        self.scale_box.setValue(2)
        self.gain_spinner.setValue(2)

if __name__ == "__main__":
    app = QtGui.QApplication.instance() # sets up QApplication if there isnt one already
    if not app:
        app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show() # Shows gui
    timer = pg.QtCore.QTimer() # Starts timer to refresh settings every 0.1s
    timer.timeout.connect(update_values)
    timer.start(100)
    while (1): #Lets the user do the command as much as they want
        raw_input('Press Enter to start oscilloscope.\n')
        #output = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", '" + str(ai_channel_format) + "', '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", " + str(notes) + ")"
        print settings['output']
        if settings['save'] == True and settings['save_dir'] == "":
            print "You have not chosen a save directory. Please choose one and try again."
        else:
            exec(settings['output'])
    sys.exit(app.exec_())