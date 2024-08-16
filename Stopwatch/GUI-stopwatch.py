import time
import os
from tkinter import *

class Timer:
    def __init__(self):
        self.HH,self.MM,self.SS,self.current=0,0,0,'00:00:00'
        self.state="STOP"
        self.count=0 ## to avoid  multiple start() call,which increases the speed of timer 

    def stop(self,l,root):
        self.__init__()
        l['text']=self.current
        
    def pause(self,l,root):
        self.state="PAUSE"
        self.count=0
        l['text']=self.current    
        
    def start(self,l,root):
        self.state="START"
        self.count+=1
        if(self.count==1):
            self.incrementor(l,root)
        
    def incrementor(self,l,root):
        if(self.state=="START"):
            self.SS+=1
            if(int(self.SS)==60):
                self.MM+=1
                self.SS=0
            if(int(self.MM)==60):
                self.HH+=1
                self.MM=0
            self.current='{:0>2}'.format(self.HH)+":"+'{:0>2}'.format(self.MM)+":"+'{:0>2}'.format(self.SS)    
            l['text']=self.current    
            root.after(1000,lambda:self.incrementor(l,root))
            
    def show(self):
        root=Tk()
        root.title('AK-TECH 27')
        root.geometry('200x200')
        l=Label(root,text=self.current,bg='white',font=('Lucida',24,'bold'))
        l.place(x=30,y=20)
        b1=Button(root,text='Start',command=lambda:self.start(l,root))
        b1.place(x=30,y=100)
        b2=Button(root,text='Pause',command=lambda:self.pause(l,root))
        b2.place(x=80,y=100)
        b3=Button(root,text='Stop',command=lambda:self.stop(l,root))
        b3.place(x=130,y=100)
        root.mainloop()
            
t=Timer()
t.show()
