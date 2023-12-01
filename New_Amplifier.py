# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\New_Amplifier.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QLabel, QPushButton, QComboBox

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Amplifier_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(390, 320)
        Dialog.setMaximumSize(QtCore.QSize(390, 320))
        self.amplifier_name = QLineEdit(Dialog)
        self.amplifier_name.setGeometry(QtCore.QRect(20, 30, 361, 20))
        self.amplifier_name.setObjectName(_fromUtf8("amplifier_name"))
        self.gains_dict = QLineEdit(Dialog)
        self.gains_dict.setGeometry(QtCore.QRect(20, 70, 361, 20))
        self.gains_dict.setObjectName(_fromUtf8("gains_dict"))
        self.fc_dict = QLineEdit(Dialog)
        self.fc_dict.setGeometry(QtCore.QRect(20, 110, 361, 20))
        self.fc_dict.setObjectName(_fromUtf8("fc_dict"))
        self.modes_dict = QLineEdit(Dialog)
        self.modes_dict.setGeometry(QtCore.QRect(20, 150, 361, 20))
        self.modes_dict.setObjectName(_fromUtf8("modes_dict"))
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 361, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 361, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 361, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.save_dict = QPushButton(Dialog)
        self.save_dict.setGeometry(QtCore.QRect(220, 270, 71, 31))
        self.save_dict.setObjectName(_fromUtf8("save_dict"))
        self.close_window = QPushButton(Dialog)
        self.close_window.setGeometry(QtCore.QRect(310, 270, 71, 31))
        self.close_window.setObjectName(_fromUtf8("close_window"))
        self.edit_dict = QPushButton(Dialog)
        self.edit_dict.setGeometry(QtCore.QRect(220, 220, 71, 31))
        self.edit_dict.setObjectName(_fromUtf8("edit_dict"))
        self.edit_amplifier = QComboBox(Dialog)
        self.edit_amplifier.setGeometry(QtCore.QRect(20, 250, 181, 31))
        self.edit_amplifier.setObjectName(_fromUtf8("edit_amplifier"))
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 181, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.delete_amp = QPushButton(Dialog)
        self.delete_amp.setGeometry(QtCore.QRect(310, 220, 71, 31))
        self.delete_amp.setObjectName(_fromUtf8("delete_amp"))
        self.commander_scale = QLineEdit(Dialog)
        self.commander_scale.setGeometry(QtCore.QRect(20, 190, 361, 20))
        self.commander_scale.setObjectName(_fromUtf8("commander_scale"))
        self.label_6 = QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 361, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Amplifier Telegraph", None))
        self.amplifier_name.setToolTip(_translate("Dialog", "Amplifier Name", None))
        self.gains_dict.setToolTip(_translate("Dialog", "Enter dictionary in format \n"
"voltage:gain,voltage2:gain2\n"
" eg. 0.5:1.0:1.0:2.0:1.5:5.0", None))
        self.fc_dict.setToolTip(_translate("Dialog", "Enter dictionary in format \n"
"voltage:fc,voltage2:fc2\n"
" eg. 0.5:1000:1.0:2000:1.5:5000", None))
        self.modes_dict.setToolTip(_translate("Dialog", "Enter dictionary in format \n"
"voltage:mode,voltage2:mode2\n"
" eg. 0.5:\'V\':1.0:\'A\':1.5:\'A\'", None))
        self.label.setToolTip(_translate("Dialog", "Amplifier Name", None))
        self.label.setText(_translate("Dialog", "Amplifier Name", None))
        self.label_5.setToolTip(_translate("Dialog", "Enter dictionary in format \n"
"voltage:gain,voltage2:gain2\n"
" eg. 0.5:1.0:1.0:2.0:1.5:5.0", None))
        self.label_5.setText(_translate("Dialog", "Gains Telegraph Dictionary", None))
        self.label_2.setToolTip(_translate("Dialog", "Enter dictionary in format \n"
"voltage:fc,voltage2:fc2\n"
" eg. 0.5:1000:1.0:2000:1.5:5000", None))
        self.label_2.setText(_translate("Dialog", "Filter Cutoff Telegraph Dictionary", None))
        self.label_3.setToolTip(_translate("Dialog", "Enter dictionary in format \n"
"voltage:mode,voltage2:mode2\n"
" eg. 0.5:\'V\':1.0:\'A\':1.5:\'A\'", None))
        self.label_3.setText(_translate("Dialog", "Modes Telegraph Dictionary", None))
        self.save_dict.setToolTip(_translate("Dialog", "Create a new amplifier dictionary with above settings", None))
        self.save_dict.setText(_translate("Dialog", "Create", None))
        self.close_window.setToolTip(_translate("Dialog", "Close the amplifier telegraph editor", None))
        self.close_window.setText(_translate("Dialog", "Close", None))
        self.edit_dict.setToolTip(_translate("Dialog", "Save the edits to the amplifier dictionaries", None))
        self.edit_dict.setText(_translate("Dialog", "Edit", None))
        self.edit_amplifier.setToolTip(_translate("Dialog", "Choose an amplifier to edit", None))
        self.label_4.setToolTip(_translate("Dialog", "Choose an amplifier to edit", None))
        self.label_4.setText(_translate("Dialog", "Edit Amplifier", None))
        self.delete_amp.setToolTip(_translate("Dialog", "Delete currently selected amplifier", None))
        self.delete_amp.setText(_translate("Dialog", "Delete", None))
        self.commander_scale.setToolTip(_translate("Dialog", "Enter dictionary in format \n"
"voltage:mode,voltage2:mode2\n"
" eg. 0.5:\'V\':1.0:\'A\':1.5:\'A\'", None))
        self.label_6.setToolTip(_translate("Dialog", "Enter Commander Input Scale (mv/V)", None))
        self.label_6.setText(_translate("Dialog", "Commander Scale", None))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

