import sip
sip.setapi('QString',2)
sip.setapi('QVariant',2)
import sys
from pyqtgraph.Qt import QtCore, QtGui,  uic
import pyqtgraph as pg
import os
import nidaq_scope

qtCreatorFile = "C:\Users\Public\Documents\Samuel\Gui_v1\gui_v1.3.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Settings dictionary
settings = {'save':[],
                        'rate':[],
                        'fc':[],
                        'win_size':[],
                        'ai_channel':[],
                        'save_dir':[None], 
                        'config':[], 
                        'limits':[], 
                        'unit':[], 
                        'scale':[], 
                        'gain':[], 
                        'notes':[], 
                        'amplifier':[], 
                        'limits_format':[],
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
        ############################################################
        # Setting up Values
        global update_values 
        def update_values():
            save = settings['save'] =(self.save_check.isChecked())
            rate = settings['rate'] =(self.rate_spinner.value())
            fc = settings['fc'] =(self.fc_box.value())
            win_size =settings['win_size'] =(self.window_size_spinner.value())/float(1000.00) 
            ai_channel = settings['ai_channel'] ='/Dev1/ai0' 
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
                settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", '" + str(ai_channel) + "', '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", '" + str(notes) + "')"
            if settings['amplifier'] == "MultiClamp700":
                scope = "nidaq_scope.mc700scope("
                settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(fc) + ", " + str(win_size) + ", '" + str(ai_channel) + "', '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", '" + str(notes) + "')"

    def browse(self): # Dialog to set save directory
        cd=QtGui.QFileDialog.getExistingDirectory(self, 'Set Directory')
        self.current_directory.setText(cd)
    
    def leave (self): # Exit button
        #sys.exit()
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
    timer = pg.QtCore.QTimer() # Starts timer to refresh settings every 0.1s
    timer.timeout.connect(update_values)
    timer.start(100)
    while (1): #Lets the user do the command as much as they want
        raw_input('Press Enter to start oscilloscope.\n')
        #scope = "nidaq_scope.scope("
        #output = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", '" + str(ai_channel) + "', '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", " + str(notes) + ")"
        print settings['output']
        if settings['save'] == True and settings['save_dir'] == "":
            print "You have not chosen a save directory. Please choose one and try again."
        else:
            exec(settings['output'])
    #sys.exit(app.exec_())