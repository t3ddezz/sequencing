from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import sys

class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("check your data")
        self.setGeometry(400, 400, 330, 385)
        
        #self.window1 = MyWindow()
        
        #self.input_yes_no = QtWidgets.QLabel(self)
        #self.input_yes_no.move(115, 50)
        #self.input_yes_no.setText('-')
        
        self.input_flowcell = QtWidgets.QLabel(self)
        #self.input_flowcell.setText('FLO-MIN106')
        self.input_flowcell.move(115,50)
        

        self.label_flowcell = QtWidgets.QLabel(self)
        self.label_flowcell.setText('sampel name:')
        self.label_flowcell.move(20, 70)
        
        
        self.kitlabel = QtWidgets.QLabel(self)
        self.kitlabel.move(20, 10)
        self.kitlabel.setText('Kit:')

        self.barlabel = QtWidgets.QLabel(self)
        self.barlabel.move(20, 30)
        self.barlabel.setText('Barcoding Kit:')
        
        self.barcodinglabel = QtWidgets.QLabel(self)
        self.barcodinglabel.move(20, 50)
        self.barcodinglabel.setText('Barcode:')
        
        self.input0 = QtWidgets.QLabel(self)
        self.input0.move(115, 10)

        self.input00 = QtWidgets.QLabel(self)
        self.input00.move(115, 30)
        
        self.input1 = QtWidgets.QLabel(self)
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
        self.button.clicked.connect(self.close)

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

    def displayInfo(self):
        self.show( )


    #def upload_activated(self):
        #self.window1.button_upload.setEnabled(True)
         

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        
        #self.secondwindow = Window2()
        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle('Tool summary')
        self.iniUI()

      


    
    def iniUI(self):

        self.window2 = Window2()
        
        
        

        self.label_kit = QtWidgets.QLabel(self)
        self.label_kit.setText('choose one kit')
        self.label_kit.move(45, 10)

        self.combobox_kit = QtWidgets.QComboBox(self)
        kits = ['Select kit','LSK-109','110','RPB004']
        self.combobox_kit.addItems(kits)
        self.combobox_kit.move(40,30)
        self.combobox_kit.view().setRowHidden(0, True)
        self.combobox_kit.activated.connect(self.showComboMessage)
        
        self.qlabel = QtWidgets.QLabel(self)
        self.qlabel.setText('')
        self.qlabel.setHidden(True)

        self.qlabel2 = QtWidgets.QLabel(self)
        self.qlabel2.setText('')
        self.qlabel2.setHidden(True)

        self.qlabel3 = QtWidgets.QLabel(self)
        self.qlabel3.setText('')
        self.qlabel3.setHidden(True)
        
        self.combobox_kit.activated[str].connect(self.onChanged) 

        self.combobox_bar = QtWidgets.QComboBox(self)
        kits2 = ['Select kit','EXP-NBD104','NBD114','RPB004']
        self.combobox_bar.addItems(kits2)
        self.combobox_bar.move(40,115)
        self.combobox_bar.view().setRowHidden(0, True)
        self.combobox_bar.activated.connect(self.showComboMessage2)
        self.combobox_bar.setDisabled(True)

        self.combobox_bar.activated[str].connect(self.onChanged2)

        self.label_barcode = QtWidgets.QLabel(self)
        self.label_barcode.setText('barcode?')
        self.label_barcode.move(47, 50)

        self.combobox_barcode = QtWidgets.QComboBox(self)
        kits2 = ['choose barcode','FLO-MIN106']
        self.combobox_barcode.addItems(kits2)
        self.combobox_barcode.move(40,145)
        self.combobox_barcode.adjustSize()
        self.combobox_barcode.view().setRowHidden(0, True)
        self.combobox_barcode.activated.connect(self.showComboMessage3)
        
        self.combobox_barcode.activated[str].connect(self.onChanged3)
    
        
        
        self.radiobutton_no = QtWidgets.QRadioButton(self)
        self.radiobutton_no.toggled.connect(self.radioclicked_no)
        self.radiobutton_no.move(45, 70)
        #self.radiobutton_no.setChecked(True)
        self.label_radiobutton_no = QtWidgets.QLabel(self)
        self.label_radiobutton_no.setText('no')
        self.label_radiobutton_no.move(65, 70)
       

        self.textedit = QtWidgets.QTextEdit(self)
        self.textedit.setGeometry(45, 180, 200, 150)
        #self.textedit.setHidden(True)



        self.radiobutton_yes = QtWidgets.QRadioButton(self)
        self.radiobutton_yes.toggled.connect(self.radioclicked_yes)
        self.radiobutton_yes.move(100, 70)
        
        self.label_radiobutton_yes = QtWidgets.QLabel(self)
        self.label_radiobutton_yes.setText('yes')
        self.label_radiobutton_yes.move(120, 70)
        
        
        self.label_barcode_yes_no = QtWidgets.QLabel(self)
        self.label_barcode_yes_no.setHidden(True)

    




        '''self.label_samplename = QtWidgets.QLabel(self)
        self.label_samplename.setText('insert sample name')
        self.label_samplename.move(45, 265)
        self.label_samplename.adjustSize()
        

        self.lineedit_samplename = QtWidgets.QLineEdit(self)
        self.lineedit_samplename.move(45, 280)
        self.lineedit_samplename.setGeometry(45, 280, 200, 30)'''

        self.label1 = QtWidgets.QLabel(self)
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

        

        self.button_checkdata = QtWidgets.QPushButton(self)
        self.button_checkdata.setText('check data')
        self.button_checkdata.move(40, 330)
        #self.button_checkdata.clicked.connect(self.clicked)
        #self.button_checkdata.clicked.connect(self.window2)
        #self.button_checkdata.clicked.connect(self.uplaod)
        #self.button_checkdata.clicked.connect(self.passinginfo)
        self.button_checkdata.clicked.connect(self.passinInformation)


     

        self.button_upload = QtWidgets.QPushButton(self)
        self.button_upload.setText('upload')
        self.button_upload.move(40, 360)
        self.button_upload.setEnabled(False)

        self.checkbox = QtWidgets.QCheckBox("24-sample names",self)
        self.checkbox.adjustSize()
        self.checkbox.stateChanged.connect(self.clickbox)
        self.checkbox.move(100, 95)
        self.checkbox.setDisabled(True)
        #self.checkbox.setHidden(True)


    def onChanged(self, text):
        self.qlabel.setText(text)
    
    
    def onChanged2(self, text):
        self.qlabel2.setText(text)
    
    
    def onChanged3(self, text):
        self.qlabel3.setText(text)

   
    def showComboMessage(self, index=-1, enable=False):
        if index:
            self.combobox_kit.model().item(0).setEnabled(enable)
   
   
    def showComboMessage2(self, index=-1, enable=False):
        if index:
            self.combobox_bar.model().item(0).setEnabled(enable)
    
    
    def showComboMessage3(self, index=-1, enable=False):
        if index:
            self.combobox_barcode.model().item(0).setEnabled(enable)

   
    def radioclicked_no(self): 

        self.window2.hide()
        self.window2.hide2()

        self.combobox_bar.setDisabled(True)
        self.label_barcode_yes_no.setText('no')
        self.checkbox.setChecked(False)
        self.checkbox.setDisabled(True)
        #self.checkbox.setHidden(True)
        #self.textedit.setDisabled(False)
        #self.textedit.setHidden(False)
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
        
    
    #def uplaod(self):
        #self.button_upload.setEnabled(True)
    
    
    def radioclicked_yes(self):

        self.window2.unhide2()

        self.combobox_bar.setDisabled(False)
        self.label_barcode_yes_no.setText('yes')
        self.checkbox.setDisabled(False)
        #self.checkbox.setHidden(False)
        #self.textedit.setDisabled(True)
        #self.textedit.setHidden(True)
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

   
    def passinInformation(self):
        
        self.window2.input_flowcell.setText(self.qlabel3.text())
        #self.window2.input_yes_no.setText(self.label_barcode_yes_no.text())
        self.window2.input0.setText(self.qlabel.text())
        self.window2.input00.setText(self.qlabel2.text())
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

        


        
            
    
  
    

    '''def window2(self):                                             # <===
        self.w = Window2()
        self.w.show()'''
        

        
    




        
        
       
            

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

'''app.setStyle('Fusion')
    dark_palette = QtWidgets.QtPalette

    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)

    app.setPalette(dark_palette)

    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")'''

window()    