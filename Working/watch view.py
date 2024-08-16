from support import alarm
from tkinter import *
from datetime import datetime
import time
import os
import sys

##Incresing recursion limit.Default is around 1010 when I tested...........
sys.setrecursionlimit(1000000)

                                            #<----- S T O P   W A T C H ----->#
class StopWatch:
    def __init__(self):
        self.state=""
        self.light_count,self.color_count=0,0
        self.lcolour="blue"
        self.light_state="DISCO"
        self.MM,self.SS,self.MS=0,0,0
        self.count=0    ## to avoid  multiple start() call,which increases the speed of timer 

    def changestate(self):
        self.light_state="NORMAL"
        w.lightcolor()
            
    def lightcolor(self):
        self.color_count+=1
        if self.color_count==1:
            self.lcolour="blue"
        elif self.color_count==2:
            self.lcolour="green"
        elif self.color_count==3:
            self.lcolour="red"
        elif self.color_count==4:
            self.lcolour="yellow"
        elif self.color_count==5:
            self.lcolour="orange"    
        else:
            self.color_count,self.light_state=0,"DISCO"
            
            
    def light(self,root,*l1):
        w.STATE="STOPWATCH"
        if(w.STATE=="STOPWATCH"):
            for l in l1:
                l.destroy()

            l1=Label(root,text=('{:0>2}'.format(self.MM)+":"+'{:0>2}'.format(self.MM)),font=('Lucida',46,'bold'),fg=self.lcolour,bg="#9AB8A3")
            l1.place(x=160,y=360)
            l2=Label(root,text='{:0>2}'.format(self.MS),font=('Lucida',34,'bold'),fg=self.lcolour,bg="#9AB8A3")
            l2.place(x=320,y=410)
            b1=Button(root,text="Light",command=lambda:sw.light(root,l1,l2))
            b1.place(x=10,y=10)
            b2=Button(root,text="Change",command=lambda:sw.changestate())
            b2.place(x=10,y=50)
            root.after(1000,lambda:sw.stopwatch(root,l1,l2))
        
        if(self.light_count<=60):
            if(self.light_state=="DISCO"):
                sw.lightcolor()
            root.after(50,lambda:sw.light(root,l1,l2))
        else:
            self.light_count=0
            root.after(1,lambda:sw.display(root,l1,l2))
            
    def reset(self,root,l1,l2):
        self.state=""
        l1.destroy()
        l2.destroy()
        self.MM,self.SS,self.MS=0,0,0
        l1=Label(root,text=('{:0>2}'.format(self.MM)+":"+'{:0>2}'.format(self.SS)),font=('Lucida',46,'bold'),fg="black",bg="#9AB8A3")
        l1.place(x=160,y=360)
        l2=Label(root,text='{:0<2}'.format(self.MS),font=('Lucida',34,'bold'),fg="black",bg="#9AB8A3")
        l2.place(x=320,y=410)
        
    def pause(self,root,l1,l2):
        l1.destroy()
        l2.destroy()
        self.state="PAUSE"
        self.count=0
        l1=Label(root,text=('{:0>2}'.format(self.MM)+":"+'{:0>2}'.format(self.SS)),font=('Lucida',46,'bold'),fg="black",bg="#9AB8A3")
        l1.place(x=160,y=360)
        l2=Label(root,text='{:0<2}'.format(self.MS),font=('Lucida',34,'bold'),fg="black",bg="#9AB8A3")
        l2.place(x=320,y=410)    
        
    def start(self,root,l1,l2):
        self.state="START"
        self.count+=1
        if(self.count==1):
            self.incrementor(root,l1,l2)

    def set(self,root,l1,l2):
        if self.state=="START":
            sw.pause(root,l1,l2)
            self.state="PAUSE"
        elif self.state=="PAUSE" or self.state=="":
            sw.start(root,l1,l2)
            self.state="START"
        
    def incrementor(self,root,l1,l2):
        l1.destroy()
        l2.destroy()
        if(self.state=="START"):
            self.MS+=1
            if(int(self.MS)==10):
                self.SS+=1
                self.MS=0
            if(int(self.SS)==60):
                self.MM+=1
                self.SS=0
            l1=Label(root,text=('{:0>2}'.format(self.MM)+":"+'{:0>2}'.format(self.SS)),font=('Lucida',46,'bold'),fg="black",bg="#9AB8A3")
            l1.place(x=160,y=360)
            l2=Label(root,text='{:0<2}'.format(self.MS),font=('Lucida',34,'bold'),fg="black",bg="#9AB8A3")
            l2.place(x=320,y=410)
            root.after(99,lambda:sw.incrementor(root,l1,l2))
            
    def stopwatch(self,root,*l1):
        w.STATE="STOPWATCH"
        if(w.STATE=="STOPWATCH"):
            for l in l1:
                l.destroy()

            l1=Label(root,text=('{:0>2}'.format(self.MM)+":"+'{:0>2}'.format(self.SS)),font=('Lucida',46,'bold'),fg="black",bg="#9AB8A3")
            l1.place(x=160,y=360)
            l2=Label(root,text='{:0<2}'.format(self.MS),font=('Lucida',34,'bold'),fg="black",bg="#9AB8A3")
            l2.place(x=320,y=410)
            b1=Button(root,text="Light",command=lambda:sw.light(root,l1,l2))
            b1.place(x=10,y=10)
            b2=Button(root,text="Change",command=lambda:sw.changestate())
            b2.place(x=10,y=50)
            b3=Button(root,text="Set",command=lambda:sw.set(root,l1,l2))
            b3.place(x=10,y=400)
            b4=Button(root,text="Reset",command=lambda:sw.reset(root,l1,l2))
            b4.place(x=10,y=450)
            root.after(1000,lambda:sw.stopwatch(root,l1,l2))


                                                #<----- T I M E   W A T C H ----->#


class Watch:
    def __init__(self):
        self.light_count,self.color_count=0,0
        self.lcolour="blue"
        self.light_state="DISCO"
        self.STATE="WATCH"

    def changestate(self):
        self.light_state="NORMAL"
        w.lightcolor()
            
    def lightcolor(self):
        self.color_count+=1
        if self.color_count==1:
            self.lcolour="blue"
        elif self.color_count==2:
            self.lcolour="green"
        elif self.color_count==3:
            self.lcolour="red"
        elif self.color_count==4:
            self.lcolour="yellow"
        elif self.color_count==5:
            self.lcolour="orange"    
        else:
            self.color_count,self.light_state=0,"DISCO"
            
            
    def light(self,root,*l1):
        for l in l1:
            l.destroy()
        self.light_count+=1    
        l1=Label(root,text=(datetime.now()).strftime("%#I:%M"),font=('Lucida',46,'bold'),fg=self.lcolour,bg="#9AB8A3")
        l1.place(x=160,y=360)
        l2=Label(root,text=(datetime.now()).strftime("%S"),font=('Lucida',34,'bold'),fg=self.lcolour,bg="#9AB8A3")
        l2.place(x=320,y=410)
        l3=Label(root,text=(datetime.now()).strftime("%p"),font=('Lucida',15,'bold'),fg=self.lcolour,bg="#9AB8A3")
        l3.place(x=130,y=350)
        b1=Button(root,text="Light",command=lambda:w.light(root,l1,l2,l3))
        b1.place(x=10,y=10)
       
        if(self.light_count<=60):
            if(self.light_state=="DISCO"):
                w.lightcolor()
            root.after(50,lambda:w.light(root,l1,l2,l3))
        else:
            self.light_count=0
            root.after(1,lambda:w.display(root,l1,l2,l3))
        
        
    def display(self,root,*l1):
        if self.STATE=="WATCH":
            for l in l1:
                l.destroy()
            root.geometry('600x600')
            
            layout=PhotoImage(file=(os.getcwd()+"\support\layout.png"))
            base=Canvas(root,height=600,width=600)
            base.create_image(300,300,image=layout)
            base.place(x=0,y=0)
            
            l1=Label(root,text=(datetime.now()).strftime("%#I:%M"),font=('Lucida',46,'bold'),fg="black",bg="#9AB8A3")
            l1.place(x=160,y=360)
            l2=Label(root,text=(datetime.now()).strftime("%S"),font=('Lucida',34,'bold'),fg="black",bg="#9AB8A3")
            l2.place(x=320,y=410)
            l3=Label(root,text=(datetime.now()).strftime("%p"),font=('Lucida',15,'bold'),fg="black",bg="#9AB8A3")
            l3.place(x=130,y=350)
            b1=Button(root,text="Light",command=lambda:w.light(root,l1,l2,l3))
            b1.place(x=10,y=10)
            b2=Button(root,text="Change",command=lambda:w.changestate())
            b2.place(x=10,y=50)
            b3=Button(root,text="Mode",command=lambda:sw.stopwatch(root,l1,l2,l3,b1,b2,b3))
            b3.place(x=500,y=50)
            
            root.after(1000,lambda:w.display(root,l1,l2,l3))
            root.mainloop()
        
        
        
w=Watch()
sw=StopWatch()
root=Tk()
w.display(root,Label())
