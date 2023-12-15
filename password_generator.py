from PyQt6 import QtCore, QtGui, QtWidgets
import string
from random import *

class Ui_password_generater(object):

    def setupUi(self, password_generater):
        password_generater.setObjectName("password_generater")
        # password_generater.resize(454, 248)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(password_generater.sizePolicy().hasHeightForWidth())
        password_generater.setSizePolicy(sizePolicy)
        password_generater.setMinimumSize(QtCore.QSize(470, 350))
        password_generater.setMaximumSize(QtCore.QSize(470, 350))
        font = QtGui.QFont()
        font.setPointSize(10)
        password_generater.setFont(font)
        password_generater.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        password_generater.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

        self.l1 = QtWidgets.QLabel(parent=password_generater)
        self.l1.setGeometry(QtCore.QRect(45, 45, 180, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.l1.setFont(font)
        self.l1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.l1.setMouseTracking(True)
        self.l1.setAutoFillBackground(False)
        self.l1.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.l1.setScaledContents(False)
        self.l1.setWordWrap(False)
        self.l1.setIndent(0)
        self.l1.setOpenExternalLinks(False)
        self.l1.setObjectName("l1")

        self.passlen = QtWidgets.QLineEdit(parent=password_generater)
        self.passlen.setEnabled(True)
        self.passlen.setGeometry(QtCore.QRect(225, 45, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.passlen.setFont(font)
        self.passlen.setToolTipDuration(0)
        self.passlen.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.passlen.setText("")
        self.passlen.setFrame(True)
        self.passlen.setCursorPosition(0)
        self.passlen.setReadOnly(False)
        self.passlen.setClearButtonEnabled(True)
        self.passlen.setObjectName("passlen")

        self.l2 = QtWidgets.QLabel(parent=password_generater)
        self.l2.setGeometry(QtCore.QRect(45, 95, 180, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.l2.setFont(font)
        self.l2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.l2.setMouseTracking(True)
        self.l2.setAutoFillBackground(False)
        self.l2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.l2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.l2.setWordWrap(False)
        self.l2.setIndent(0)
        self.l2.setOpenExternalLinks(False)
        self.l2.setObjectName("l2")

        self.passcreate = QtWidgets.QPushButton(parent=password_generater)
        self.passcreate.setGeometry(QtCore.QRect(140, 250, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.passcreate.setFont(font)
        self.passcreate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.passcreate.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.passcreate.setIconSize(QtCore.QSize(10, 10))
        self.passcreate.setCheckable(False)
        self.passcreate.setObjectName("passcreate")

        self.l3 = QtWidgets.QLabel(parent=password_generater)
        self.l3.setGeometry(QtCore.QRect(45, 300, 180, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.l3.setFont(font)
        self.l3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.l3.setMouseTracking(True)
        self.l3.setAutoFillBackground(False)
        self.l3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.l3.setScaledContents(False)
        self.l3.setWordWrap(False)
        self.l3.setIndent(0)
        self.l3.setOpenExternalLinks(False)
        self.l3.setObjectName("l3")
        
        self.digits = QtWidgets.QCheckBox(parent=password_generater)
        self.digits.setGeometry(QtCore.QRect(225, 95, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.digits.setFont(font)
        self.digits.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.digits.setChecked(False)
        self.digits.setObjectName("digits")

        self.lowercase = QtWidgets.QCheckBox(parent=password_generater)
        self.lowercase.setGeometry(QtCore.QRect(225, 125, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lowercase.setFont(font)
        self.lowercase.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.lowercase.setIconSize(QtCore.QSize(16, 16))
        self.lowercase.setChecked(False)
        self.lowercase.setObjectName("lowercase")

        self.uppercase = QtWidgets.QCheckBox(parent=password_generater)
        self.uppercase.setGeometry(QtCore.QRect(225, 155, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.uppercase.setFont(font)
        self.uppercase.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.uppercase.setChecked(False)
        self.uppercase.setObjectName("uppercase")

        self.specialchar = QtWidgets.QCheckBox(parent=password_generater)
        self.specialchar.setGeometry(QtCore.QRect(225, 185, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.specialchar.setFont(font)
        self.specialchar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.specialchar.setObjectName("specialchar")

        self.password = QtWidgets.QLineEdit(parent=password_generater)
        self.password.setEnabled(True)
        self.password.setGeometry(QtCore.QRect(225, 300, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setToolTipDuration(0)
        self.password.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.password.setText("")
        self.password.setFrame(True)
        self.password.setCursorPosition(0)
        self.password.setReadOnly(True)
        self.password.setClearButtonEnabled(False)
        self.password.setObjectName("password")

        self.n1 = QtWidgets.QLabel(parent=password_generater)
        self.n1.setGeometry(QtCore.QRect(225, 65, 251, 21)) #225, 45, 200, 21
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.n1.setFont(font)
        self.n1.setIndent(4)
        self.n1.setObjectName("n1")
        self.n1.setVisible(False)

        self.n2 = QtWidgets.QLabel(parent=password_generater)
        self.n2.setEnabled(True)
        self.n2.setGeometry(QtCore.QRect(225, 205, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.n2.setFont(font)
        self.n2.setIndent(4)
        self.n2.setObjectName("n2")
        self.n2.setVisible(True)

        self.l4 = QtWidgets.QLabel(parent=password_generater)
        self.l4.setEnabled(True)
        self.l4.setGeometry(QtCore.QRect(345, 330, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.l4.setFont(font)
        self.l4.setIndent(4)
        self.l4.setObjectName("l4")
        self.l4.setVisible(True)

        self.retranslateUi(password_generater)
        QtCore.QMetaObject.connectSlotsByName(password_generater)

    def retranslateUi(self, password_generater):
        _translate = QtCore.QCoreApplication.translate
        password_generater.setWindowTitle(_translate("password_generater", "password_generater"))
        self.l1.setText(_translate("password_generater", "Length of Password"))
        self.l2.setText(_translate("password_generater", "Charecter Type"))
        self.passcreate.setText(_translate("password_generater", "Create Password"))
        self.l3.setText(_translate("password_generater", "Password "))
        self.lowercase.setText(_translate("password_generater", "Lowercase"))
        self.uppercase.setText(_translate("password_generater", "Uppercase"))
        self.digits.setText(_translate("password_generater", "Digits"))
        self.specialchar.setText(_translate("password_generater", "Special charecter"))
        self.n1.setText(_translate("password_generater", "*length  of password shoud be 6-20"))
        self.l4.setText(_translate("password_generater", "theprathamkhobragade"))

        self.passcreate.clicked.connect(self.passlens)
        self.passcreate.setShortcut(_translate("Form", "Return"))
        global clickd,clickl,clicku,clicks
        clickd=self.digits.isChecked()
        clickl=self.lowercase.isChecked()
        clicku=self.uppercase.isChecked()
        clicks=self.specialchar.isChecked()

        self.digits.clicked.connect(self.check                  )#------------------------------------------------------------------------
        self.lowercase.clicked.connect(self.check)
        self.uppercase.clicked.connect(self.check)
        self.specialchar.clicked.connect(self.check)

    def check(self):                    #------------------------------------------------------------------------
        global clickd,clickl,clicku,clicks
        clickd=self.digits.isChecked()
        clickl=self.lowercase.isChecked()
        clicku=self.uppercase.isChecked()
        clicks=self.specialchar.isChecked()
            
    def allow(self):                    #------------------------------------------------------------------------
        if((clickd and clickl and clicku and clicks)==False):
            self.password.setText("")
            self.n2.setText("*Select at least one option")
            self.n2.setVisible(True)
            self.n2.setStyleSheet("color: rgb(255, 0, 0);")  
    
    def passlens(self):                 #------------------------------------------------------------------------
        global plen,result,password,plen
        password=[]
        result=[]
        plen=self.passlen.text() 
        
        if((clickd or clickl or clicku or clicks)==False):
            self.password.setText("")
            self.n2.setText("*Select at least one option")
            self.n2.setVisible(True)
            self.n2.setStyleSheet("color: rgb(255, 0, 0);")
        elif((clickd or clickl or clicku or clicks)==True):
            self.n2.setVisible(False)

        if(len(plen)==0):
            self.n1.setText("Enter valid number")
            self.n1.setVisible(True)
            self.n1.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            plen=int(plen)
            if(plen<8 or plen>20):
                self.password.setText("")
                self.passlen.setText("")
                self.n1.setText("*length  of password shoud be 6-20")
                self.n1.setVisible(True)
                self.n1.setStyleSheet("color: rgb(255, 0, 0);")
            
            else:                   #------------------------------------------------------------------------
                self.n1.setVisible(False)
                
                if(plen<11):
                    if((clickd or clickl or clicku or clicks)==True):
                        self.n2.setVisible(False)
                        code()
                        p="".join(password)
                        self.password.setText(p)

                else:
                    if((clickd or clickl or clicku or clicks)==False):
                        self.password.setText("")
                        self.n2.setText("*Select at least one option")
                        self.n2.setVisible(True)
                        self.n2.setStyleSheet("color: rgb(255, 0, 0);")
                    
                    elif((clickd and (clickl or clicku or clicks))):
                        self.n2.setVisible(False)
                        code()
                        p="".join(password)
                        self.password.setText(p)
                    
                    elif((clicks and (clickl or clicku or clickd))):
                        self.n2.setVisible(False)
                        code()
                        p="".join(password)
                        self.password.setText(p)
                    
                    elif(clickl or clicku):
                        self.n2.setVisible(False)
                        code()
                        p="".join(password)
                        self.password.setText(p)
                    else:
                        self.password.setText("")
                        self.n2.setText("*Select more option")
                        self.n2.setVisible(True)
                        self.n2.setStyleSheet("color: rgb(255, 0, 0);")
                        pass

                                        
if __name__ == "__main__":                          #------------------------------------------------------------------------
    import sys
    app = QtWidgets.QApplication(sys.argv)
    password_generater = QtWidgets.QWidget()
    ui = Ui_password_generater()
    ui.setupUi(password_generater)
    password_generater.show()
    
    lowercase=list(string.ascii_lowercase)
    uppercase=list(string.ascii_uppercase)
    digits=list(string.digits)
    specialchar=['@','$','&','*','!','€','#','%', '/','=','?', '~']
    # specialchar=list(string.punctuation)

    def results(r):                         #-------------------------------------------------------------------
        x=0
        while x==0:
            x=randint(0,plen)
        for i in range(x):
            result.append(choice(r))

    def sure():                                 #----------------------------------------------------------------
        if(clickd):
            results(digits)
        if(clickl):
            results(lowercase)
        if(clicku):
            results(uppercase)  
        if(clicks):
            results(specialchar)
        else:
            pass


    def code():                                 #-------------------------------------------------------------------------
        global result
        while (len(result)<plen):
            sure()
            result=set(result)
            result=list(result)
        shuffle(result)

        final()
        p="".join(password)


    def count():                                    #-------------------------------------------------------------------------------------
        d=l=u=s=0
        for i in password:
            if(i in lowercase):
                l=l+1
            elif(i in uppercase):
                u=u+1
            elif (i in digits):
                d=d+1
            elif (i in specialchar):
                s=s+1
        
        if(clickd and d==0):
            del(password[:])
            final()

        if(clickl and l==0):
            del(password[:])
            final()

        if(clicku and u==0):
            del(password[:])
            final()

        if(clicks and s==0):
            del(password[:])
            final()

    def final():                            #---------------------------------------------------------------------------------------
        for i in range(0, plen):
            password.append(choice(result))
        count()

    sys.exit(app.exec())
