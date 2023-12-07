from PyQt5 import sip
import sys
import os
import numpy as np
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QDialog, QFileDialog
from PyQt5 import QtCore, uic
import nidaq_scope

#Need next 3 for inside
#from pyqtgraph.Qt import QtCore, QtGui,  uic
import pyqtgraph as pg
#import nidaq_scope

#Need these 2 for outside
#from PyQt4 import QtCore, QtGui, uic
#from PyQt4.QtCore import *

from New_Amplifier import Amplifier_Dialog
from Edit_Pulse import Pulse_Dialog


qtCreatorFile = "./nidaq_scope_gui.ui" #Path for ui file
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

settings = {'save':[], # Settings dictionary
                        'rate':[],
                        'fc':[],
                        'win_size':[],
                        'ai_channel':[],
                        'ai_channel2':[],
                        'ai_channel_format':[],
                        'save_dir':[], 
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
                        'fname':[],
                        'gain_telegraph':[],
                        'fc_telegraph':[],
                        'units_telegraph':[],
                        'gaintele':[],
                        'fctele':[],
                        'modetele':[],
                        'script_dir':[],
                        'commander_scale':[],
                        'prepulse':[1],
                        'pulse_amp':[-0.01],
                        'pulse_length':[0.01],
                        'postpulse':[8.99],
                        'holding':[-0.06],						
                        'pulse':[True]}
                                      
def load(self): # Sets up ability to load 
        load_dir = os.path.normpath(os.path.join(settings['script_dir'], 'Defaults', settings['fname']))
        #load_dir = os.path.normpath(os.path.join(settings['script_dir'], 'Defaults', settings['fname']))
        r = open(load_dir, 'r')
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
        line10 = lines[10].rstrip()
        line11 = float(lines[11].rstrip())
        line12 = lines[12].rstrip()
        line13 = lines[13].rstrip()
        line14 = lines[14].rstrip()
        line15 = lines[15].rstrip()
        line16 = lines[16].rstrip()
        line17 = lines[17].rstrip()
        line18 = lines[18].rstrip()
        line19 = lines[19].rstrip()
        line20 = lines[20].rstrip()		
        line21 = lines[21].rstrip()		
        line22 = lines[22].rstrip()		
        line23 = lines[23].rstrip()		
        line24 = lines[24].rstrip() 
 
        #########################################################
        # Change boxes to _settings
        if line0 == 'False':
            self.save_check.setChecked(False)
        elif line0 == 'True':
            self.save_check.setChecked(True)
        self.rate_spinner.setValue(line1)
        self.fc_spinner.setValue(line2)
        self.window_size_spinner.setValue(line3)
        self.ai_channel_box.setText(line4)
        self.ai_channel2_box.setText(line5)
        self.current_directory.setText(line6)
        if line7 == 'DIFFERENTIAL':
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
        self.scale_box.setText(line10)
        self.gain_spinner.setValue(line11)
        self.notes_box.setText(line12)
        index = self.amplifier_box.findText(line17)
        self.amplifier_box.setCurrentIndex(index)
        self.acq4_path.setText(line13)
        self.gain_telegraph.setText(line14)
        self.fc_telegraph.setText(line15)
        self.units_telegraph.setText(line16)

        settings['prepulse'] = line18
        settings['pulse_amp'] = line19
        settings['pulse_length'] = line20
        settings['postpulse'] = line21
        settings['holding'] = line22
        settings['commander_scale'] = line23

        if line24 == 'False':
             self.pulse_check.setChecked(False)
        elif line24 == 'True':
             self.pulse_check.setChecked(True)
        update_nidaq_values()
        r.close()		

def nosave(): #Error check between save and save_dir
    update_nidaq_values()
    nosave = QMessageBox()
    nosave.setIcon(QMessageBox.Warning)
    nosave.setText("You have not chosen a save directory. Please choose one and try again")
    nosave.setStandardButtons(QMessageBox.Ok)
    nosave.setWindowTitle("No Save Directory")
    nosave.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    nosave.exec_()
  
def func(): #Sends command to amplifier
	
    if settings['output'] == []:
        return
    else:
        exec(settings['output'])
        os.chdir(settings['script_dir'])
        settings_path = os.path.normpath(os.path.join(settings['script_dir'], 'Defaults', '_settings.txt'))
        f = open(settings_path,'w+')
        f.write(str(settings['save']) + '\n' + str(settings['rate'])+ '\n' + str(settings['fc'])+ '\n' + str(settings['win_size'])+ '\n' + str(settings['ai_channel'])+ 
        '\n' + str(settings['ai_channel2'])+ '\n' + str(settings['save_dir'])+ '\n' + str(settings['config'])+ '\n' + str(settings['limits'])+ '\n' + str(settings['unit'])+ 
        '\n' + str(settings['scale'])+ '\n' + str(settings['gain'])+ '\n' + str(settings['notes'])+ '\n' + str(settings['acq4_dir'])+
        '\n' + str(settings['gain_telegraph']) + '\n' + str(settings['fc_telegraph']) + '\n' + str(settings['units_telegraph']) + '\n' + str(settings['amplifier'])+
        '\n' + str(settings['prepulse']) + '\n' + str(settings['pulse_amp']) + '\n' + str(settings['pulse_length']) + '\n' + str(settings['postpulse'])+
        '\n' + str(settings['holding']) + '\n' + str(settings['commander_scale']) + '\n' + str(settings['pulse']))
        f.close()
	

	
	# Gui                        
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window |QtCore.Qt.CustomizeWindowHint |QtCore.Qt.WindowTitleHint )
        settings['script_dir'] = os.getcwd()
        self.get_amplifiers()
        self.directory_button.clicked.connect(self.browse)
        self.excecute_button.clicked.connect(self.leave)
        self.amplifier_box.activated.connect(self.get_dict)
        self.default_combo.currentIndexChanged.connect(self.grey_save)
        self.load_default_button.clicked.connect(self.load_default)
        self.save_default_button.clicked.connect(self.save_default)
        self.update_gain_fc_unit.clicked.connect(self.update_gain_fc_units_func)
        self.acq4_button.clicked.connect(self.set_acq4_dir)
        self.create_telegraph_dictionary.clicked.connect(self.other_window)
        self.pulse_button.clicked.connect(self.pulse_window)
        self.scale_box.editingFinished.connect(self.evaluate_scale_box)
        
		############################################################
        # Setting up Values for contiuous updating
        global update_nidaq_values
        def update_nidaq_values():
            save = settings['save'] =(self.save_check.isChecked())
            rate = settings['rate'] =(self.rate_spinner.value())
            fc = settings['fc'] =(self.fc_spinner.value())            
            settings['win_size'] =(self.window_size_spinner.value())
            win_size = settings['win_size']/float(1000.00) 
            ai_channel = settings['ai_channel'] =(self.ai_channel_box.displayText())
            ai_channel2 = settings['ai_channel2'] = (self.ai_channel2_box.displayText())
            if ai_channel2 == "None" or ai_channel2 == "":
                ai_channel_format = settings['ai_channel_format'] = str( "'" + ai_channel + "'")
            else:
                ai_channel_format = str("['" + ai_channel + "','" + ai_channel2 + "']")
            settings['save_dir'] = save_dir = (self.current_directory.text())
            save_dir = save_dir.replace('\\','/')
            if save_dir == "":
                save_dir = "."
            config = settings['config'] =(self.config_combo.currentText()) 
            limits = settings['limits'] =(self.ai_limit_box.value()) 
            unit = settings['unit'] =(self.volts_radio.isChecked()) 
            if  unit ==True:
                unit ='V'
            if  unit ==False:
                unit ='A'
            scale = settings['scale'] =(self.scale_box.displayText()) 
            gain = settings['gain'] =(self.gain_spinner.value())
            notes = settings['notes'] =(self.notes_box.toPlainText()) 
            if  notes =="":
                notes ="None"
            settings['amplifier'] =(self.amplifier_box.currentText()) 
            limits_format = settings['limits_format'] ="[-" + str(limits) + "," + str(limits) + "]"  
            settings['acq4_dir'] = (self.acq4_path.text())
            acq4_directory = settings['acq4_dir'].replace('\\','/')
            settings['gain_telegraph'] = (self.gain_telegraph.displayText())
            settings['fc_telegraph'] = (self.fc_telegraph.displayText())
            settings['units_telegraph'] = (self.units_telegraph.displayText())
            pulse = settings['pulse'] = (self.pulse_check.isChecked())
            if settings['amplifier'] == 'Please Select Your Amplifier':
                settings['output'] = []
            elif settings['amplifier'] == "MultiClamp700":
                rec_settings = ""
                rec_settings += "Amplifier: %s; " % (settings['amplifier'])
                rec_settings += "Amplifier scale: %s; " % (settings['scale'])
                rec_settings += "Amplifier gain: %s; " % (settings['gain'])
                rec_settings += "Amplifier low-pass filter cutoff: %s Hz; " % (settings['fc'])
                rec_settings += "Sampling rate: %s Hz; " % (settings['rate'])
                rec_settings += "Unit of recorded signal: %s; " % (unit)
                rec_settings += "Test pulse? %s; " % (settings['pulse'])
                rec_settings += "Holding command: %s (mV or pA); " % (settings['holding'])
                rec_settings += "Test pulse interval: %s s; " % (np.float64(settings['win_size'])/1000)
                rec_settings += "Test pulse start: %s s; " % (np.float64(settings['prepulse'])/1000)
                rec_settings += "Duration of test pulse: %s s; " % (settings['pulse_length'])
                rec_settings += "Amplitude of test pulse: %s (mV or pA); " % (settings['pulse_amp'])  
                scope = "nidaq_scope.mc700scope("
                settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(fc) + ", " + str(win_size) + ", " + str(ai_channel_format) + ", '" + str(save_dir)  + "', '" + str(config)+ "', " + str(limits_format) + ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain) + ", '" + str(rec_settings + "Notes: " + notes) + "', '" + str(acq4_directory) + "', " + str(settings['prepulse']) + ", " + str(settings['pulse_amp'])  + ", " + str(settings['pulse_length']) + ", " + str(settings['postpulse']) + ", " + str(settings['holding'])  + ", " + str(settings['commander_scale']) + ", " + str(pulse) + ")"
            else:
                scope = "nidaq_scope.scope("
                settings['output'] = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", " + str(ai_channel_format) + ", '" + str(save_dir)  + "', '" + str(config) + "', " + str(limits_format)  + ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", '" + str(rec_settings + "Notes: " + notes) + "', " + str(settings['prepulse']) + ", " + str(settings['pulse_amp']) + ", " + str(settings['pulse_length']) + ", " + str(settings['postpulse']) + ", " + str(settings['holding']) + ", " + str(settings['commander_scale']) + ", "  +  str(pulse) + ")"

        #########################################################
        # Loads last successfully used settings
        settings['fname'] = '_settings.txt'
        
        self.get_dict()
        try:
            load(self)
        except:
            if not os.path.exists('Defaults'):
                os.mkdir('Defaults')
            def_dir = os.path.normpath(os.path.join(settings['script_dir'], 'Defaults', 'Default.txt'))
            f = open(def_dir,'w+')
            f.write('False\n20000\n4000\n1000\n/Dev1/ai0\nNone\n\nDIFF\n10.0\nTrue\n1\n1\n\n\n\n\n\nBasic\n1\n-0.01\n0.01\n8.99\n-0.06\n1000\nFalse')
            f.close()
            settings['commander_scale']=1000
            settings['prepulse']=1.0
            settings['pulse_amp']=-0.01
            settings['pulse_length']=0.01
            settings['postpulse']=8.99
            settings['holding']=-0.06
            
    def evaluate_scale_box(self): #Changes the scale box to a floating point
        current_scale = self.scale_box.displayText()
        try: 
            floated = float(current_scale)
            stringed = str(floated)
            self.scale_box.setText(stringed)
        except:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("The text in the scale box needs to be a number.\n It may be in scientific notation")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.setWindowTitle("Error in Format")
            self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            self.msg.exec_()
		
    def grey_save(self): #Greys out the save button, preventing override of "Default"
        preset_text = (self.default_combo.currentText())
        if preset_text == 'Default':
            self.save_default_button.setEnabled(False)
        else:
            self.save_default_button.setEnabled(True)
        update_nidaq_values()

    def load_default(self): # Sets up loading defaults
        settings['fname'] = (self.default_combo.currentText()) + ".txt"
        try:
            window.get_dict()
            load(self)
        except:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("This preset has not yet been set")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.setWindowTitle("Unsuccessful Load")
            self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            self.msg.exec_()
                
    def save_default(self): # Sets up saving defaults
        update_nidaq_values()
        fname = (self.default_combo.currentText()) + ".txt"
        fpath = os.path.normpath(os.path.join(settings['script_dir'], 'Defaults', fname))
        f = open(fpath,'w+')
        f.write(str(settings['save']) + '\n' + str(settings['rate'])+ '\n' + str(settings['fc'])+ '\n' + str(settings['win_size'])+ '\n' + str(settings['ai_channel'])+ 
        '\n' + str(settings['ai_channel2'])+ '\n' + str(settings['save_dir'])+ '\n' + str(settings['config'])+ '\n' + str(settings['limits'])+ '\n' + str(settings['unit'])+ 
        '\n' + str(settings['scale'])+ '\n' + str(settings['gain'])+ '\n' + str(settings['notes'])+ '\n' + str(settings['acq4_dir'])+ 
        '\n' + str(settings['gain_telegraph']) + '\n' + str(settings['fc_telegraph']) + '\n' + str(settings['units_telegraph']) + '\n' + str(settings['amplifier'])+ 
        '\n' + str(settings['prepulse']) + '\n' + str(settings['pulse_amp']) + '\n' + str(settings['pulse_length']) + '\n' + str(settings['postpulse'])+
        '\n' + str(settings['holding']) + '\n' + str(settings['commander_scale']) + '\n' + str(settings['pulse']))
        f.close()
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Current settings have been successfully saved")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.msg.exec_()
    
    def set_acq4_dir(self): # Dialog to set acq4 directory
        ac_dir = QFileDialog.getExistingDirectory(self, 'Set ACQ4 Directory')
        self.acq4_path.setText(ac_dir)
        update_nidaq_values()
    
    def browse(self): # Dialog to set save directory
        cd=QFileDialog.getExistingDirectory(self, 'Set Save Directory')
        self.current_directory.setText(cd)
        update_nidaq_values()
        #os.chdir("..")
    
    def leave (self): # Exit button
        os._exit(1)
	
    def get_dict(self): # Gets the Dictionaries for that Amplifier
        amplifier = settings['amplifier'] = (self.amplifier_box.currentText())
        if amplifier != 'Please Select Your Amplifier':
            cur_amp_path = os.path.normpath(os.path.join(settings['script_dir'], 'Amplifiers', (settings['amplifier']))) 
            r = open(cur_amp_path, 'r')
            lines = r.readlines()
            settings['gaintele'] = lines[1].rstrip()
            settings['fctele'] = lines[3].rstrip()
            settings['modetele'] = lines[5].rstrip()
            settings['commander_scale'] = lines[7].rstrip()
            if settings['commander_scale'] == '':
                settings['commander_scale'] = 1	
            r.close()
        if amplifier == 'Basic':
            self.gain_telegraph.setText(None)
            self.gain_telegraph.setEnabled(False)
            self.fc_telegraph.setText(None)
            self.fc_telegraph.setEnabled(False)
            self.units_telegraph.setText(None)
            self.units_telegraph.setEnabled(False)
            self.fc_spinner.setValue(0)
            self.fc_spinner.setEnabled(False)
            self.gain_spinner.setValue(1.0)
            self.scale_box.setText('1')
            self.volts_radio.click()
        if amplifier == 'MultiClamp700':
            self.gain_telegraph.setText(None)
            self.gain_telegraph.setEnabled(False)
            self.fc_telegraph.setEnabled(False)
            self.units_telegraph.setText(None)
            self.units_telegraph.setEnabled(False)
            self.fc_spinner.setEnabled(True)
        else:
            self.gain_telegraph.setEnabled(True)
            self.fc_telegraph.setEnabled(True)
            self.units_telegraph.setEnabled(True)
            self.fc_spinner.setEnabled(True)


    def delete_amplifier(self): # Deletes Amplifier on button press
        amp_name = self.ui2.edit_amplifier.currentText()
        del_path = os.path.normpath(os.path.join(settings['script_dir'], 'Amplifiers', amp_name))
        os.remove(del_path)
        self.get_amplifiers2()
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("You have deleted %s from the amplifiers list" % (amp_name))
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.msg.exec_()		
		
    def update_gain_fc_units_func(self): # Updates the gain, fc and units from ai channels
        if settings['amplifier'] == 'Please Select Your Amplifier':
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("You have not chosen an amplifier")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            self.msg.exec_()
        else:
            gainz = None 
            if self.gain_telegraph.displayText() != '' :
                chan = self.gain_telegraph.displayText()
                conf = self.config_combo.currentText()
                gainz = nidaq_scope.get_gain(chan, conf, settings['gaintele'], )
                if gainz != 'gainfail':
                    self.gain_spinner.setValue(float(gainz))
            fcz = None
            if self.fc_telegraph.displayText() != '' :
                chan2 = self.fc_telegraph.displayText()
                conf = self.config_combo.currentText()
                fcz = nidaq_scope.get_fc(chan2, conf, settings['fctele'])
                if fcz != 'fcfail':
                   self.fc_spinner.setValue(int('%d' % (fcz)))
            unitz = None
            if self.units_telegraph.displayText() != '' :
                chan3 = self.units_telegraph.displayText()
                conf = self.config_combo.currentText()
                unitz = nidaq_scope.get_mode(chan3, conf, settings['modetele'])
                if unitz == 'A':
                    self.amps_radio.click()
                elif unitz == 'V':
                    self.volts_radio.click()
            errormessage = ''
            if gainz == 'gainfail':
                errormessage = errormessage + 'Gain\n'
            if fcz == 'fcfail':
                errormessage = errormessage + ' Filter\n'
            if unitz == 'modefail':
                errormessage = errormessage + ' Units\n'
            if gainz == 'gainfail' or fcz == 'fcfail' or unitz == 'modefail':
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setText("The following values could not be updated:\n %s \n Check if your amplifier supports telegraphs\n Check if your amplifier telegraph dictionaries are correct\n Check if your telegraph is in the right format eg. Dev1/ai1" % (errormessage))
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.msg.setWindowTitle("Incorrect Telegraphs")
                self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
                self.msg.exec_()
        update_nidaq_values()

    def get_amplifiers(self): # Gets saved amplifiers for combobox1
        self.amplifier_box.clear()
        amp_path = os.path.normpath(os.path.join(settings['script_dir'],'Amplifiers'))
        files = [ f for f in os.listdir(amp_path)]
        self.amplifier_box.addItem('Please Select Your Amplifier')
        self.amplifier_box.addItems(files)
		
    def get_amplifiers2(self): # Gets saved amplifiers for combobox2
        self.ui2.edit_amplifier.clear()
        amp_path = os.path.normpath(os.path.join(settings['script_dir'],'Amplifiers'))
        files = [ f for f in os.listdir(amp_path)]
        self.ui2.edit_amplifier.addItem('Select Amplifier to Edit')
        self.ui2.edit_amplifier.addItems(files)
	
    def create(self): # Creates new amplifier
        new_name = (self.ui2.amplifier_name.displayText())
        path = os.path.normpath(os.path.join(settings['script_dir'],'Amplifiers', new_name))
        gains_dict = (self.ui2.gains_dict.displayText())
        fc_dict = (self.ui2.fc_dict.displayText())	
        modes_dict = (self.ui2.modes_dict.displayText())
        commander_scale = (self.ui2.commander_scale.displayText())
        try:
            open(path, 'r')
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("This amplifier's telegraph settings already exist.\nTry editing the settings instead")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            self.msg.exec_()			
        except:
            f = open(path, 'w+')
            f.write('#Gains\n' + gains_dict + '\n' + '#Fcs\n' + fc_dict + '\n' + '#Modes\n' +  modes_dict +'\n' + '#Commander Scale\n' + commander_scale + '\n')
            f.close()
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("The new amplifier telegraph settings have been saved successfully. ")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            self.msg.exec_()
        finally:
            self.get_amplifiers2()
		
    def save_edit(self): # Overwrites amplifier settings
        new_name = (self.ui2.amplifier_name.displayText())
        path = os.path.normpath(os.path.join(settings['script_dir'],'Amplifiers', new_name))
        gains_dict = (self.ui2.gains_dict.displayText())
        fc_dict = (self.ui2.fc_dict.displayText())	
        modes_dict = (self.ui2.modes_dict.displayText())
        commander_scale = (self.ui2.commander_scale.displayText())
        f = open(path, 'w+')
        f.write('#Gains\n' + gains_dict + '\n' + '#Fcs\n' + fc_dict + '\n' + '#Modes\n' +  modes_dict +'\n' + '#Commander Scale\n' + commander_scale + '\n')
        f.close()
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("The amplifier telegraph settings have been edited successfully. ")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.msg.exec_()		
		
    def closewin(self): # Closes amplifier window
        settings['amplifer'] = None
        self.get_amplifiers()
        self.window2.close()
		
    def close_pulse(self): # Closes pulse window
	    self.window3.close()
	
    def fill_tele(self): # Fills telegraphs
        amp_name = self.ui2.edit_amplifier.currentText()
        if amp_name != 'Select Amplifier to Edit':
            self.ui2.amplifier_name.setText(amp_name)
            cur_amp_path = os.path.normpath(os.path.join(settings['script_dir'], 'Amplifiers', amp_name))
            r = open(cur_amp_path, 'r')
            lines = r.readlines()
            gaintele = lines[1].rstrip()
            fctele = lines[3].rstrip()
            modestele =lines[5].rstrip()
            commander_scale = lines[7].rstrip()		
            self.ui2.gains_dict.setText(gaintele)
            self.ui2.fc_dict.setText(fctele)
            self.ui2.modes_dict.setText(modestele)
            self.ui2.commander_scale.setText(commander_scale)
            r.close()
        if amp_name == 'Basic':
            self.ui2.delete_amp.setEnabled(False)
        else:
            self.ui2.delete_amp.setEnabled(True)

    def update_pulse(self):
        settings['prepulse'] = (self.ui3.down_spinner_1.value())
        settings['pulse_amp'] = (self.ui3.amplitude_spinner.value())
        settings['pulse_length'] = (self.ui3.pulse_length_spinner.value())
        #settings['postpulse'] = (self.ui3.down_spinner_2.value())
        settings['postpulse'] = (self.window_size_spinner.value() * 1e-03) - settings['prepulse'] - settings['pulse_length']
        settings['holding'] = (self.ui3.holding_voltage_spinner.value())
        settings['commander_scale'] = (self.ui3.commander_scale_spinner.value())

    def get_commander_scale(self):
        amplifier = (self.amplifier_box.currentText())
        cur_amp_path = os.path.normpath(os.path.join(settings['script_dir'], 'Amplifiers', amplifier)) 
        r = open(cur_amp_path, 'r')
        lines = r.readlines()
        settings['commander_scale'] = lines[7].rstrip()
        self.ui3.commander_scale_spinner.setValue(float(settings['commander_scale']))
        r.close()
		
	
    def other_window(self): # Opens amplifier window
        self.window2 = QDialog()
        self.ui2 = Amplifier_Dialog()
        self.ui2.setupUi(self.window2)
        self.window2.setWindowFlags(QtCore.Qt.Window |QtCore.Qt.CustomizeWindowHint |QtCore.Qt.WindowTitleHint )
        self.get_amplifiers2()
        self.window2.show()
        self.ui2.close_window.clicked.connect(self.closewin)
        self.ui2.save_dict.clicked.connect(self.create)
        self.ui2.edit_amplifier.activated.connect(self.fill_tele)
        self.ui2.edit_dict.clicked.connect(self.save_edit)
        self.ui2.delete_amp.clicked.connect(self.delete_amplifier)
		
    def pulse_graph(self): # Show pulse graph
        wave = []
        for i in range(0,int(settings['prepulse']*1000)):
            wave.append(settings['holding'])
        for i in range(0,int(settings['pulse_length']*1000)):
            wave.append((settings['holding'])+(settings['pulse_amp']))
        for i in range(0,int(settings['postpulse']*1000)):
            wave.append(settings['holding'])	
        graph= pg.plot(wave)
        graph.setLabel('left', 'Command (mV or pA)' )
        graph.setLabel('bottom', 'Time (ms)',)
		
    def pulse_window(self):
        self.window3 = QDialog()
        self.ui3 = Pulse_Dialog()
        self.ui3.setupUi(self.window3)
        self.window3.setWindowFlags(QtCore.Qt.Window |QtCore.Qt.CustomizeWindowHint |QtCore.Qt.WindowTitleHint )
        self.window3.show()
        self.ui3.down_spinner_1.setValue(np.float64(settings['prepulse']))
        self.ui3.amplitude_spinner.setValue(np.float64(settings['pulse_amp']))		
        self.ui3.pulse_length_spinner.setValue(np.float64(settings['pulse_length']))		
        self.ui3.down_spinner_2.setValue(np.float64(settings['postpulse']))		
        self.ui3.holding_voltage_spinner.setValue(np.float64(settings['holding']))
        self.ui3.commander_scale_spinner.setValue(np.uint32(settings['commander_scale']))		

        self.ui3.down_spinner_1.editingFinished.connect(self.update_pulse)
        self.ui3.amplitude_spinner.editingFinished.connect(self.update_pulse)
        self.ui3.pulse_length_spinner.editingFinished.connect(self.update_pulse)
        self.ui3.down_spinner_2.editingFinished.connect(self.update_pulse)
        self.ui3.holding_voltage_spinner.editingFinished.connect(self.update_pulse)
        self.ui3.commander_scale_spinner.editingFinished.connect(self.update_pulse)
        self.ui3.get_commander_scale_button.clicked.connect(self.get_commander_scale)
        self.ui3.close_window.clicked.connect(self.close_pulse)
        self.ui3.show_wave_button.clicked.connect(self.pulse_graph)
		
			
if __name__ == "__main__":
    app = QApplication.instance() # sets up QApplication if there isnt one already
    if not app:
        app = QApplication(sys.argv)
    window = MyApp()
    window.show() # Shows gui
    update_nidaq_values()
    while (1): #Lets the user do the command as much as they want
        input('Press Enter to start oscilloscope.\n')
        window.update_gain_fc_units_func()       
		#output = scope + str(save) + ", " + str(rate) + ", " + str(win_size) + ", '" + str(ai_channel_format) + "', '" + str(save_dir)+ "', '" + str(config)+ "', " + str(limits_format)+ ", '" + str(unit)+ "', " + str(scale)+ ", " + str(gain)+ ", " + str(notes) + ")"
        if settings['save'] == True and settings['save_dir'] == "":
            nosave()
        else:
            func()
    sys.exit(app.exec_())
