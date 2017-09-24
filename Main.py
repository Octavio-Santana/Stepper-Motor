# -*- coding: utf-8 -*-
"""
@author: Octavio Santana
"""

import sys
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
import stepper_motor_gpio as step

class Main(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.t = 0
        self.i = 0
        self.j = 1
        self.k = 1
        self.cond = step.cond
        self.stop = step.stop

        self.step = QtGui.QSpinBox(self)
        self.radioH = QtGui.QRadioButton('Horario')
        self.radioA = QtGui.QRadioButton('AntiHorario')
        self.btnGo = QtGui.QPushButton('Go')
        self.btnClose = QtGui.QPushButton('Close')

        fbox = QtGui.QFormLayout()
        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()

        fbox.addRow('Numero de passo(s)', self.step)
        hbox.addWidget(self.radioH)
        hbox.addWidget(self.radioA)
        hbox.addStretch()
        fbox.addRow(QtGui.QLabel('Sentido'), hbox)
        fbox.addRow(self.btnGo, self.btnClose)

        # Clicked button #
        self.btnClose.clicked.connect(self.Stop)
        self.btnClose.clicked.connect(self.close)
        self.btnGo.clicked.connect(self.Go)

        self.radioH.setChecked(True)
        self.radioH.toggled.connect(lambda:self.radiostate(self.radioH))

        self.setLayout(fbox)

    def Stop(self):
        self.stop()

    def Go(self):
        passo = int(self.step.text())
        s = self.radiostate(self.radioH)
        self.t, self.j, self.k = self.cond(self.t, self.i, self.j, self.k, s)
        motor = step.Motor_Passo(passo, s, self.t)
        self.i += 1
        self.t = motor.run()
        #print '\n'

    def radiostate(self, radio):
        if radio.isChecked() == True:
            return 'h'
        else:
            return 'a'

root = QtGui.QApplication(sys.argv)
app = Main()
app.show()
sys.exit(root.exec_())
