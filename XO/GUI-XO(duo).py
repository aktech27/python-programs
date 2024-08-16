from tkinter import *
from time import *
from os import *
from tkinter import messagebox
i=1
def main():
    global i
    root=Tk()
    root.geometry('600x550')
    root.title('XO-GAME')
    l=Label(root,text='\n\n\t\t       \n')
    l.grid(row=0,column=0)
    loc=r'watermark2.png'
    wmark=PhotoImage(file=loc)

    def process(b):
        global i
        if(i%2==1):
            if(b['text']==''):
             b['text']='X'
             b['fg']='red'
             i=i+1
            elif(b['text']=='X' or b['text']=='O'):
             messagebox.showinfo('ERROR','Invalid move by player 1.TRY AGAIN')   
        elif(i%2==0):
            if(b['text']==''):
             b['text']='O'
             b['fg']='blue'
             i=i+1
            elif(b['text']=='X' or b['text']=='O'):
              messagebox.showinfo('ERROR','Invalid move by player 2.TRY AGAIN')
             
        if(b1['text']==b2['text']==b3['text']=='X' or
           b4['text']==b5['text']==b6['text']=='X' or
           b7['text']==b8['text']==b9['text']=='X' or
           b1['text']==b4['text']==b7['text']=='X' or
           b2['text']==b5['text']==b8['text']=='X' or
           b3['text']==b6['text']==b9['text']=='X' or
           b1['text']==b5['text']==b9['text']=='X' or
           b3['text']==b5['text']==b7['text']=='X'):        
            messagebox.showinfo('GAME OVER','X WINS')
            ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
            if(ans=='yes'):
                i=1
                root.destroy()
                main()
            elif(ans=='no'):
                root.destroy()
                sys.exit()

        if(b1['text']==b2['text']==b3['text']=='O' or
           b4['text']==b5['text']==b6['text']=='O' or
          b7['text']==b8['text']==b9['text']=='O' or
          b1['text']==b4['text']==b7['text']=='O' or
          b2['text']==b5['text']==b8['text']=='O' or
          b3['text']==b6['text']==b9['text']=='O' or
          b1['text']==b5['text']==b9['text']=='O' or
          b3['text']==b5['text']==b7['text']=='O'):
             messagebox.showinfo('GAME OVER','O WINS')
             ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
             if(ans=='yes'):
                i=1
                root.destroy()
                main()
             elif(ans=='no'):
                root.destroy()
                sys.exit()

        if(i>=10):
                messagebox.showinfo('GAME OVER','TIE GAME')
                ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
                if(ans=='yes'):
                    i=1
                    root.destroy()
                    main()
                elif(ans=='no'):
                    root.destroy()
                    sys.exit()


                
        
    b1=Button(root,text='',font=('Algerian','20'),height=3,width=6,bg='white',fg='black',command=lambda:process(b1))
    b1.grid(row=1,column=1)
    b2=Button(root,text='',font=('Algerian','20'),height=3,width=6,bg='white',fg='black',command=lambda:process(b2))
    b2.grid(row=1,column=2)
    b3=Button(root,text='',font=('Algerian','20'),height=3,width=6,bg='white',fg='black',command=lambda:process(b3))
    b3.grid(row=1,column=3)
    b4=Button(root,text='',font=('Algerian','20'),height=3,width=6,bg='white',fg='black',command=lambda:process(b4))
    b4.grid(row=2,column=1)
    b5=Button(root,text='',font=('Algerian','20'),height=3,width=6,bg='white',fg='black',command=lambda:process(b5))
    b5.grid(row=2,column=2)
    b6=Button(root,text='',font=('Algerian','20'),height=3,width=6,bg='white',fg='black',command=lambda:process(b6))
    b6.grid(row=2,column=3)
    b7=Button(root,text='',font=('Algerian','20'),height=3,width=6,bg='white',fg='black',command=lambda:process(b7))
    b7.grid(row=3,column=1)
    b8=Button(root,text='',font=('Algerian','20'),height=3,width=6,bg='white',fg='black',command=lambda:process(b8))
    b8.grid(row=3,column=2)
    b9=Button(root,text='',font=('Algerian','20'),height=3,width=6,bg='white',fg='black',command=lambda:process(b9))
    b9.grid(row=3,column=3)
    gap=Label(root,text='\n\n\n\n\t        ')
    gap.grid(row=4,column=4)
    w1=Label(root,image=wmark)
    w1.grid(row=5,column=5)
    root.mainloop()

def loader():
        ld=Tk()
        ld.title('Loading')
        ld.geometry('500x500')
        loc=r'xo2.png'
        img=PhotoImage(file=loc)
        l=Label(ld,image=img)
        l.place(x=0,y=0)
        ld.after(3000,lambda:ld.destroy())
        ld.mainloop()


def gintro():
    ak=Tk()
    ak.title('Ahamed Kabeer')
    ak.geometry('515x508')
    loc=r'Logo2.png'
    img=PhotoImage(file=loc)
    l=Label(ak,image=img)
    l.place(x=0,y=0)
    ak.after(5000,lambda:ak.destroy())
    ak.mainloop()
    
gintro()
loader()
main()












