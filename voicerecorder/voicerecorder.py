from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
from PyQt6.QtGui import *
import sounddevice as sd
import soundfile as sf
import queue
import threading as td
import datetime
import glob
from pygame import mixer
import os
import shutil

def timerEvent0():           #-------------------------------------------------timerEvent0
    global time,timershow,timerlabel
    time=time.addSecs(1)
    timershow=time.toString("hh:mm:ss")
    timerlabel.setText(timershow)



def start0():                       #-------------------------------------------------start0
    global startbtn,timer,clicks,time,startthread,dirctlabel,clickp,timershow,dsply,voicelabel,newlabel,source,destination,filename,sthread
    play0()
    filename0()
    clicks=startbtn.isChecked()
    clickp=False
    
    if clicks:
        dsply=False
        display()
        startbtn.setIcon(QIcon('icons/stop.png'))
        startbtn.setIconSize(QSize(35,35))
        pausebtn.setEnabled(True)
        pausebtn.setVisible(True)
        voicelabel.setVisible(True)
        timerlabel.setVisible(True)
        timer = QTimer()
        time = QTime(0, 0, 0)
        timer.start(1000)
        timer.timeout.connect(timerEvent0)
        sthread=True
        # stops_threads=False
        startthread=td.Thread(target=rec0)
        os.chdir("tempfiles")
        startthread.start()
        filelabel.setVisible(False)
        newlabel.setVisible(False)

    else:
        dsply=True
        sthread=False
        # stops_threads=True
        timer.stop()
        
        source=os.getcwd()+"\\"+filename
        os.chdir("..")
        destination=os.getcwd()+"\\"+filename
        pausebtn.setEnabled(False)
        pausebtn.setVisible(False)
        voicelabel.setVisible(False)
        timerlabel.setVisible(False)
        newlabel.setVisible(True)
        startbtn.setIcon(QIcon('icons/start.png'))
        startbtn.setIconSize(QSize(40,40))
        timerlabel.setText("00:00:00")
        # files0()
        filelabel.setVisible(True)
        

def filename0():                        #----------------------------------------------------------filename0
    global y
    x = datetime.datetime.now()
    y=x.strftime("%Y")
    y=y+x.strftime("%m")
    y=y+x.strftime("%d")
    y=y+"_"
    y=y+x.strftime("%H")
    y=y+x.strftime("%M")
    y=y+x.strftime("%S")

def rec0():                       #----------------------------------------------------------rec0
    global y,clickp,source,destination,filename
    q = queue.Queue()
    def callback(indata, frames, time, status):
        if clickp==False:
            q.put(indata.copy())

    filename=y+".wav"
    with sf.SoundFile(filename, mode='x', samplerate=41000,channels=2) as file:
        with sd.InputStream(samplerate=41000,channels=2, callback=callback):
            while sthread:
                if clickp==False:
                    file.write(q.get())
                else:
                    pass
                # if stops_threads:
                #     break
    shutil.move(source,destination)
    files0()

def pause0():               #------------------------------------------------------------------------pause0
    global pausebtn,clicks,clickp
    if clicks:
        clickp=pausebtn.isChecked()
        if clickp:
            timer.stop()
            pausebtn.setIcon(QIcon('../icons/pause.png'))
            pausebtn.setIconSize(QSize(40,40))
        else:
            timer.start(1000)
            pausebtn.setIcon(QIcon('../icons/resume.png'))
            pausebtn.setIconSize(QSize(40,40))
def buttons0():
    playbtn1.setIcon(QIcon('icons/pause.png'))
    playbtn2.setIcon(QIcon('icons/pause.png'))
    playbtn3.setIcon(QIcon('icons/pause.png'))
    playbtn4.setIcon(QIcon('icons/pause.png'))
    playbtn5.setIcon(QIcon('icons/pause.png'))
    playbtn6.setIcon(QIcon('icons/pause.png'))

def play0():                        #-------------------------------------------------------------------------play0
    mixer.init()
    global p1,p2,p3,p4,p5,p6,s,truelist,sthread,syz
    syz=False
    p1=playbtn1.isChecked() 
    p2=playbtn2.isChecked() 
    p3=playbtn3.isChecked() 
    p4=playbtn4.isChecked() 
    p5=playbtn5.isChecked() 
    p6=playbtn6.isChecked()

    
    buttons0()

    if mixer.get_busy():
        mixer.Sound.stop(s)


    if len(truelist)==0:
        truelist=[" "," "]
    
    if syz==False:
        del(truelist[0])

    def yz():
        while syz:
            if mixer.get_busy()==False:
                playbtn1.setChecked(False) 
                playbtn2.setChecked(False) 
                playbtn3.setChecked(False) 
                playbtn4.setChecked(False) 
                playbtn5.setChecked(False) 
                playbtn6.setChecked(False)
                
                buttons0()
                truelist.clear()
                break
            
    if p1:                          #---------------#---------------#
        s1=files[0]
        playbtn1.setIcon(QIcon('icons/resume.png'))
        truelist.append("p1")
        if truelist[0]!=truelist[1]:
            s=mixer.Sound(s1)
            mixer.Sound.play(s)
            syz=True
            sthread=td.Thread(target=yz)
            sthread.start()
        else:
            mixer.Sound.stop(s)
            truelist.clear()
            playbtn1.setIcon(QIcon('icons/pause.png'))

    if p2:                          #---------------#---------------#
        s2=files[1]
        playbtn2.setIcon(QIcon('icons/resume.png'))
        truelist.append("p2")
        if truelist[0]!=truelist[1]:
            s=mixer.Sound(s2)
            mixer.Sound.play(s)
            syz=True
            sthread=td.Thread(target=yz)
            sthread.start()
        else:
            mixer.Sound.stop(s)
            truelist.clear()
            playbtn2.setIcon(QIcon('icons/pause.png'))

    if p3:                          #---------------#---------------#
        s3=files[2]
        playbtn3.setIcon(QIcon('icons/resume.png'))
        truelist.append("p3")
        if truelist[0]!=truelist[1]:
            s=mixer.Sound(s3)
            mixer.Sound.play(s)
            syz=True
            sthread=td.Thread(target=yz)
            sthread.start()
        else:
            mixer.Sound.stop(s)
            truelist.clear()
            playbtn3.setIcon(QIcon('icons/pause.png'))
    
    if p4:                          #---------------#---------------#
        s4=files[3]
        playbtn4.setIcon(QIcon('icons/resume.png'))
        truelist.append("p4")
        if truelist[0]!=truelist[1]:
            s=mixer.Sound(s4)
            mixer.Sound.play(s)
            syz=True
            sthread=td.Thread(target=yz)
            sthread.start()
        else:
            mixer.Sound.stop(s)
            truelist.clear()
            playbtn4.setIcon(QIcon('icons/pause.png'))
    
    if p5:                          #---------------#---------------#
        s5=files[4]
        playbtn5.setIcon(QIcon('icons/resume.png'))
        truelist.append("p5")
        if truelist[0]!=truelist[1]:
            s=mixer.Sound(s5)
            mixer.Sound.play(s)
            syz=True
            sthread=td.Thread(target=yz)
            sthread.start()
        else:
            mixer.Sound.stop(s)
            truelist.clear()
            playbtn5.setIcon(QIcon('icons/pause.png'))

    if p6:                          #---------------#---------------#
        s6=files[5]
        playbtn6.setIcon(QIcon('icons/resume.png'))
        truelist.append("p6")
        if truelist[0]!=truelist[1]:
            s=mixer.Sound(s6)
            mixer.Sound.play(s)
            sthread=td.Thread(target=yz)
            sthread.start()
        else:
            mixer.Sound.stop(s)
            truelist.clear()
            playbtn6.setIcon(QIcon('icons/pause.png'))
    
    playbtn1.setChecked(False) 
    playbtn2.setChecked(False) 
    playbtn3.setChecked(False) 
    playbtn4.setChecked(False) 
    playbtn5.setChecked(False) 
    playbtn6.setChecked(False)
    
def display():                  #---------------------------------------------------------------------------------display
    global playbtn1,playbtn2,playbtn3,playbtn4,playbtn5,playbtn6,dsply,flen
    dirctlabel.setText(os.getcwd()+"\\")
    if dsply:
        dirctlabel.setVisible(True)
    else:
        dirctlabel.setVisible(False)
    buttons0()

    
    if flen>=6:                   #---------------#---------------#  
        playbtn1.setEnabled(dsply)
        playbtn2.setEnabled(dsply)
        playbtn3.setEnabled(dsply)
        playbtn4.setEnabled(dsply)
        playbtn5.setEnabled(dsply)
        playbtn6.setEnabled(dsply)
        playbtn1.setVisible(dsply)
        playbtn2.setVisible(dsply)
        playbtn3.setVisible(dsply)
        playbtn4.setVisible(dsply)
        playbtn5.setVisible(dsply)
        playbtn6.setVisible(dsply)

    if flen==5:                     #---------------#---------------#
        playbtn1.setEnabled(dsply)
        playbtn2.setEnabled(dsply)
        playbtn3.setEnabled(dsply)
        playbtn4.setEnabled(dsply)
        playbtn5.setEnabled(dsply)
        playbtn1.setVisible(dsply)
        playbtn2.setVisible(dsply)
        playbtn3.setVisible(dsply)
        playbtn4.setVisible(dsply)
        playbtn5.setVisible(dsply)

    if flen==4:                      #---------------#---------------#
        playbtn1.setEnabled(dsply)
        playbtn2.setEnabled(dsply)
        playbtn3.setEnabled(dsply)
        playbtn4.setEnabled(dsply)
        playbtn1.setVisible(dsply)
        playbtn2.setVisible(dsply)
        playbtn3.setVisible(dsply)
        playbtn4.setVisible(dsply)

    if flen==3:                      #---------------#---------------#
        playbtn1.setEnabled(dsply)
        playbtn2.setEnabled(dsply)
        playbtn3.setEnabled(dsply)
        playbtn1.setVisible(dsply)
        playbtn2.setVisible(dsply)
        playbtn3.setVisible(dsply)

    if flen==2:                      #---------------#---------------#
        playbtn1.setEnabled(dsply)
        playbtn2.setEnabled(dsply)
        playbtn1.setVisible(dsply)
        playbtn2.setVisible(dsply)

    if flen==1:                      #---------------#---------------#
        playbtn1.setEnabled(dsply)
        playbtn1.setVisible(dsply)

def files0():                           #---------------------------------------------------------------------------------files0
    
    global filelabel,files,flen,f,dsply
    files=[]
    f=glob.glob(r"*.wav")
    flen=len(f)

    for i in range(flen):
        files.append(f[-1-i])

    s="\n--------------------------------------\n".join(files)
    filelabel.setText(s)    
    display()


class Window(QWidget):                     #-------------------------------------------------
    def __init__(self):
        super().__init__()
        self.setMaximumSize(344, 498)
        self.setMinimumSize(344, 498)
        self.setWindowTitle("voice recorder")
        global  startbtn,timerlabel,pausebtn,filelabel,voicelabel,newlabel,dirctlabel

        timerlabel = QLabel("00:00:00", self)
        timerlabel.setFont(QFont("calibri", 25))
        timerlabel.setStyleSheet("color:red;")
        timerlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        timerlabel.setGeometry(100, 250, 135, 50)
        timerlabel.setVisible(False)

        backgroundlable=QLabel(self)        #--------------------------------------------------------
        backgroundlable.setGeometry(0, 408, 344, 90)
        backgroundlable.setStyleSheet("background-color:grey")
                                            
        startbtn=QPushButton(self)          #--------------------------------------------------------
        startbtn.setGeometry(145, 425, 51, 51)
        startbtn.setCheckable(True)
        startbtn.setIcon(QIcon('icons/start.png'))
        startbtn.setIconSize(QSize(40,40))
        startbtn.setStyleSheet("background-color:white;border-radius:25")
        startbtn.setShortcut("Return")
        startbtn.clicked.connect(start0)
                                            
        pausebtn=QPushButton(self)          #--------------------------------------------------------
        pausebtn.setGeometry(250, 425, 51, 51)
        pausebtn.setCheckable(True)
        pausebtn.setIcon(QIcon('icons/resume.png'))
        pausebtn.setIconSize(QSize(40,40))
        pausebtn.setStyleSheet("background-color:white;border-radius:25")
        pausebtn.setShortcut("Enter")
        pausebtn.setEnabled(False)
        pausebtn.setVisible(False)
        pausebtn.clicked.connect(pause0)

        voicelabel=QPushButton(self)
        voicelabel.setGeometry(115,100,100,100)
        voicelabel.setIcon(QIcon("icons/mic.png"))
        voicelabel.setIconSize(QSize(80,80))
        voicelabel.setCheckable(True)
        voicelabel.setStyleSheet("background-color:white;border-radius:50;border: 1px solid red")
        voicelabel.setVisible(False)

        filelabel = QLabel("0", self)            #--------------------------------------------------------
        filelabel.setFont(QFont("calibri", 15))
        filelabel.setStyleSheet("color:black")
        filelabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        filelabel.setGeometry(20, 25, 230, 288)
        

        newlabel = QLabel("new", self)            #--------------------------------------------------------newlabel
        newlabel.setFont(QFont("calibri", 10))
        newlabel.setStyleSheet("color:Yellow;background-color:red")
        newlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        newlabel.setGeometry(250, 30, 25, 15)
        newlabel.setVisible(False)

        dirctlabel = QLabel("", self)            #--------------------------------------------------------directoreylabel
        dirctlabel.setFont(QFont("calibri", 10))
        dirctlabel.setStyleSheet("color:grey;")
        dirctlabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        dirctlabel.setGeometry(0, 0, 344, 15)
        dirctlabel.setVisible(True)

        global playbtn1,playbtn2,playbtn3,playbtn4,playbtn5,playbtn6    #--------------------------------------------------------
        playbtn1=QPushButton(self)
        playbtn1.setGeometry(290, 28, 20, 20)
        playbtn1.setCheckable(True)
        playbtn1.setIcon(QIcon('icons/pause.png'))
        playbtn1.setIconSize(QSize(30,30))
        playbtn1.setStyleSheet("background-color:green;border-radius:10")
        playbtn1.setEnabled(False)
        playbtn1.setVisible(False)
        playbtn1.clicked.connect(play0)
 
        playbtn2=QPushButton(self)
        playbtn2.setGeometry(290, 78, 20, 20)
        playbtn2.setCheckable(True)
        playbtn2.setIcon(QIcon('icons/pause.png'))
        playbtn2.setIconSize(QSize(30,30))
        playbtn2.setStyleSheet("background-color:green;border-radius:10")
        playbtn2.setEnabled(False)
        playbtn2.setVisible(False)
        playbtn2.clicked.connect(play0)

        playbtn3=QPushButton(self)
        playbtn3.setGeometry(290, 128, 20, 20)
        playbtn3.setCheckable(True)
        playbtn3.setIcon(QIcon('icons/pause.png'))
        playbtn3.setIconSize(QSize(30,30))
        playbtn3.setStyleSheet("background-color:green;border-radius:10")
        playbtn3.setEnabled(False)
        playbtn3.setVisible(False)
        playbtn3.clicked.connect(play0)

        playbtn4=QPushButton(self)
        playbtn4.setGeometry(290, 178, 20, 20)
        playbtn4.setCheckable(True)
        playbtn4.setIcon(QIcon('icons/pause.png'))
        playbtn4.setIconSize(QSize(30,30))
        playbtn4.setStyleSheet("background-color:green;border-radius:10")
        playbtn4.setEnabled(False)
        playbtn4.setVisible(False)
        playbtn4.clicked.connect(play0)

        playbtn5=QPushButton(self)
        playbtn5.setGeometry(290, 228, 20, 20)
        playbtn5.setCheckable(True)
        playbtn5.setIcon(QIcon('icons/pause.png'))
        playbtn5.setIconSize(QSize(30,30))
        playbtn5.setStyleSheet("background-color:green;border-radius:10")
        playbtn5.setEnabled(False)
        playbtn5.setVisible(False)
        playbtn5.clicked.connect(play0)

        playbtn6=QPushButton(self)
        playbtn6.setGeometry(290, 278, 20, 20)
        playbtn6.setCheckable(True)
        playbtn6.setIcon(QIcon('icons/pause.png'))
        playbtn6.setIconSize(QSize(30,30))
        playbtn6.setStyleSheet("background-color:green;border-radius:10")
        playbtn6.setEnabled(False)
        playbtn6.setVisible(False)
        playbtn6.clicked.connect(play0)

app = QApplication(sys.argv)#---------------------------------------------------------------------------------
window = Window()
window.show()
dsply=True
truelist=[]
files0()
os.system('cls')
sys.exit(app.exec())