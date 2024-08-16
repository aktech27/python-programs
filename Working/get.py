from support import alarm
from tkinter import *
from datetime import datetime
import time

class Watch:
    def __init__(self):
        HH,MM,SS=0,0,0
        
    def display(self,root,l):
        root.geometry('500x500')
        l.destroy()
        l=Label(root,text=(datetime.now()).strftime("%I:%M:%S"))
        l.pack()        
        root.after(1000,lambda:w.display(root,l))
        root.mainloop()
        
w=Watch()
root=Tk()
w.display(root,Label())

