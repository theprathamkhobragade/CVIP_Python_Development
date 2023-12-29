from tkinter import *
import random
import tkinter

root = Tk()
root.title('Typing Speed Test')
start=False


#       -------------------------window dimensions----------------------------
# root.geometry('800x350')
root.minsize(800,350)
root.maxsize(800,350)
timelabel=True
#       -------------------------window widgets----------------------------
def resetWritingLabels():
    global text,timelabel,enter,res,ps
    ps=False
    res=False
    enter=False
    file = open("love.txt", "r")
    text = random.choice(file.read().split("\n"))

    global name#------------------------------------------------------------heding
    name = Label(root, text="Typing Speed Test", fg='black',font=('Calibri',25))
    name.place(relx=0.5, rely=0.15, anchor=S)

    global anykey                               #--------------------------------------------------typing starts by pressing any key
    anykey = Label(root,text="Enter any key", fg='blue',font=('Calibri',15),height=1,width=12)
    anykey.place(relx=0.5, rely=0.25, anchor=CENTER)

    global timelefts
    timelefts = Label(root)

    global typedlabel#------------------------------------------------------------typed letters 
    typedlabel = Label(root, text=text[0:0], fg='green',font=('Calibri',18))
    typedlabel.place(relx=0.505, rely=0.4, anchor=E)
    
    global remaininglabel#------------------------------------------------------------remaining untyped words
    remaininglabel = Label(root, text=text[0:],font=('Calibri',18))
    remaininglabel.place(relx=0.5, rely=0.4, anchor=W)

    global letterlabel#------------------------------------------------------------letter to be typed
    letterlabel = Label(root, text=text[0], fg='black',font=('Calibri',18))
    letterlabel.place(relx=0.5, rely=0.5, anchor=N)

    global tag#------------------------------------------------------------signature name
    tag = Label(root, text="theprathamkhobragade", fg='black',font=('Calibri',12))
    tag.place(relx=1, rely=1,anchor=SE)
    

    # root.after(1000, addSecond)
    root.bind('<Key>', keyPress)


def addSecond():
    global passedSeconds
    passedSeconds -= 1             #---------------------------------------------seconds  counter with color
    try:
        if(passedSeconds<50):
            timelefts.configure(text=f"{passedSeconds} Seconds",fg=rgbc((51, 255, 0)))
        if(passedSeconds<40):
            timelefts.configure(text=f"{passedSeconds} Seconds",fg=rgbc((44, 240, 10)))
        if(passedSeconds<30):
            timelefts.configure(text=f"{passedSeconds} Seconds",fg=rgbc((133, 240, 10)))
        if(passedSeconds<20):
            timelefts.configure(text=f"{passedSeconds} Seconds",fg=rgbc((240, 167, 10)))
        if(passedSeconds<10):
            timelefts.configure(text=f"{passedSeconds} Seconds",fg='red')
        else:
            timelefts.configure(text=f"{passedSeconds} Seconds")    
    except tkinter.TclError:
        pass
    if(passedSeconds==0):
        root.after(1000,stopTest)
    if timelabel:                           #---------------------------------------------seconds  count per seconds
        root.after(1000, addSecond)

def stopTest():
    global timelabel,enter,res,ps
    enter=False
    timelabel = False                        #---------------------------------------------totoal  wpm
    wpm = len(typedlabel.cget('text'))/5
    wpm=int(wpm)
    ps=True
                            #---------------------------------------------Destroy all labels.
    resbtn.destroy()
    pausebtn.destroy()
    timelefts.destroy()
    letterlabel.destroy()
    remaininglabel.destroy()
    typedlabel.destroy()
    root.unbind_all('<key>')

    if res==False:
                                #---------------------------------------------display result.
        global resultlabel
        resultlabel = Label(root, text=f'WPM: {wpm}', fg='black',font=('Calibri',18))
        resultlabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        
                                #---------------------------------------------retry button.
        global restartbutton
        restartbutton = Button(text="Restart", fg='White',font=('Calibri',18),bg = "red", bd=2,command=restart)
        restartbutton.place(relx=0.5, rely=0.6, anchor=CENTER)
    else:
        pass
    

def restart():#---------------------------------------------restarts on result screen
    global ps
    ps=False                       
    resultlabel.destroy() #---------------------------------------------Destroy result labels.
    restartbutton.destroy()
    resetWritingLabels()

def onrestart():                            #---------------------------------------------restarts on typing scrreeen
    global ps,res,timelabel
    timelabel = False
    ps=False
    res=True
    stopTest()
    resetWritingLabels()

def onpause():                           #---------------------------------------------pause on typing scrreeen
    global ps,timelabel
    if ps==True:
        ps=False
        timelabel = True
        root.after(1000, addSecond)

    else:
        ps=True
        timelabel = False


def keyPress(event):
    global enter,timelabel,passedSeconds,timelefts,resbtn,pausebtn
    key = event
    if enter and (ps==False):
        starts(key)

    elif key and (ps==False):
    # if key.keysym=="Return":
        enter=True
        timelabel=True
        passedSeconds=60
        root.after(1000, addSecond)
        anykey.destroy()
        
        timelefts = Label(root, text=f'60 Seconds', fg='green',font=('Calibri',20))#--------------------timer
        timelefts.place(relx=0.5, rely=0.2, anchor=N)

        resbtn = Button(root, text="Restart", fg='White',font=('Calibri',10),bg = "red", bd=2,command=onrestart)#--------------------restart btn on typing screen
        resbtn.place(relx=1, rely=0, anchor=NE)

        pausebtn = Button(root, text="Pause", fg='White',font=('Calibri',10),bg = "red", bd=2,command=onpause)#--------------------pause btn on typing scren
        pausebtn.place(relx=0.932, rely=0, anchor=NE)
        

def starts(key):#--------------------------------------------------pressed keyboard keys
    try:
        if(len(remaininglabel.cget("text"))!=0):
            if key.char==remaininglabel.cget("text")[0]:
                typedlabel.configure(text=typedlabel.cget('text') + key.char)
                    
                remaininglabel.configure(text=remaininglabel.cget('text')[1:])
                if(len(remaininglabel.cget("text"))!=0):
                    if remaininglabel.cget('text')[0]==" ":
                        letterlabel.configure(text="space")
                    else:
                        letterlabel.configure(text=remaininglabel.cget('text')[0],fg='black')
                else:  
                    root.after(1000,stopTest)

            else:
                    if(key.keysym =="Shift_L" or key.keysym=="Shift_R" or key.keysym=="Caps_lock" ):
                        pass           
                    else:
                        if remaininglabel.cget('text')[0]==" ":
                            letterlabel.configure(text="space",fg='red')
                        else:
                            letterlabel.configure(text=remaininglabel.cget('text')[0],fg='red')
                                             
    except tkinter.TclError:
        pass

def rgbc(rgb):              #---------------------------------------------translate rgb value to color
    return "#%02x%02x%02x" % rgb   


                            #---------------------------------------------starts from here.
if __name__=='__main__':
    resetWritingLabels()
    root.mainloop()