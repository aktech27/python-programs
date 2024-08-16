from tkinter.colorchooser import *
from tkinter import *

def choose():
    chosen=askcolor()
    l1v['text']=chosen[1]
    l5['bg']=chosen[1]
    l2v['text']='{:.2f}'.format(chosen[0][0])
    l3v['text']='{:.2f}'.format(chosen[0][1])
    l4v['text']='{:.2f}'.format(chosen[0][2])
    
root=Tk()
root.geometry('360x500')
root.title('AKTECH-Coding Noob')
C=Canvas(root,bg='black',height=500,width=360)
C.place(x=0,y=0)
L=Label(root,text='COLOR CHOOSER',bg='black',fg='yellow',font=('Times',24,'bold'))
L.place(x=40,y=10)

b1=Button(root,text='Click Here',bg='white',font=('Times',24),command=lambda:choose())
b1.place(x=100,y=400)

l1=Label(root,text='HEX-CODE:',bg='black',fg='white',font=('Times',20))
l1.place(x=10,y=100)
l1v=Label(root,text='',bg='white',width=10,font=('Times',20))
l1v.place(x=170,y=100)

l2=Label(root,text='R:',bg='black',fg='red',font=('Times',20))
l2.place(x=10,y=170)
l2v=Label(root,text='',fg='red',bg='white',width=5,font=('Times',20))
l2v.place(x=40,y=170)

l3=Label(root,text='G:',bg='black',fg='green',font=('Times',20))
l3.place(x=130,y=170)
l3v=Label(root,text='',fg='green',bg='white',width=5,font=('Times',20))
l3v.place(x=160,y=170)

l4=Label(root,text='B:',bg='black',fg='blue',font=('Times',20))
l4.place(x=240,y=170)
l4v=Label(root,text='',fg='blue',bg='white',width=5,font=('Times',20))
l4v.place(x=270,y=170)

l5=Label(root,bg='black',height=5,width=10)
l5.place(x=130,y=280)

root.mainloop()
