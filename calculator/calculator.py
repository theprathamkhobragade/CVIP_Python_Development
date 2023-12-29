from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_caluculator(object):
    def setupUi(self, caluculator):
        caluculator.setObjectName("caluculator")
        caluculator.setMinimumSize(411, 501)
        caluculator.setMaximumSize(411, 510)

        self.input = QtWidgets.QLineEdit(parent=caluculator)
        self.input.setGeometry(QtCore.QRect(10, 10, 391, 55))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        self.input.setFont(font)
        self.input.setStyleSheet("border:1px solid black;")
        self.input.setText("")
        self.input.setFrame(False)
        self.input.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.input.setReadOnly(True)
        self.input.setClearButtonEnabled(False)
        self.input.setObjectName("input")
        self.input.setToolTipDuration(0)
        self.input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.input.setText("")
        self.input.setFrame(False)
        self.input.setCursorPosition(0)
        self.input.setReadOnly(True)
        self.input.setClearButtonEnabled(False)
        self.input.setObjectName("input")

        self.input2 = QtWidgets.QLineEdit(parent=caluculator)
        self.input2.setGeometry(QtCore.QRect(11, 11, 389, 25))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        self.input2.setFont(font)
        self.input2.setStyleSheet("")
        self.input2.setText("")
        self.input2.setFrame(False)
        self.input2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.input2.setReadOnly(True)
        self.input2.setPlaceholderText("")
        self.input2.setClearButtonEnabled(False)
        self.input2.setObjectName("input2")
        self.input2.setVisible(False)

        self.division = QtWidgets.QPushButton(parent=caluculator)
        self.division.setGeometry(QtCore.QRect(9, 110, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.division.setFont(font)
        self.division.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.division.setAutoDefault(False)
        self.division.setDefault(False)
        self.division.setFlat(False)
        self.division.setObjectName("division")

        self.substraction = QtWidgets.QPushButton(parent=caluculator)
        self.substraction.setGeometry(QtCore.QRect(209, 110, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.substraction.setFont(font)
        self.substraction.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.substraction.setObjectName("substraction")

        self.addition = QtWidgets.QPushButton(parent=caluculator)
        self.addition.setEnabled(True)
        self.addition.setGeometry(QtCore.QRect(309, 110, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addition.setFont(font)
        self.addition.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addition.setObjectName("addition")

        self.multiplication = QtWidgets.QPushButton(parent=caluculator)
        self.multiplication.setEnabled(True)
        self.multiplication.setGeometry(QtCore.QRect(109, 110, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.multiplication.setFont(font)
        self.multiplication.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.multiplication.setObjectName("multiplication")

        self.equal = QtWidgets.QPushButton(parent=caluculator)
        self.equal.setEnabled(True)
        self.equal.setGeometry(QtCore.QRect(109, 429, 193, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.equal.setFont(font)
        self.equal.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.equal.setObjectName("equal")

        self.dot = QtWidgets.QPushButton(parent=caluculator)
        self.dot.setEnabled(True)
        self.dot.setGeometry(QtCore.QRect(310, 190, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dot.setFont(font)
        self.dot.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dot.setObjectName("dot")

        self.zero = QtWidgets.QPushButton(parent=caluculator)
        self.zero.setGeometry(QtCore.QRect(9, 429, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.zero.setFont(font)
        self.zero.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.zero.setObjectName("zero")

        self.one = QtWidgets.QPushButton(parent=caluculator)
        self.one.setGeometry(QtCore.QRect(9, 345, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.one.setFont(font)
        self.one.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.one.setObjectName("one")

        self.two = QtWidgets.QPushButton(parent=caluculator)
        self.two.setEnabled(True)
        self.two.setGeometry(QtCore.QRect(109, 345, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.two.setFont(font)
        self.two.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.two.setObjectName("two")

        self.three = QtWidgets.QPushButton(parent=caluculator)
        self.three.setGeometry(QtCore.QRect(209, 345, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.three.setFont(font)
        self.three.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.three.setObjectName("three")

        self.four = QtWidgets.QPushButton(parent=caluculator)
        self.four.setGeometry(QtCore.QRect(9, 265, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.four.setFont(font)
        self.four.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.four.setObjectName("four")

        self.five = QtWidgets.QPushButton(parent=caluculator)
        self.five.setEnabled(True)
        self.five.setGeometry(QtCore.QRect(109, 265, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.five.setFont(font)
        self.five.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.five.setObjectName("five")

        self.six = QtWidgets.QPushButton(parent=caluculator)
        self.six.setGeometry(QtCore.QRect(209, 265, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.six.setFont(font)
        self.six.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.six.setObjectName("six")

        self.seven = QtWidgets.QPushButton(parent=caluculator)
        self.seven.setGeometry(QtCore.QRect(9, 190, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.seven.setFont(font)
        self.seven.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.seven.setObjectName("seven")

        self.eight = QtWidgets.QPushButton(parent=caluculator)
        self.eight.setEnabled(True)
        self.eight.setGeometry(QtCore.QRect(109, 190, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.eight.setFont(font)
        self.eight.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.eight.setObjectName("eight")

        self.nine = QtWidgets.QPushButton(parent=caluculator)
        self.nine.setGeometry(QtCore.QRect(209, 190, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nine.setFont(font)
        self.nine.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.nine.setObjectName("nine")

        self.clear = QtWidgets.QPushButton(parent=caluculator)
        self.clear.setEnabled(True)
        self.clear.setGeometry(QtCore.QRect(309, 345, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        # font.setPointSize(12)
        font.setBold(True)
        font.setWeight(10)
        self.clear.setFont(font)
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clear.setObjectName("clear")

        self.delet = QtWidgets.QPushButton(parent=caluculator)
        self.delet.setEnabled(True)
        self.delet.setGeometry(QtCore.QRect(308, 265, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        # font.setPointSize(12)
        font.setBold(True)
        font.setWeight(20)
        self.delet.setFont(font)
        self.delet.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delet.setObjectName("delet")

        self.power = QtWidgets.QPushButton(parent=caluculator)
        self.power.setEnabled(True)
        self.power.setGeometry(QtCore.QRect(309, 429, 94, 57))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.power.setFont(font)
        self.power.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.power.setCheckable(True)
        self.power.setChecked(True)
        self.power.setStyleSheet("color:green")
        self.power.setDefault(False)
        self.power.setObjectName("power")

        self.l1 = QtWidgets.QLabel(parent=caluculator)
        self.l1.setEnabled(True)
        self.l1.setGeometry(QtCore.QRect(285, 490, 120, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.l1.setFont(font)
        self.l1.setIndent(4)
        self.l1.setObjectName("l1")
        self.l1.setVisible(True)

        self.retranslateUi(caluculator)
        QtCore.QMetaObject.connectSlotsByName(caluculator)

    def retranslateUi(self, caluculator):
        _translate = QtCore.QCoreApplication.translate
        caluculator.setWindowTitle(_translate("caluculator", "caluculator"))

        self.input.setPlaceholderText(_translate("caluculator", "0.0"))
        self.l1.setText(_translate("caluculator", "theprathamkhobragade"))

        self.division.setText(_translate("caluculator", "/"))
        self.division.setShortcut(_translate("caluculator", "/"))
        self.substraction.setText(_translate("caluculator", "-"))
        self.substraction.setShortcut(_translate("caluculator", "-"))
        self.addition.setText(_translate("caluculator", "+"))
        self.addition.setShortcut(_translate("caluculator", "+"))
        self.multiplication.setText(_translate("caluculator", "*"))
        self.multiplication.setShortcut(_translate("caluculator", "*"))

        self.dot.setText(_translate("caluculator", "."))
        self.dot.setShortcut(_translate("caluculator", "."))
        self.zero.setText(_translate("caluculator", "0"))
        self.zero.setShortcut(_translate("caluculator", "0"))
        self.one.setText(_translate("caluculator", "1"))
        self.one.setShortcut(_translate("caluculator", "1"))
        self.two.setText(_translate("caluculator", "2"))
        self.two.setShortcut(_translate("caluculator", "2"))
        self.three.setText(_translate("caluculator", "3"))
        self.three.setShortcut(_translate("caluculator", "3"))
        self.four.setText(_translate("caluculator", "4"))
        self.four.setShortcut(_translate("caluculator", "4"))
        self.five.setText(_translate("caluculator", "5"))
        self.five.setShortcut(_translate("caluculator", "5"))
        self.six.setText(_translate("caluculator", "6"))
        self.six.setShortcut(_translate("caluculator", "6"))
        self.seven.setText(_translate("caluculator", "7"))
        self.seven.setShortcut(_translate("caluculator", "7"))
        self.eight.setText(_translate("caluculator", "8"))
        self.eight.setShortcut(_translate("caluculator", "8"))
        self.nine.setText(_translate("caluculator", "9"))
        self.nine.setShortcut(_translate("caluculator", "9"))

        self.clear.setText(_translate("caluculator", "clear\nctrl+Bkspce"))
        self.clear.setShortcut(_translate("caluculator", "ctrl+Backspace"))
        self.delet.setText(_translate("caluculator", "del\nBackspace"))
        self.delet.setShortcut(_translate("caluculator", "Backspace"))
        self.power.setText(_translate("caluculator", "power"))
        self.equal.setText(_translate("caluculator", "="))
        self.equal.setShortcut(_translate("caluculator", "="))

        self.equal.clicked.connect(self.equal0)
        self.division.clicked.connect(self.division0)
        self.multiplication.clicked.connect(self.multiplication0)
        self.substraction.clicked.connect(self.substaction0)
        self.addition.clicked.connect(self.addition0)
        self.dot.clicked.connect(self.dot0)
        
        self.zero.clicked.connect(self.zero0)
        self.one.clicked.connect(self.one0)
        self.two.clicked.connect(self.two0)
        self.three.clicked.connect(self.three0)
        self.four.clicked.connect(self.four0)
        self.five.clicked.connect(self.five0)
        self.six.clicked.connect(self.six0)
        self.seven.clicked.connect(self.seven0)
        self.eight.clicked.connect(self.eight0)
        self.nine.clicked.connect(self.nine0)

        self.clear.clicked.connect(self.clear0)
        # self.clearsh.clicked.connect(self.clear0)
        self.delet.clicked.connect(self.delet0)
        self.power.clicked.connect(self.power0)
        checkp=self.power.isChecked()

    def power0(self):
        global checkp,result,temp,short,inputs
        checkp=self.power.isChecked()
        if(checkp==False):
            result=""
            temp=""
            short=[]
            inputs=[]

            self.power.setStyleSheet("color:red")
            self.zero.setEnabled(False)
            self.one.setEnabled(False)
            self.two.setEnabled(False)
            self.three.setEnabled(False)
            self.four.setEnabled(False)
            self.five.setEnabled(False)
            self.six.setEnabled(False)
            self.seven.setEnabled(False)
            self.eight.setEnabled(False)
            self.nine.setEnabled(False)
            self.dot.setEnabled(False)

            self.division.setEnabled(False)
            self.multiplication.setEnabled(False)
            self.addition.setEnabled(False)
            self.substraction.setEnabled(False)
            self.clear.setEnabled(False)
            self.delet.setEnabled(False)
            self.equal.setEnabled(False)
            self.input.setPlaceholderText("")
            self.input2.setText(temp)
            self.input.setText(result)
            
        else:
            self.power.setStyleSheet("color:green")
            self.zero.setEnabled(True)
            self.one.setEnabled(True)
            self.two.setEnabled(True)
            self.three.setEnabled(True)
            self.four.setEnabled(True)
            self.five.setEnabled(True)
            self.six.setEnabled(True)
            self.seven.setEnabled(True)
            self.eight.setEnabled(True)
            self.nine.setEnabled(True)
            self.dot.setEnabled(True)
            
            self.division.setEnabled(True)
            self.multiplication.setEnabled(True)
            self.addition.setEnabled(True)
            self.substraction.setEnabled(True)
            self.clear.setEnabled(True)
            self.delet.setEnabled(True)
            self.equal.setEnabled(True)
            self.input.setPlaceholderText("0.0")

    def clear0(self):
        global temp, short
        result=""
        temp="0"
        short=[]
        self.input.setText("")
        self.input2.setText("")
    
    def delet0(self):
        global temp
        if(len(short)==1):
            short.clear()
            for i in range(0,len(temp)):
                short.append(temp[i])
        
        if(len(temp)!=0):
            temp=temp[:-1]
            j="".join(short)
            if(temp!=j):
                short.clear()
                for i in range(0,len(temp)):
                    short.append(temp[i])
            
        self.input.setText(temp)
        self.input2.setVisible(False)

    def equal0(self):
        global temp ,result
        result=""
        if(len(temp)==0):
            temp=temp+"0"
        if(temp[-1]=='*' or temp[-1]=='/' or temp[-1]=='+' or temp[-1]=='-' or temp[-1]=='='):
            temp=temp[:-1]
        pratham('=')
        equal()
        calculate()
        self.input2.setVisible(True)
        self.input2.setText(temp)
        self.input.setText(str(result))
        
        temp=str(result)
        inputs.clear()

    def division0(self):
        self.input2.setVisible(False)
        global temp
        if(len(temp)==0 or temp[-1]=="."):
            temp=temp+"0"
        if(temp[-1]=='*' or temp[-1]=='/' or temp[-1]=='+' or temp[-1]=='-' or temp[-1]=='='):
            temp=temp[:-1]

        pratham('/')
        self.input.setText(temp)
    
    def multiplication0(self):
        self.input2.setVisible(False)
        global temp
        if(len(temp)==0 or temp[-1]=="."):
            temp=temp+"0"
        if(temp[-1]=='*' or temp[-1]=='/' or temp[-1]=='+' or temp[-1]=='-' or temp[-1]=='='):
            temp=temp[:-1]

        pratham('*')
        self.input.setText(temp)
    
    def substaction0(self):
        self.input2.setVisible(False)
        global temp
        if(len(temp)==0 or temp[-1]=="."):
            temp=temp+"0"
        if(len(temp)>1):
            if(temp[-1]=='*' or temp[-1]=='/' or temp[-1]=='+' or temp[-1]=='-' or temp[-1]=='='):
                temp=temp[:-1]

        pratham('-')
        self.input.setText(temp)
    
    def addition0(self):
        self.input2.setVisible(False)
        global temp
        if(len(temp)==0 or temp[-1]=="."):
            temp=temp+"0"
        if(temp[-1]=='*' or temp[-1]=='/' or temp[-1]=='+' or temp[-1]=='-' or temp[-1]=='='):
            temp=temp[:-1]

        pratham('+')
        self.input.setText(temp)
    
    def dot0(self):
        global temp
        if(len(temp)==0 or temp[-1]=='*' or temp[-1]=='/' or temp[-1]=='+' or temp[-1]=='-' or temp[-1]=='='):
            temp=temp+"0"
        if(temp[-1]!='.' ):
            pratham('.')
        self.input.setText(temp)

    def zero0(self):
        self.input2.setVisible(False)
        global temp
        pratham('0')
        self.input.setText(temp)
    
    def one0(self):
        self.input2.setVisible(False)
        global temp
        pratham('1')
        self.input.setText(temp)

    def two0(self):
        self.input2.setVisible(False)
        global temp
        pratham('2')
        self.input.setText(temp)
     
    def three0(self):
        self.input2.setVisible(False)
        global temp
        pratham('3')
        self.input.setText(temp)
        
    def four0(self):
        self.input2.setVisible(False)
        global temp
        pratham('4')

        self.input.setText(temp)
    
    def five0(self):
        self.input2.setVisible(False)
        global temp
        pratham('5')
        self.input.setText(temp)
   
    def six0(self):
        self.input2.setVisible(False)
        global temp
        pratham('6')
        self.input.setText(temp)
    
    def seven0(self):
        self.input2.setVisible(False)
        global temp
        pratham('7')
        self.input.setText(temp)
    
    def eight0(self):
        self.input2.setVisible(False)
        global temp
        pratham('8')
        self.input.setText(temp)

    def nine0(self):
        self.input2.setVisible(False)
        global temp
        pratham('9')
        self.input.setText(temp)
    
if __name__ == "__main__":
    global temp
    inputs=[]
    temp=""
    short=[]
    # result=9
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    caluculator = QtWidgets.QWidget()
    ui = Ui_caluculator()
    ui.setupUi(caluculator)
    caluculator.show()
    
    def calculate():
        global result
        if(inputs[0]=="/" or inputs[0]=="*" or inputs[0]=="-" or inputs[0]=="+"):
            for i in  range(1,len(inputs),2):
                j=inputs[i]
                k=j.find(".")
                if(k!=-1):
                    inputs[i]=float(inputs[i])
                else:
                    inputs[i]=int(inputs[i])

        else:
            for i in  range(0,len(inputs),2):
                j=inputs[i]
                k=j.find(".")
                if(k!=-1):
                    inputs[i]=float(inputs[i])
                else:
                    inputs[i]=int(inputs[i])
        
        division()
        multiplication()
        substaction()
        addition()
        
        result=inputs[0]
        result=str(result)
        if(result.endswith(".0")):
            result=float(result)
            result=int(result)
            result=str(result)

        else:
            j=result.find(".")
            if j!=-1:
                result=float(result)
                result=round(result,2)
                result=str(result)

        short.clear()
        for i in range(len(result)):
            
            short.append(result[i])
            
        return result
        

    def pratham(i):
        global temp,old
        old=[]
        
        if(i=="/" or i=="*" or i=="-" or i=="+" or i=="=" or i=="."):
            short.clear()
            short.append(temp)

        short.append(i)
        temp="".join(short)
    def equal():
        for i in range(len(temp)):
            
            if(temp[i]=="/" or temp[i]=="*" or temp[i]=="-" or temp[i]=="+" or temp[i]=="="):
                k="".join(old)
                if(k!=""):
                    inputs.append(k)
                old.clear()

            old.append(temp[i])
            if(old[0]=="/" or old[0]=="*" or old[0]=="-" or old[0]=="+" or old[0]=="="):
                if(old[0]!="="):
                    inputs.append(old[0])
                old.clear()
            r="".join(old)

    def division():
        for i in range(len(inputs)):
            if(inputs[i]=="/"):
                inputs[i]=inputs[i-1]/inputs[i+1]
                del(inputs[i+1])
                del(inputs[i-1])

                for i in range(len(inputs)):
                    if(inputs[i]=="/"):
                        division()
                        break
                break
    
    def multiplication():
        for i in range(len(inputs)):
            if(inputs[i]=="*"):
                inputs[i]=inputs[i-1]*inputs[i+1]
                del(inputs[i+1])
                del(inputs[i-1])

                for i in range(len(inputs)):
                    if(inputs[i]=="*"):
                        multiplication()
                        break
                break

    def addition():
        for i in range(len(inputs)):
            if(inputs[i]=="+"):
                
                inputs[i]=inputs[i-1]+inputs[i+1]
                del(inputs[i+1])
                del(inputs[i-1])

                for i in range(len(inputs)):
                    if(inputs[i]=="+"):
                        addition()
                        break
                break

    def substaction():
        if(inputs[0]=="-"):
            if(len(inputs)>2):
                if(inputs[2]=="+"):
                    inputs[0]=inputs[3]-inputs[1]
                    del(inputs[3])
                    del(inputs[2])
                    del(inputs[1])

                elif(inputs[2]=="-"):
                    inputs[0]=-(inputs[3]+inputs[1])
                    del(inputs[3])
                    del(inputs[2])
                    del(inputs[1])
                else:
                    pass

            else:
                inputs[0]=-inputs[1]
        else:
            for i in range(len(inputs)):
                if(inputs[i]=="-"):
                        inputs[i]=inputs[i-1]-inputs[i+1]
                        del(inputs[i+1])
                        del(inputs[i-1])

                        for i in range(len(inputs)):
                            if(inputs[i]=="-"):
                                substaction()
                                break
                        break

    sys.exit(app.exec())