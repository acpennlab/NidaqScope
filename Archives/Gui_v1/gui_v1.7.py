import sip
sip.setapi('QString',2)
sip.setapi('QVariant',2)
import sys
from pyqtgraph.Qt import QtCore, QtGui,  uic
import pyqtgraph as pg
import os
import nidaq_scope
#from PyQt4 import QtCore, QtGui, uic
#from PyQt4.QtCore import *
from PyQt4.QtGui import QMessageBox

qtCreatorFile = "C:\Users\Public\Documents\Samuel\Gui_v1\gui_v1.9.ui" 
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
                        'output':[],
                        'acq4_dir':[],
                        'fname':[]}
def load(self):
        r = open(settings['fname'], 'r')
        lines = r.readlines()
        #########################################################
        # Retrieve settings line by line
        line0 = lines[0].rstrip()
        line1 = int(lines[1].rstrip())
        line2 = int(lines[2].rstrip())
        line3 = int(lines[3].rstrip())
        line4 = lines[4].rstrip()
        line5 = lines[5].rstrip()
        line6 = lines[6].rstrip()
        line7 = lines[7].rstrip()
        line8 = float(lines[8].rstrip())
        line9 = lines[9].rstrip()
        line10 = int(lines[10].rstrip())
        line11 = int(lines[11].rstrip())
        line12 = lines[12].rstrip()
        line13 = lines[13].rstrip()
        line14 = lines[14].rstrip()
        
        #########################################################
        # Change boxes to settings
        if line0 == 'False':
            self.save_check.setChecked(False)
        elif line0 == 'True':
            self.save_check.setChecked(True)
        self.rate_spinner.setValue(line1)
        self.fc_box.setValue(line2)
        self.window_size_spinner.setValue(line3)
        self.ai_channel_box.setText(line4)
        self.ai_channel2_box.setText(line5)
        self.current_directory.setText(line6)
        if line7 == 'Differential':
            self.config_combo.setCurrentIndex(0)
        elif line7 == 'NRSE':
            self.config_combo.setCurrentIndex(1)
        elif line7 == 'RSE':
            self.config_combo.setCurrentIndex(2)
        self.ai_limit_box.setValue(line8)
        if line9 == 'False':
            self.amps_radio.click()
        elif line9 == 'True':
            self.volts_radio.click()
        self.scale_box.setValue(line10)
        self.gain_spinner.setValue(line11)
        self.notes_box.setText(line12)
        if line14 == 'Generic':
            self.amplifier_box.setCurrentIndex(0)
        elif line14 == 'MultiClamp700':
            self.amplifier_box.setCurrentIndex(1)
        elif line14 == 'Axopatch200':
            self.amplifier_box.setCurrentIndex(2)
        self.acq4_path.setText(line13)

                        
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
        self.load_default_button.clicked.connect(self.load_default)
        self.save_default_button.clicked.connect(self.save_default)
        self.acq4_button.clicked.connect(self.set_acq4_dir)
        #########################################################
        # Loading last used settings
        settings['fname'] = '_settings.txt'
        try:
            load(self)
        except:
            f = open('Default 1.txt','w+')
            f.write('False\n20000\n4000\n1000\n/Dev1/ai0\nNone\n\nDifferential\n10.0\nTrue\n1\n1\n\n\nGeneric')
            f.close()

            
        ############################################################
        # Setting up Values
        global update_values 
        def update_values():
            save = settings['save'] =(self.save_check.isChecked())
            rate = settings['rate'] =(self.rate_spinner.value())
            fc = settings['fc'] =(self.fc_box.value())
            settings['win_size'] =(self.window_size_spinner.value())
            win_size = settings['win_size']/float(1000.00) 
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
            acq4_directory = settings['acq4_dir'] = (self.acq4_path.text())            
            if amplifier == "Generic":
                scope = "nidaq_scope.scope("
                settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", " + str(ai_channel_format) + ", '" + str(save_dir)+ "', '" + str(config) + "', " + str(limits_format)  + ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", '" + str(notes) + "')"
                #settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", " + str(ai_channel_format) + ", '" + str(save_dir)+ "', '" + str(config) + "', " + str(limits_format)  + ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", '" + str(notes) + "', '" + str(acq4_directory) + "')"
            if settings['amplifier'] == "MultiClamp700":
                scope = "nidaq_scope.mc700scope("
                settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(fc) + ", " + str(win_size) + ", " + str(ai_channel_format) + ", '" + str(save_dir) + "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", '" + str(notes) +  "')"
                #settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(fc) + ", " + str(win_size) + ", " + str(ai_channel_format) + ", '" + str(save_dir) + "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", '" + str(notes) + "', '" + str(acq4_directory) + "')"

        
    def load_default(self):
        settings['fname'] = (self.default_combo.currentText()) + ".txt"
        try:
            load(self)
        except:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("This default has not been set yet")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.setWindowTitle("Unsuccessful Load")
            self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            self.msg.exec_()
            

    
    def save_default(self):
        fname = (self.default_combo.currentText()) + ".txt"
        if fname == 'Default 1.txt':
            self.defaulterror = QMessageBox()
            self.defaulterror.setIcon(QMessageBox.Warning)
            self.defaulterror.setText("You cannot override Default 1\nNow say you are sorry.")
            self.defaulterror.addButton(QtGui.QPushButton("I'm sorry"),QtGui.QMessageBox.YesRole)
            self.defaulterror.setWindowTitle('Error')
            self.defaulterror.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            self.defaulterror.exec_()
        else:
            f = open(fname,'w+')
            f.write(str(settings['save']) + '\n' + str(settings['rate'])+ '\n' + str(settings['fc'])+ '\n' + str(settings['win_size'])+ '\n' + str(settings['ai_channel'])+ 
            '\n' + str(settings['ai_channel2'])+ '\n' + str(settings['save_dir'])+ '\n' + str(settings['config'])+ '\n' + str(settings['limits'])+ '\n' + str(settings['unit'])+ 
            '\n' + str(settings['scale'])+ '\n' + str(settings['gain'])+ '\n' + str(settings['notes'])+ '\n' + str(settings['acq4_dir'])+ '\n' + str(settings['amplifier']))
            f.close()
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Current settings have been successfully saved")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.setWindowTitle("Save Successful")
            self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            self.msg.exec_()
    
    def set_acq4_dir(self):
        ac_dir = QtGui.QFileDialog.getExistingDirectory(self, 'Set ACQ4 Directory')
        self.acq4_path.setText(ac_dir)
    
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
     
if __name__ == "__main__":
    app = QtGui.QApplication.instance() # sets up QApplication if there isnt one already
    if not app:
        app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show() # Shows gui
    timer = QtCore.QTimer() # Starts timer to refresh settings every 0.1s
    timer.timeout.connect(update_values)
    timer.start(100)
    while (1): #Lets the user do the command as much as they want
        raw_input('Press Enter to start oscilloscope.\n')
        #output = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", '" + str(ai_channel_format) + "', '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", " + str(notes) + ")"
        #print settings['output']
        if settings['save'] == True and settings['save_dir'] == "":
            print "You have not chosen a save directory. Please choose one and try again."
        else:
            exec(settings['output'])
            f = open('_settings.txt','w+')
            f.write(str(settings['save']) + '\n' + str(settings['rate'])+ '\n' + str(settings['fc'])+ '\n' + str(settings['win_size'])+ '\n' + str(settings['ai_channel'])+ 
            '\n' + str(settings['ai_channel2'])+ '\n' + str(settings['save_dir'])+ '\n' + str(settings['config'])+ '\n' + str(settings['limits'])+ '\n' + str(settings['unit'])+ 
            '\n' + str(settings['scale'])+ '\n' + str(settings['gain'])+ '\n' + str(settings['notes'])+ '\n' + str(settings['acq4_dir'])+ '\n' + str(settings['amplifier']))
            f.close()
    sys.exit(app.exec_())