#!/usr/bin/env python
import sys
import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)
print(sys.path)
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QInputDialog,  QFileDialog
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import pandas as pd
import io
import requests
import os.path

class Window2(QMainWindow):#class for window2 (pop up window)
    def __init__(self):
        super(Window2,self).__init__()
        self.setWindowTitle("check your data")
        self.setGeometry(400, 400, 330, 385)
        self.iniUI()


    def iniUI(self):#
        
        #self.window1 = MyWindow()
       
        

        self.tablewidget = QtWidgets.QTableWidget

        self.label_sample = QtWidgets.QLabel(self)
        self.label_sample.setText('sampel name:')
        self.label_sample.move(20, 70)
        
        
        self.kitlabel = QtWidgets.QLabel(self)
        self.kitlabel.move(20, 10)
        self.kitlabel.setText('kit:')

        self.barlabel = QtWidgets.QLabel(self)
        self.barlabel.move(20, 30)
        self.barlabel.setText('barcoding kit:')
        
        self.barcodinglabel = QtWidgets.QLabel(self)
        self.barcodinglabel.move(20, 50)
        self.barcodinglabel.setText('flowcell:')
        
        self.input0 = QtWidgets.QLabel(self)#kit
        self.input0.move(115, 10)

        self.input00 = QtWidgets.QLabel(self)#barcode
        self.input00.move(115, 30)

        self.input000 = QtWidgets.QLabel(self)#flowcell
        self.input000.move(115, 50)
        
        self.input1 = QtWidgets.QLabel(self)#samples 1-24
        self.input1.move(20, 90)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('1')
        self.label1.move(10, 90)
        
        self.input2 = QtWidgets.QLabel(self)
        self.input2.move(20,110)
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('2')
        self.label2.move(10, 110)
        
        self.input3 = QtWidgets.QLabel(self)
        self.input3.move(20,130)
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText('3')
        self.label3.move(10, 130)
    
        self.input4 = QtWidgets.QLabel(self)
        self.input4.move(20,150)
        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText('4')
        self.label4.move(10, 150)
        
        self.input5 = QtWidgets.QLabel(self)
        self.input5.move(20,170)
        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText('5')
        self.label5.move(10, 170)
        
        self.input6 = QtWidgets.QLabel(self)
        self.input6.move(20,190)
        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText('6')
        self.label6.move(10, 190)
        
        self.input7 = QtWidgets.QLabel(self)
        self.input7.move(20,210)
        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText('7')
        self.label7.move(10, 210)
        
        self.input8 = QtWidgets.QLabel(self)
        self.input8.move(20,230)
        self.label8 = QtWidgets.QLabel(self)
        self.label8.setText('8')
        self.label8.move(10, 230)
        
        self.input9 = QtWidgets.QLabel(self)
        self.input9.move(20,250)
        self.label9 = QtWidgets.QLabel(self)
        self.label9.setText('9')
        self.label9.move(10, 250)
        
        self.input10 = QtWidgets.QLabel(self)
        self.input10.move(20,270)
        self.label10 = QtWidgets.QLabel(self)
        self.label10.setText('10')
        self.label10.move(6, 270)
        
        self.input11 = QtWidgets.QLabel(self)
        self.input11.move(20,290)
        self.label11 = QtWidgets.QLabel(self)
        self.label11.setText('11')
        self.label11.move(6, 290)
        
        self.input12 = QtWidgets.QLabel(self)
        self.input12.move(20,310)
        self.label12 = QtWidgets.QLabel(self)
        self.label12.setText('12')
        self.label12.move(6, 310)
        
        self.input13 = QtWidgets.QLabel(self)
        self.input13.move(200,90)
        self.label13 = QtWidgets.QLabel(self)
        self.label13.setText('13')
        self.label13.move(184, 90)
       
        self.input14 = QtWidgets.QLabel(self)
        self.input14.move(200,110)
        self.label14 = QtWidgets.QLabel(self)
        self.label14.setText('14')
        self.label14.move(184, 110)
        
        self.input15 = QtWidgets.QLabel(self)
        self.input15.move(200,130)
        self.label15 = QtWidgets.QLabel(self)
        self.label15.setText('16')
        self.label15.move(184, 130)
        
        self.input16 = QtWidgets.QLabel(self)
        self.input16.move(200,150)
        self.label16 = QtWidgets.QLabel(self)
        self.label16.setText('16')
        self.label16.move(184, 150)
        
        self.input17 = QtWidgets.QLabel(self)
        self.input17.move(200,170)
        self.label17 = QtWidgets.QLabel(self)
        self.label17.setText('17')
        self.label17.move(184, 170)
        
        self.input18 = QtWidgets.QLabel(self)
        self.input18.move(200,190)
        self.label18 = QtWidgets.QLabel(self)
        self.label18.setText('18')
        self.label18.move(184, 190)
        
        self.input19 = QtWidgets.QLabel(self)
        self.input19.move(200,210)
        self.label19 = QtWidgets.QLabel(self)
        self.label19.setText('19')
        self.label19.move(184, 210)
        
        self.input20 = QtWidgets.QLabel(self)
        self.input20.move(200,230)
        self.label20 = QtWidgets.QLabel(self)
        self.label20.setText('20')
        self.label20.move(184, 230)
        
        self.input21 = QtWidgets.QLabel(self)
        self.input21.move(200,250)
        self.label21 = QtWidgets.QLabel(self)
        self.label21.setText('21')
        self.label21.move(184, 250)
        
        self.input22 = QtWidgets.QLabel(self)
        self.input22.move(200,270)
        self.label22 = QtWidgets.QLabel(self)
        self.label22.setText('22')
        self.label22.move(184, 270)
        
        self.input23 = QtWidgets.QLabel(self)
        self.input23.move(200,290)
        self.label23 = QtWidgets.QLabel(self)
        self.label23.setText('23')
        self.label23.move(184, 290)
        
        self.input24 = QtWidgets.QLabel(self)
        self.input24.move(200,310)
        self.label24 = QtWidgets.QLabel(self)
        self.label24.setText('24')
        self.label24.move(184, 310)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText('ok!')
        self.button.move(230, 355) 
        #self.button.clicked.connect(self.upload_activated)
        self.button.clicked.connect(self.close)#close window2


    def hide2(self):#hide all labels from 2 to 12 
        self.label2.setHidden(True)
        self.label3.setHidden(True)
        self.label4.setHidden(True)
        self.label5.setHidden(True)
        self.label6.setHidden(True)
        self.label7.setHidden(True)
        self.label8.setHidden(True)
        self.label9.setHidden(True)
        self.label10.setHidden(True)
        self.label11.setHidden(True)
        self.label12.setHidden(True)  


    def unhide2(self):#unhide all labels from 2 to 12
        self.label2.setHidden(False)
        self.label3.setHidden(False)
        self.label4.setHidden(False)
        self.label5.setHidden(False)
        self.label6.setHidden(False)
        self.label7.setHidden(False)
        self.label8.setHidden(False)
        self.label9.setHidden(False)
        self.label10.setHidden(False)
        self.label11.setHidden(False)
        self.label12.setHidden(False)


    def unhide(self):#show all labels from 13 to 24
         self.label13.setHidden(False)
         self.label14.setHidden(False)
         self.label15.setHidden(False)
         self.label16.setHidden(False)
         self.label17.setHidden(False)
         self.label18.setHidden(False)
         self.label19.setHidden(False)
         self.label20.setHidden(False)
         self.label21.setHidden(False)
         self.label22.setHidden(False)
         self.label23.setHidden(False)
         self.label24.setHidden(False)


    def hide(self):#hide all labels from 13 to 24
        self.label13.setHidden(True)
        self.label14.setHidden(True)
        self.label15.setHidden(True)
        self.label16.setHidden(True)
        self.label17.setHidden(True)
        self.label18.setHidden(True)
        self.label19.setHidden(True)
        self.label20.setHidden(True)
        self.label21.setHidden(True)
        self.label22.setHidden(True)
        self.label23.setHidden(True)
        self.label24.setHidden(True)

 
    def displayInfo(self):#shows window2
        self.show( )


    #def upload_activated(self):
     #   self.window1.button_upload.setEnabled(True)
         

class MyWindow(QMainWindow):#create a window through the initUI() method, and call it in the initialization method init()
    
    def __init__(self):
        super(MyWindow, self).__init__()
        
        #self.secondwindow = Window2()
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Tool summary')
        self.iniUI()#function call

    

    def iniUI(self):

    # 'self' is the first parameter of the methods of a class that refers to the instance of the same

        self.window2 = Window2()#for initiating window2
        

        self.label_kit = QtWidgets.QLabel(self)#creating label
        self.label_kit.setText('choose barcode')
        self.label_kit.move(43, 190)

        self.combobox_kit = QtWidgets.QComboBox(self)
        kits = ['no barcode','EXP-PBC096','EXP-PBC001','EXP-NBD114','EXP-NBD104','EXP-NBD196']
        self.combobox_kit.addItems(kits)
        self.combobox_kit.move(40,215)#position in window (x,y)
        self.combobox_kit.currentTextChanged.connect(self.combchanged2)#connect combobox to function
        
        
        self.qlabel = QtWidgets.QLabel(self) #labels without any further function
        self.qlabel.setText('')
        self.qlabel.setHidden(True)

        self.qlabel2 = QtWidgets.QLabel(self)
        self.qlabel2.setText('')
        self.qlabel2.setHidden(True)

        self.qlabel3 = QtWidgets.QLabel(self)
        self.qlabel3.setText('')
        self.qlabel3.setHidden(True)
        
         

        

        self.label_barcode = QtWidgets.QLabel(self)
        self.label_barcode.setText('more then one sample?')
        self.label_barcode.move(45, 260)
        self.label_barcode.adjustSize()

        self.combobox_barcode = QtWidgets.QComboBox(self)
        kits2 = ['choose flowcell','FLO-MIN106']
        self.combobox_barcode.addItems(kits2)
        self.combobox_barcode.move(40, 350)
        self.combobox_barcode.adjustSize()
        self.combobox_barcode.view().setRowHidden(0, True)
        self.combobox_barcode.activated.connect(self.showComboMessage3)
        
        self.combobox_barcode.activated[str].connect(self.onChanged3)#function to hide first index of list
    
        
        
        self.radiobutton_no = QtWidgets.QRadioButton(self)# round button (gruoped with radiobutton_yes)- only one can be selected
        self.radiobutton_no.toggled.connect(self.radioclicked_no)
        self.radiobutton_no.move(45, 270)
        self.label_radiobutton_no = QtWidgets.QLabel(self)
        self.label_radiobutton_no.setText('no')
        self.label_radiobutton_no.move(65, 270)
       

        self.label_textedit = QtWidgets.QLabel(self)
        self.label_textedit.setText('add additional informations')
        self.label_textedit.move(292, 410)
        self.label_textedit.adjustSize()
        self.textedit = QtWidgets.QTextEdit(self)#little edit field to add additional info
        self.textedit.setGeometry(290, 430, 200, 150)
        



        self.radiobutton_yes = QtWidgets.QRadioButton(self)
        self.radiobutton_yes.toggled.connect(self.radioclicked_yes)
        self.radiobutton_yes.move(100, 270)
        self.label_radiobutton_yes = QtWidgets.QLabel(self)
        self.label_radiobutton_yes.setText('yes')
        self.label_radiobutton_yes.move(120, 270)
        
        
        self.label_barcode_yes_no = QtWidgets.QLabel(self)
        self.label_barcode_yes_no.setHidden(True)

    


        self.label1 = QtWidgets.QLabel(self)# labels for lineedits for the samples
        self.label1.setText('1')
        self.label1.move(275, 20)
        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(290,20)
        self.lineedit1.setFixedWidth(120)


        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('2')
        self.label2.move(275, 50)
        self.label2.setHidden(True)
        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.move(290,50)
        self.lineedit2.setHidden(True)
        self.lineedit2.setFixedWidth(120)

        

        self.label3 = QtWidgets.QLabel(self) 
        self.label3.setText('3')
        self.label3.move(275, 80)
        self.label3.setHidden(True)
        self.lineedit3 = QtWidgets.QLineEdit(self)
        self.lineedit3.move(290,80)
        self.lineedit3.setHidden(True)
        self.lineedit3.setFixedWidth(120)


        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText('4')
        self.label4.move(275, 110)
        self.label4.setHidden(True)
        self.lineedit4 = QtWidgets.QLineEdit(self)
        self.lineedit4.move(290,110)
        self.lineedit4.setHidden(True)
        self.lineedit4.setFixedWidth(120)


        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText('5')
        self.label5.move(275, 140)
        self.label5.setHidden(True)
        self.lineedit5 = QtWidgets.QLineEdit(self)
        self.lineedit5.move(290,140)
        self.lineedit5.setHidden(True)
        self.lineedit5.setFixedWidth(120)


        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText('6')
        self.label6.move(275, 170)
        self.label6.setHidden(True)
        self.lineedit6 = QtWidgets.QLineEdit(self)
        self.lineedit6.move(290,170)
        self.lineedit6.setHidden(True)
        self.lineedit6.setFixedWidth(120)


        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText('7')
        self.label7.move(275, 200)
        self.label7.setHidden(True)
        self.lineedit7 = QtWidgets.QLineEdit(self)
        self.lineedit7.move(290,200)
        self.lineedit7.setHidden(True)
        self.lineedit7.setFixedWidth(120)

        self.label8 = QtWidgets.QLabel(self)
        self.label8.setText('8')
        self.label8.move(275, 230)
        self.label8.setHidden(True)
        self.lineedit8 = QtWidgets.QLineEdit(self)
        self.lineedit8.move(290,230)
        self.lineedit8.setHidden(True)
        self.lineedit8.setFixedWidth(120)

        self.label9 = QtWidgets.QLabel(self)
        self.label9.setText('9')
        self.label9.move(275, 260)
        self.label9.setHidden(True)
        self.lineedit9 = QtWidgets.QLineEdit(self)
        self.lineedit9.move(290,260)
        self.lineedit9.setHidden(True)
        self.lineedit9.setFixedWidth(120)

        self.label10 = QtWidgets.QLabel(self)
        self.label10.setText('10')
        self.label10.move(275, 290)
        self.label10.setHidden(True)
        self.lineedit10 = QtWidgets.QLineEdit(self)
        self.lineedit10.move(290,290)
        self.lineedit10.setHidden(True)
        self.lineedit10.setFixedWidth(120)

        self.label11 = QtWidgets.QLabel(self)
        self.label11.setText('11')
        self.label11.move(275, 320)
        self.label11.setHidden(True)
        self.lineedit11 = QtWidgets.QLineEdit(self)
        self.lineedit11.move(290,320)
        self.lineedit11.setHidden(True)
        self.lineedit11.setFixedWidth(120)

        self.label12 = QtWidgets.QLabel(self)
        self.label12.setText('12')
        self.label12.move(275, 350)
        self.label12.setHidden(True)
        self.lineedit12 = QtWidgets.QLineEdit(self)
        self.lineedit12.move(290,350)
        self.lineedit12.setHidden(True)
        self.lineedit12.setFixedWidth(120)

        self.label13 = QtWidgets.QLabel(self)
        self.label13.setText('13')
        self.label13.move(415, 20)
        self.label13.setHidden(True)
        self.lineedit13 = QtWidgets.QLineEdit(self)
        self.lineedit13.move(430,20)
        self.lineedit13.setHidden(True)
        self.lineedit13.setFixedWidth(120)

        self.label14 = QtWidgets.QLabel(self)
        self.label14.setText('14')
        self.label14.move(415, 50)
        self.label14.setHidden(True)
        self.lineedit14 = QtWidgets.QLineEdit(self)
        self.lineedit14.move(430,50)
        self.lineedit14.setHidden(True)
        self.lineedit14.setFixedWidth(120)

        self.label15 = QtWidgets.QLabel(self)
        self.label15.setText('15')
        self.label15.move(415, 80)
        self.label15.setHidden(True)
        self.lineedit15 = QtWidgets.QLineEdit(self)
        self.lineedit15.move(430, 80)
        self.lineedit15.setHidden(True)
        self.lineedit15.setFixedWidth(120)
        
        self.label16 = QtWidgets.QLabel(self)
        self.label16.setText('16')
        self.label16.move(415, 110)
        self.label16.setHidden(True)
        self.lineedit16 = QtWidgets.QLineEdit(self)
        self.lineedit16.move(430, 110)
        self.lineedit16.setHidden(True)
        self.lineedit16.setFixedWidth(120)
        
        self.label17 = QtWidgets.QLabel(self)
        self.label17.setText('17')
        self.label17.move(415, 140)
        self.label17.setHidden(True)
        self.lineedit17 = QtWidgets.QLineEdit(self)
        self.lineedit17.move(430, 140)
        self.lineedit17.setHidden(True)
        self.lineedit17.setFixedWidth(120)
        
        self.label18 = QtWidgets.QLabel(self)
        self.label18.setText('18')
        self.label18.move(415, 170)
        self.label18.setHidden(True)
        self.lineedit18 = QtWidgets.QLineEdit(self)
        self.lineedit18.move(430, 170)
        self.lineedit18.setHidden(True)
        self.lineedit18.setFixedWidth(120)
        
        self.label19 = QtWidgets.QLabel(self)
        self.label19.setText('19')
        self.label19.move(415, 200)
        self.label19.setHidden(True)
        self.lineedit19 = QtWidgets.QLineEdit(self)
        self.lineedit19.move(430, 200)
        self.lineedit19.setHidden(True)
        self.lineedit19.setFixedWidth(120)
        
        self.label20 = QtWidgets.QLabel(self)
        self.label20.setText('20')
        self.label20.move(415, 230)
        self.label20.setHidden(True)
        self.lineedit20 = QtWidgets.QLineEdit(self)
        self.lineedit20.move(430, 230)
        self.lineedit20.setHidden(True)
        self.lineedit20.setFixedWidth(120)
        
        self.label21 = QtWidgets.QLabel(self)
        self.label21.setText('21')
        self.label21.move(415, 260)
        self.label21.setHidden(True)
        self.lineedit21 = QtWidgets.QLineEdit(self)
        self.lineedit21.move(430, 260)
        self.lineedit21.setHidden(True)
        self.lineedit21.setFixedWidth(120)
        
        self.label22 = QtWidgets.QLabel(self)
        self.label22.setText('22')
        self.label22.move(415, 290)
        self.label22.setHidden(True)
        self.lineedit22 = QtWidgets.QLineEdit(self)
        self.lineedit22.move(430, 290)
        self.lineedit22.setHidden(True)
        self.lineedit22.setFixedWidth(120)
        
        self.label23 = QtWidgets.QLabel(self)
        self.label23.setText('23')
        self.label23.move(415, 320)
        self.label23.setHidden(True)
        self.lineedit23 = QtWidgets.QLineEdit(self)
        self.lineedit23.move(430, 320)
        self.lineedit23.setHidden(True)
        self.lineedit23.setFixedWidth(120)
        
        self.label24 = QtWidgets.QLabel(self)
        self.label24.setText('24')
        self.label24.move(415, 350)
        self.label24.setHidden(True)
        self.lineedit24 = QtWidgets.QLineEdit(self)
        self.lineedit24.move(430, 350)
        self.lineedit24.setHidden(True)
        self.lineedit24.setFixedWidth(120)

        

        self.button_checkdata = QtWidgets.QPushButton(self)#button to insepct data
        self.button_checkdata.setText('check data')
        self.button_checkdata.move(40, 510)
        #self.button_checkdata.clicked.connect(self.clicked)
        #self.button_checkdata.clicked.connect(self.window2)
        #self.button_checkdata.clicked.connect(self.uplaod)
        #self.button_checkdata.clicked.connect(self.passinginfo)
        self.button_checkdata.clicked.connect(self.passinInformation)#function to open another window


        '''self.combobox_dna = QtWidgets.QComboBox(self)
        dna = ['SQK-LSK109-XL','SQK-LSK110','SQK-LSK109','SQK-16S024','SQK-LRK001',
        'SQK-RBK004','SQK-PBK004','SQK-RAB204','SQK-RPB004','SQK-PSK004','SQK-RAD004']
        self.combobox_dna.addItems(dna)
        self.combobox_dna.move(160,10)

        self.combobox_rna = QtWidgets.QComboBox(self)
        rna = ['SQK-PCB109','SQK-RNA002','SQK-PCS109','SQK-DCS109']
        self.combobox_rna.addItems(rna)
        self.combobox_rna.move(160, 30)

        self.combobox_pcr = QtWidgets.QComboBox(self)
        pcr =['SQK-16S024','SQK-PCB109','SQK-CS9109','SQK-PCS109','SQK-PBK004',
        'SQK-RPB004','SQK-PSK004','SQK-RAB204']
        self.combobox_pcr.addItems(pcr)
        self.combobox_pcr.move(160, 50)

        self.combobox_pcr_free = QtWidgets.QComboBox(self)
        pcr_free = ['SQK-LSK109','SQK-LSK109-XL','SQK-CS9109','SQK-LSK110','SQK-RNA002',
        'SQK-LRK001','SQK-DCS109','SQK-RBK004','SQK-RAD004']
        self.combobox_pcr_free.addItems(pcr_free)
        self.combobox_pcr_free.move(160, 70)

        self.combobox_multi_no = QtWidgets.QComboBox(self)
        multiplexing_no = ['SQK-PCB109','SQK-LSK109-XL','SQK-CS9109','SQK-LSK110','SQK-RNA002','SQK-LRK001',
        'SQK-PCS109','SQK-DCS109','SQK-PSK004','SQK-RAD004']
        self.combobox_multi_no.addItems(multiplexing_no)
        self.combobox_multi_no.move(160, 90)

        self.combobox_multi_yes = QtWidgets.QComboBox(self)
        mutiplexing_yes = ['SQK-LSK109','SQK-LSK109-XL','SQK-16S024','SQK-LSK110',
        'SQK-CS9109','SQK-PCB109','SQK-PCS109','SQK-DCS109','SQK-PBK004','SQK-RBK004',
        'SQK-RAB204','SQK-RPB004']
        self.combobox_multi_yes.addItems(mutiplexing_yes)
        self.combobox_multi_yes.move(160, 110)'''


        self.button_upload = QtWidgets.QPushButton(self)
        self.button_upload.setText('upload')
        self.button_upload.move(40, 560)
        #self.button_upload.setEnabled(False)
        self.button_upload.clicked.connect(self.upload)
    
        self.checkbox = QtWidgets.QCheckBox("24-sample names",self)
        self.checkbox.adjustSize()
        self.checkbox.stateChanged.connect(self.clickbox)
        self.checkbox.move(100, 295)
        self.checkbox.setDisabled(True)

        self.checkbox_95 = QtWidgets.QCheckBox("96-sample names",self)
        self.checkbox_95.adjustSize()
        self.checkbox_95.stateChanged.connect(self.clickbox2)
        self.checkbox_95.move(100, 320)
        self.checkbox_95.setDisabled(True)
        


        
        self.label_dna = QtWidgets.QLabel(self)
        self.label_dna.setText('DNA')
        self.label_dna.move(40,20)

        self.samplytype_label = QtWidgets.QLabel(self)
        self.samplytype_label.setText('sample types')
        self.samplytype_label.move(33,3)

        
        self.label_rna = QtWidgets.QLabel(self)
        self.label_rna.setText('RNA')
        self.label_rna.move(100,20)

        
        self.label_pcr = QtWidgets.QLabel(self)
        self.label_pcr.setText('PCR')
        self.label_pcr.move(40,50)

        self.pcr_label = QtWidgets.QLabel(self)
        self.pcr_label.setText('PCR')
        self.pcr_label.move(55,36)

        
        self.label_pcr_free = QtWidgets.QLabel(self)
        self.label_pcr_free.setText('PCR-FREE')
        self.label_pcr_free.move(100,50)

        
        self.label_yes = QtWidgets.QLabel(self)
        self.label_yes.setText('yes')
        self.label_yes.move(40,88)
            
        self.label_multiplexing = QtWidgets.QLabel(self)
        self.label_multiplexing.setText('Multiplexing?')
        self.label_multiplexing.move(33,70)

       
        self.label_no = QtWidgets.QLabel(self)
        self.label_no.setText('no')
        self.label_no.move(100,88)

        
        self.dna_checkbox = QtWidgets.QCheckBox(self)
        self.dna_checkbox.move(20,20)
        self.dna_checkbox.stateChanged.connect(self.clickbox_dna)

        self.rna_checkbox = QtWidgets.QCheckBox(self)
        self.rna_checkbox.move(80, 20)
        self.rna_checkbox.stateChanged.connect(self.clickbox_rna)

        self.pcr_checkbox = QtWidgets.QCheckBox(self)
        self.pcr_checkbox.move(20, 50)
        self.pcr_checkbox.stateChanged.connect(self.clickbox_pcr)

        self.pcr_free_checkbox = QtWidgets.QCheckBox(self)
        self.pcr_free_checkbox.move(80, 50)
        self.pcr_free_checkbox.stateChanged.connect(self.clickbox_pcr_free)

        self.yes_checkbox = QtWidgets.QCheckBox(self)
        self.yes_checkbox.move(20, 88)
        self.yes_checkbox.stateChanged.connect(self.clickbox_yes)

        self.no_checkbox = QtWidgets.QCheckBox(self)
        self.no_checkbox.move(80, 88)
        self.no_checkbox.stateChanged.connect(self.clickbox_no)
        
        

        self.button_anwenden = QtWidgets.QPushButton(self)
        self.button_anwenden.setText('use filter')
        self.button_anwenden.move(40, 120)
        self.button_anwenden.clicked.connect(self.anwenden)

        

        nb_row = 96
        nb_col = 1

        self.tablewidget = QtWidgets.QTableWidget(self)#table for 96 samples
        
        self.tablewidget.setRowCount(nb_row)
        self.tablewidget.setColumnCount(nb_col)
        self.tablewidget.setGeometry(QtCore.QRect(570,20,140,560))
        self.tablewidget.setHorizontalHeaderLabels(["samples"])
        self.tablewidget.setHidden(True)
        

        

        self.list_kits = QtWidgets.QComboBox(self)#all current sequencing kits
        kitliste = ['Select Kit','SQK-PCB109','SQK-RNA002','SQK-PCS109','SQK-DCS109','SQK-CS9109','SQK-LSK109','SQK-LSK109-XL','SQK-16S024','SQK-LSK110',
        'SQK-LRK001','SQK-RBK004','SQK-PBK004','SQK-RAB204','SQK-RPB004','SQK-PSK004','SQK-RAD004']
        self.list_kits.addItems(kitliste)
        self.list_kits.move(40,160)
        self.list_kits.currentTextChanged.connect(self.combchanged)
        
        self.labelupload = QtWidgets.QLabel(self)
        self.labelupload.setText('')
        self.labelupload.setHidden(True)


    def upload(self, state):#function to upload files and create run_info.txt
        dialog = QFileDialog()
        direc = dialog.getExistingDirectory(self, 'Select an  directory')
        
        save_path = direc

        name_of_file = 'run_info' 

        completeName = os.path.join(save_path, name_of_file + ".txt")    
           

        demo = open(completeName, "w")

        kit = self.list_kits.currentText()
        barcodekit = self.combobox_kit.currentText()
        flowcell = self.combobox_barcode.currentText()

        demo.write('Kit#')
        demo.write(kit)
        demo.write('\n')

        demo.write('Barcodekit#')
        demo.write(barcodekit)
        demo.write('\n')

        demo.write('Flowcell#')
        demo.write(flowcell)
        demo.write('\n')
        
        
        
        label_yes_no = self.labelupload.text()
        
        if label_yes_no == 'no':
            lineedit01 = self.lineedit1.text()
            demo.write('NB01#')
            demo.write(lineedit01)
            
        
        
        if label_yes_no == 'yes':
            checkbox_24 = self.checkbox.checkState()
            checkbox_95 = self.checkbox_95.checkState()
            
            if checkbox_24 == 2:
                lineedit13 = self.lineedit13.text()
                lineedit14 = self.lineedit14.text()
                lineedit15 = self.lineedit15.text()
                lineedit16 = self.lineedit16.text()
                lineedit17 = self.lineedit17.text()
                lineedit18 = self.lineedit18.text()
                lineedit19 = self.lineedit19.text()
                lineedit20 = self.lineedit20.text()
                lineedit21 = self.lineedit21.text()
                lineedit22 = self.lineedit22.text()
                lineedit23 = self.lineedit23.text()
                lineedit24 = self.lineedit24.text()

                liste = [lineedit13,lineedit14,lineedit15,lineedit16,lineedit17,lineedit18,lineedit19,lineedit20,
                lineedit21,lineedit22,lineedit23,lineedit24]

                a = 13
                for i in range(0,12):
                    demo.write('NB0')
                    demo.write(str(a))
                    demo.write('#')
                    demo.write(liste[i])
                    demo.write('\n')
                    a = a + 1       
            if checkbox_24 == 0 and checkbox_95 == 0:
                
                lineedit01 = self.lineedit1.text()
                lineedit02 = self.lineedit2.text()
                lineedit03 = self.lineedit3.text()
                lineedit04 = self.lineedit4.text()
                lineedit05 = self.lineedit5.text()
                lineedit06 = self.lineedit6.text()
                lineedit07 = self.lineedit7.text()
                lineedit08 = self.lineedit8.text()
                lineedit09 = self.lineedit9.text()
                lineedit10 = self.lineedit10.text()
                lineedit11 = self.lineedit11.text()
                lineedit12 = self.lineedit12.text()
                liste = [lineedit01,lineedit02,lineedit03,lineedit04,lineedit05,lineedit06,lineedit07,lineedit08,
                lineedit09,lineedit10,lineedit11,lineedit12]
                a = 1
                for i in range(0,12):
                    if a<10:
                        demo.write('NB0')
                        demo.write(str(a))
                        demo.write('#')
                        demo.write(liste[i])
                        demo.write('\n')
                        a = a + 1
                    else:
                        demo.write('NB')
                        demo.write(str(a))
                        demo.write('#')
                        demo.write(liste[i])
                        demo.write('\n')
                        a = a + 1
            
            if checkbox_95 == 2: 
                ku = 0
                ka = 0
                kl = 0
                counter = 1
                
                rows  =  self.tablewidget.rowCount()
                list_96 = []
                for i in range(rows):
                    table = self.tablewidget.item(i, 0)
                    if table:
                        if table.text():
                            ku = '#'
                            ke = str(counter)
                            ka = table.text()
                            kl =  ka + ku + ke
                            list_96.append(ka)
                            counter = counter + 1
                        else:
                            counter = counter + 1
                            list_96.append('')
                    else:
                        counter = counter + 1
                        list_96.append('')
                a = 1
                for i in range(rows):
                    if a<10:
                        demo.write('NB0')
                        demo.write(str(a))
                        demo.write('#')
                        demo.write(list_96[i])
                        demo.write('\n')
                        a = a + 1
                    else:
                        demo.write('NB')
                        demo.write(str(a))
                        demo.write('#')
                        demo.write(list_96[i])
                        demo.write('\n')
                        a = a + 1
                    
                

        
        
        
        #tablewidget = self.tablewidget.currentItem().row(1).column(0)
        #tablewidget = self.tablewidget.itemAt(0,0).text()
        #tablewidget = self.tablewidget.item(self.row,col).text()
        #print(tablewidget)


        #/n zeilenumbruch
        demo.close()
 

    def combchanged2(self, value):#function for barcoding kits to sleect number of samples automatic
        n = value
        if n == 'no barcode':
            self.radiobutton_no.setChecked(True)
        if n == 'EXP-NBD196' or n == 'EXP-PBC096':
            self.radiobutton_yes.setChecked(True)
            self.checkbox_95.setChecked(True)
            self.tablewidget.setHidden(False)
            self.label1.setHidden(True)
            self.label2.setHidden(True)
            self.label3.setHidden(True)
            self.label4.setHidden(True)
            self.label5.setHidden(True)
            self.label6.setHidden(True)
            self.label7.setHidden(True)
            self.label8.setHidden(True)
            self.label9.setHidden(True)
            self.label10.setHidden(True)
            self.label11.setHidden(True)
            self.label12.setHidden(True)
            self.lineedit1.setHidden(True)
            self.lineedit2.setHidden(True)
            self.lineedit3.setHidden(True)
            self.lineedit4.setHidden(True)
            self.lineedit5.setHidden(True)
            self.lineedit6.setHidden(True)
            self.lineedit7.setHidden(True)
            self.lineedit8.setHidden(True)
            self.lineedit9.setHidden(True)
            self.lineedit10.setHidden(True)
            self.lineedit11.setHidden(True)
            self.lineedit12.setHidden(True)
        if n == 'EXP-PBC001' or n == 'EXP-NBD104' or n == 'SQK-RPB004':
            self.radiobutton_yes.setChecked(True)
            self.checkbox_95.setChecked(False)
            self.checkbox.setChecked(False)
            self.label1.setHidden(False)
            self.label2.setHidden(False)
            self.label3.setHidden(False)
            self.label4.setHidden(False)
            self.label5.setHidden(False)
            self.label6.setHidden(False)
            self.label7.setHidden(False)
            self.label8.setHidden(False)
            self.label9.setHidden(False)
            self.label10.setHidden(False)
            self.label11.setHidden(False)
            self.label12.setHidden(False)
            self.lineedit1.setHidden(False)
            self.lineedit2.setHidden(False)
            self.lineedit3.setHidden(False)
            self.lineedit4.setHidden(False)
            self.lineedit5.setHidden(False)
            self.lineedit6.setHidden(False)
            self.lineedit7.setHidden(False)
            self.lineedit8.setHidden(False)
            self.lineedit9.setHidden(False)
            self.lineedit10.setHidden(False)
            self.lineedit11.setHidden(False)
            self.lineedit12.setHidden(False)
        if n == 'EXP-NBD114':    
            self.radiobutton_yes.setChecked(True)
            self.checkbox.setChecked(True)
            self.checkbox_95.setChecked(False)
            self.label1.setHidden(True)
            self.label2.setHidden(True)
            self.label3.setHidden(True)
            self.label4.setHidden(True)
            self.label5.setHidden(True)
            self.label6.setHidden(True)
            self.label7.setHidden(True)
            self.label8.setHidden(True)
            self.label9.setHidden(True)
            self.label10.setHidden(True)
            self.label11.setHidden(True)
            self.label12.setHidden(True)
            self.lineedit1.setHidden(True)
            self.lineedit2.setHidden(True)
            self.lineedit3.setHidden(True)
            self.lineedit4.setHidden(True)
            self.lineedit5.setHidden(True)
            self.lineedit6.setHidden(True)
            self.lineedit7.setHidden(True)
            self.lineedit8.setHidden(True)
            self.lineedit9.setHidden(True)
            self.lineedit10.setHidden(True)
            self.lineedit11.setHidden(True)
            self.lineedit12.setHidden(True)

    
    def combchanged(self, value):#function to choose automatic which barcode could be used after selcting a seuqencing kit
        n = value

        kits = ['no barcode','EXP-PBC096','EXP-PBC001','EXP-NBD114','EXP-NBD104','EXP-NBD196']        
        self.combobox_kit.clear()
        self.combobox_kit.addItems(kits)


        url="https://raw.githubusercontent.com/t3ddezz/kitslist/main/Barcodelist_real1.tsv"
        re=requests.get(url).content
        barcoding = pd.read_csv(io.StringIO(re.decode('utf-8')), sep='\t', index_col=False, header=None)
        barcoding = barcoding.fillna(0)
        
        d = len(barcoding.columns)
        a = 0
        barcoding_list = ['no barcode','EXP-PBC001','EXP-PBC096','EXP-NBD114','EXP-NBD104','EXP-NBD196']
        while True:
            if  barcoding.loc[0,a] == n:
                barcoding_list.clear()
                barcoding_list = barcoding[a].tolist()
                del barcoding_list[0]
                barlist = ['no barcode']
                k = len(barcoding)
                k = k - 1
            
                for i in range(0,k):
                    if barcoding_list[i] != 0:
                        c = barcoding_list[i]
                        barlist.append(c)

                
                self.combobox_kit.clear()
                self.combobox_kit.addItems(barlist)
                break
    

            else: 
                a = a + 1

            if a == d:
                a = 0
                self.combobox_kit.clear()
                self.combobox_kit.addItems(barcoding_list)
                break
        
        
    def clickbox_dna(self, state):#functions for the filter
        if state == QtCore.Qt.Checked:
            self.rna_checkbox.setChecked(False)
    
    def clickbox_rna(self, state):
        if state == QtCore.Qt.Checked:
            self.dna_checkbox.setChecked(False)

    def clickbox_pcr(self, state):
        if state == QtCore.Qt.Checked:
            self.pcr_free_checkbox.setChecked(False)

    def clickbox_pcr_free(self, state):
        if state == QtCore.Qt.Checked:
            self.pcr_checkbox.setChecked(False)  

    def clickbox_no(self, state):
        if state == QtCore.Qt.Checked:
            self.yes_checkbox.setChecked(False)

    def clickbox_yes(self, state):
        if state == QtCore.Qt.Checked:
            self.no_checkbox.setChecked(False)   

    def onChanged3(self, text):
        self.qlabel3.setText(text)

   

   
   
    def showComboMessage2(self, index=-1, enable=False):#function to hide first index in a list
        if index:
            self.combobox_bar.model().item(0).setEnabled(enable)
    
    
    def showComboMessage3(self, index=-1, enable=False):
        if index:
            self.combobox_barcode.model().item(0).setEnabled(enable)

   
    def radioclicked_no(self):# 

        self.window2.hide()
        self.window2.hide2()
        self.labelupload.setText('no')
        #self.combobox_bar.setDisabled(True)
        self.label_barcode_yes_no.setText('no')
        self.checkbox.setChecked(False)
        self.checkbox.setDisabled(True)
        self.checkbox_95.setChecked(False)
        self.checkbox_95.setDisabled(True)
        self.tablewidget.setHidden(True)
        #self.textedit.setDisabled(False)
        #self.textedit.setHidden(False)
        self.label1.setHidden(False)
        self.label2.setHidden(True)
        self.label3.setHidden(True)
        self.label4.setHidden(True)
        self.label5.setHidden(True)
        self.label6.setHidden(True)
        self.label7.setHidden(True)
        self.label8.setHidden(True)
        self.label9.setHidden(True)
        self.label10.setHidden(True)
        self.label11.setHidden(True)
        self.label12.setHidden(True)
        self.lineedit1.setHidden(False)
        self.lineedit2.setHidden(True)
        self.lineedit3.setHidden(True)
        self.lineedit4.setHidden(True)
        self.lineedit5.setHidden(True)
        self.lineedit6.setHidden(True)
        self.lineedit7.setHidden(True)
        self.lineedit8.setHidden(True)
        self.lineedit9.setHidden(True)
        self.lineedit10.setHidden(True)
        self.lineedit11.setHidden(True)
        self.lineedit12.setHidden(True)
 


    def radioclicked_yes(self):

        self.window2.hide()
        self.window2.unhide2()
        self.labelupload.setText('yes')
        #self.combobox_bar.setDisabled(False)
        self.label_barcode_yes_no.setText('yes')
        self.checkbox.setDisabled(False)
        self.checkbox_95.setDisabled(False)
        #self.checkbox.setHidden(False)
        #self.textedit.setDisabled(True)
        #self.textedit.setHidden(True)
        self.label1.setHidden(False)
        self.label2.setHidden(False)
        self.label3.setHidden(False)
        self.label4.setHidden(False)
        self.label5.setHidden(False)
        self.label6.setHidden(False)
        self.label7.setHidden(False)
        self.label8.setHidden(False)
        self.label9.setHidden(False)
        self.label10.setHidden(False)
        self.label11.setHidden(False)
        self.label12.setHidden(False)
        self.lineedit1.setHidden(False)
        self.lineedit2.setHidden(False)
        self.lineedit3.setHidden(False)
        self.lineedit4.setHidden(False)
        self.lineedit5.setHidden(False)
        self.lineedit6.setHidden(False)
        self.lineedit7.setHidden(False)
        self.lineedit8.setHidden(False)
        self.lineedit9.setHidden(False)
        self.lineedit10.setHidden(False)
        self.lineedit11.setHidden(False)
        self.lineedit12.setHidden(False)

    
    def clickbox(self, state):
        if state == QtCore.Qt.Checked:
            self.tablewidget.setHidden(True)
            self.checkbox_95.setChecked(False)
            self.label13.setHidden(False)
            self.lineedit13.setHidden(False)
            self.label14.setHidden(False)
            self.lineedit14.setHidden(False)
            self.label15.setHidden(False)
            self.lineedit15.setHidden(False)
            self.label16.setHidden(False)
            self.lineedit16.setHidden(False)
            self.label17.setHidden(False)
            self.lineedit17.setHidden(False)
            self.label18.setHidden(False)
            self.lineedit18.setHidden(False)
            self.label19.setHidden(False)
            self.lineedit19.setHidden(False)
            self.label20.setHidden(False)
            self.lineedit20.setHidden(False)
            self.label21.setHidden(False)
            self.lineedit21.setHidden(False)
            self.label22.setHidden(False)
            self.lineedit22.setHidden(False)
            self.label23.setHidden(False)
            self.lineedit23.setHidden(False)
            self.label24.setHidden(False)
            self.lineedit24.setHidden(False)
            self.window2.unhide()
        else:
            self.label13.setHidden(True)
            self.lineedit13.setHidden(True)
            self.label14.setHidden(True)
            self.lineedit14.setHidden(True)
            self.label15.setHidden(True)
            self.lineedit15.setHidden(True)
            self.label16.setHidden(True)
            self.lineedit16.setHidden(True)
            self.label17.setHidden(True)
            self.lineedit17.setHidden(True)
            self.label18.setHidden(True)
            self.lineedit18.setHidden(True)
            self.label19.setHidden(True)
            self.lineedit19.setHidden(True)
            self.label20.setHidden(True)
            self.lineedit20.setHidden(True)
            self.label21.setHidden(True)
            self.lineedit21.setHidden(True)
            self.label22.setHidden(True)
            self.lineedit22.setHidden(True)
            self.label23.setHidden(True)
            self.lineedit23.setHidden(True)
            self.label24.setHidden(True)
            self.lineedit24.setHidden(True)
            self.window2.hide()

    def clickbox2(self,state):
        if state == QtCore.Qt.Checked:
            self.checkbox.setChecked(False)
            self.tablewidget.setHidden(False)
            self.label1.setHidden(True)
            self.label2.setHidden(True)
            self.label3.setHidden(True)
            self.label4.setHidden(True)
            self.label5.setHidden(True)
            self.label6.setHidden(True)
            self.label7.setHidden(True)
            self.label8.setHidden(True)
            self.label9.setHidden(True)
            self.label10.setHidden(True)
            self.label11.setHidden(True)
            self.label12.setHidden(True)
            self.lineedit1.setHidden(True)
            self.lineedit2.setHidden(True)
            self.lineedit3.setHidden(True)
            self.lineedit4.setHidden(True)
            self.lineedit5.setHidden(True)
            self.lineedit6.setHidden(True)
            self.lineedit7.setHidden(True)
            self.lineedit8.setHidden(True)
            self.lineedit9.setHidden(True)
            self.lineedit10.setHidden(True)
            self.lineedit11.setHidden(True)
            self.lineedit12.setHidden(True)
        else:
            self.tablewidget.setHidden(True)
            self.label1.setHidden(False)
            self.label2.setHidden(False)
            self.label3.setHidden(False)
            self.label4.setHidden(False)
            self.label5.setHidden(False)
            self.label6.setHidden(False)
            self.label7.setHidden(False)
            self.label8.setHidden(False)
            self.label9.setHidden(False)
            self.label10.setHidden(False)
            self.label11.setHidden(False)
            self.label12.setHidden(False)
            self.lineedit1.setHidden(False)
            self.lineedit2.setHidden(False)
            self.lineedit3.setHidden(False)
            self.lineedit4.setHidden(False)
            self.lineedit5.setHidden(False)
            self.lineedit6.setHidden(False)
            self.lineedit7.setHidden(False)
            self.lineedit8.setHidden(False)
            self.lineedit9.setHidden(False)
            self.lineedit10.setHidden(False)
            self.lineedit11.setHidden(False)
            self.lineedit12.setHidden(False)


    def passinInformation(self):
        
        self.window2.input000.setText(self.combobox_barcode.currentText())
        self.window2.input0.setText(self.list_kits.currentText())
        self.window2.input00.setText(self.combobox_kit.currentText())
        self.window2.input1.setText(self.lineedit1.text())
        self.window2.input3.setText(self.lineedit3.text())
        self.window2.input2.setText(self.lineedit2.text())
        self.window2.input4.setText(self.lineedit4.text())
        self.window2.input5.setText(self.lineedit5.text())
        self.window2.input6.setText(self.lineedit6.text())
        self.window2.input7.setText(self.lineedit7.text())
        self.window2.input8.setText(self.lineedit8.text())
        self.window2.input9.setText(self.lineedit9.text())
        self.window2.input10.setText(self.lineedit10.text())
        self.window2.input11.setText(self.lineedit11.text())
        self.window2.input12.setText(self.lineedit12.text())
        self.window2.input13.setText(self.lineedit13.text())
        self.window2.input14.setText(self.lineedit14.text())
        self.window2.input15.setText(self.lineedit15.text())
        self.window2.input16.setText(self.lineedit16.text())
        self.window2.input17.setText(self.lineedit17.text())
        self.window2.input18.setText(self.lineedit18.text())
        self.window2.input19.setText(self.lineedit19.text())
        self.window2.input20.setText(self.lineedit20.text())
        self.window2.input21.setText(self.lineedit21.text())
        self.window2.input22.setText(self.lineedit22.text())
        self.window2.input23.setText(self.lineedit23.text())
        self.window2.input24.setText(self.lineedit24.text())





        self.window2.displayInfo()


    def anwenden(self, state):
        kitliste = ['SQK-PCB109','SQK-RNA002','SQK-PCS109','SQK-DCS109','SQK-CS9109','SQK-LSK109','SQK-LSK109-XL','SQK-16S024','SQK-LSK110',
        'SQK-LRK001','SQK-RBK004','SQK-PBK004','SQK-RAB204','SQK-RPB004','SQK-PSK004','SQK-RAD004']
        self.list_kits.clear()
        self.list_kits.addItems(kitliste)
        
        trigger1 = 0
        trigger2 = 0
        trigger3 = 0
        y = 0
        z = 0
        x = 0
        dna = 0 
        rna = 0
        pcr = 0
        pcr_free = 0
        yes = 0
        no = 0
        
        
        dna = self.dna_checkbox.checkState()  #  0 for un-checked state, 2 for checked state
        if dna == 2:
            trigger1 = 'DNA'
            
        rna = self.rna_checkbox.checkState()
        if rna == 2:
            trigger1 = 'RNA'

        pcr = self.pcr_checkbox.checkState()
        if pcr == 2:
            trigger2 = 'PCR'
        
        pcr_free = self.pcr_free_checkbox.checkState()
        if pcr_free == 2:
            trigger2 = 'PCR_Free'

        no = self.no_checkbox.checkState()
        if no == 2:
            trigger3 = 'no'

        yes = self.yes_checkbox.checkState()
        if yes == 2:
            trigger3 = 'yes'
        
        

        
        url="https://raw.githubusercontent.com/t3ddezz/kitslist/main/Kits_real1.tsv"
        re=requests.get(url).content
        sequencing=pd.read_csv(io.StringIO(re.decode('utf-8')),sep='\t',index_col=False,)#na_filter=False)
        e = len(sequencing.columns)
        sequencing.insert(e,'liste2',0,True)
        sequencing.insert(e,'liste1',0,True)

        if trigger1 == 'DNA' or trigger1 == 'RNA':
            
            z = trigger1
            if trigger2 == 'PCR' or trigger2 == 'PCR_Free':
                x = trigger2
                if trigger3 == 'yes' or trigger3 == 'no':
                    y = trigger3

            else:
                if trigger3 == 'yes' or trigger3 == 'no':
                    x = trigger3
                
                '''else:
                    c = 0
                    a = 0
                    d = len(sequencing)
                     
                    while True:
                        if sequencing.loc[a,z] == sequencing.loc[a,z]:
                            c = sequencing.loc[a,z]
                            sequencing.loc[[a],['liste1']] = c
                            a = a + 1
                            print(c)
                        
                        else:
                            a = a + 1
                        if a == d:
                            a = 0
                            c = 0

                            break

                        kitlist = []
                    while True:
                        if sequencing.loc[a,'liste1']!= 0:
                            c = sequencing.loc[a,'liste1']
                            kitlist.append(c)
    
    
    
                            a = a + 1
                        else:
                            a = a + 1 
    
                        if a == d:
                            break 
                    print(kitlist)
                    #kitlist = sequencing['liste1'].tolist()
                    
                    
                    kitlist = sequencing[z].tolist()
                    
                    print(kitlist)
                    self.list_kits.clear()
                    self.list_kits.addItems(kitlist)'''

        else:
  
            if trigger2 == 'PCR' or trigger2 == 'PCR_Free':
                z = trigger2
                if trigger3 == 'yes' or trigger3 == 'no':
                    x = trigger3
    
            else:
                if trigger3 == 'yes' or trigger3 == 'no':
                    z = trigger3
                    
                
                '''else:
                    self.list_kits.clear()
                    self.list_kits.addItems(kitliste)'''
                    


        if z and y and x !=0:
          a = 0
          b = 0
          c = 0
          d = len(sequencing)
          f = len(sequencing)
  




          while True:
                p = sequencing.loc[a,z]
                if sequencing.loc[a,z] == sequencing.loc[b,x]:
                    c = sequencing.loc[b,x]
                    sequencing.loc[[a], ['liste1']] = c
    
    
    
                    a = a + 1
                    b = 0
    

                else: 
                    b = b + 1
                    if b == 12:
                        a = a + 1
                        b = 0
    
  
                if a == d:
                    a = 0
                    b = 0
                    c = 0

                    break 
          
          while True:
              if sequencing.loc[a,'liste1'] == sequencing.loc[b,y]:
                    c = sequencing.loc[b,y]
                    sequencing.loc[[a], ['liste2']] = c
    
                    a = a + 1
                    b = 0
    

              else: 
                    b = b + 1
                    if b == f:
                        a = a + 1
                        b = 0
              if a == d:
                    a = 0
                    b = 0
                    c = 0
                    break      

          
          kitlist = []
          while True:
                if sequencing.loc[a,'liste2']!= 0:
                  c = sequencing.loc[a,'liste2']
                  kitlist.append(c)
                  a = a + 1
                else:
                    a = a + 1 
    
                if a == d:
                    break 
          print(kitlist)
          self.list_kits.clear()
          self.list_kits.addItems(kitlist)


        else:
            if z and x !=0:
                a = 0
                b = 0
                c = 0
                d = len('liste1')
                e = len(sequencing.columns)
                kitlist = []
    
                '''while True:
                    if sequencing.loc[a,'liste1'] == sequencing.loc[b,y]:
                        c = sequencing.loc[b,y]
                        sequencing.loc[[a], ['liste2']] = c
    
                        a = a + 1
                        b = 0
    

                    else: 
                        b = b + 1
                        if b == f:
                            a = a + 1
                            b = 0
                    if a == d:
                        break''' 
                while True:
                
                    if sequencing.loc[a,z] == sequencing.loc[b,x]:
                        c = sequencing.loc[b,x]
                        sequencing.loc[[a], ['liste1']] = c
    
    
    
                        a = a + 1
                        b = 0
    

                    else: 
                        b = b + 1
                        if b == 12:
                            a = a + 1
                            b = 0
    
  
                    if a == d:
                        a = 0
                        b = 0
                        c = 0

                        break 

                while True:
                        if sequencing.loc[a,'liste1']!= 0:
                            c = sequencing.loc[a,'liste1']
                            kitlist.append(c)
    
    
    
                            a = a + 1
                        else:
                            a = a + 1 
    
                        if a == d:
                            break 
                print(kitlist)
                '''kitlist = sequencing[:,'liste2'].tolist()'''
                self.list_kits.clear()
                self.list_kits.addItems(kitlist)        
            else:
                if z != 0:
                    c = 0
                    a = 0
                    d = len(sequencing)
                    kitlist = []
                    while True:
                        if sequencing.loc[a,z] == sequencing.loc[a,z]:
                            c = sequencing.loc[a,z]
                            sequencing.loc[[a],['liste1']] = c
                            a = a + 1
                            
                        
                        else:
                            a = a + 1
                        if a == d:
                            a = 0
                            c = 0

                            break
                    
                    while True:
                        if sequencing.loc[a,'liste1']!= 0:
                            c = sequencing.loc[a,'liste1']
                            kitlist.append(c)
    
    
    
                            a = a + 1
                        else:
                            a = a + 1 
    
                        if a == d:
                            break 
                    print(kitlist)
                    
                    '''kitlist = sequencing[z].tolist()
                    print(kitlist)'''
                    self.list_kits.clear()
                    self.list_kits.addItems(kitlist)
        d = len(sequencing) 
        a = 0

        del sequencing['liste1']
        del sequencing['liste2']
        kitlist = 0
        


   
        

def window():
    app = QApplication(sys.argv)
    
    


    app.setStyle('Fusion')
    dark_palette = QtGui.QPalette()

    dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)

    app.setPalette(dark_palette)

    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()    