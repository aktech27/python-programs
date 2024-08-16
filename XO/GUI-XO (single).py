from tkinter import *
from tkinter import messagebox
import time
i=1    
class program:
    u_timer=0
    v_timer=0
    
    def loader(self):
        ld=Tk()
        ld.title('Loading')
        ld.geometry('500x500')
        loc=r'xo.png'
        img=PhotoImage(file=loc)
        l=Label(ld,image=img)
        l.place(x=0,y=0)
        ld.after(3000,lambda:ld.destroy())
        ld.mainloop()

    
    def intro(self):
        ak=Tk()
        ak.title('Ahamed Kabeer')
        ak.geometry('515x508')
        loc=r'Logo2.png'
        img=PhotoImage(file=loc)
        l=Label(ak,image=img)
        l.place(x=0,y=0)
        ak.after(3000,lambda:ak.destroy())
        ak.mainloop()

    def main(self):    
        global i
        program.u_timer=time.time()
        root=Tk()
        root.geometry('600x550')
        root.title('XO-GAME')
        l=Label(root,text='\n\n\t\t       \n')
        l.grid(row=0,column=0)
        loc=r'watermark2.png'
        wmark=PhotoImage(file=loc)

        def process(b):            
            global i

            def checkwin():
                global i
                
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
                        obj.main()
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
                     program.v_timer=time.time()
                     now=program.v_timer-program.u_timer
                     messagebox.showinfo('GAME OVER','O WINS\nTime taken:%.2f seconds'%now)
                     ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
                     if(ans=='yes'):
                        i=1
                        root.destroy()
                        obj.main()
                     elif(ans=='no'):
                        root.destroy()
                        sys.exit()

                if(i>=10):
                        program.v_timer=time.time()
                        now=program.v_timer-program.u_timer
                        messagebox.showinfo('GAME OVER','TIE GAME\nTime taken:%.2f seconds'%now)
                        ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
                        if(ans=='yes'):
                            i=1
                            root.destroy()
                            obj.main()
                        elif(ans=='no'):
                            root.destroy()
                            sys.exit()

            def pcturn():
                global i
                if(i%2==0):

                    #try to win moves....
                    
                    if((b2['text']==b3['text']=='O' or b4['text']==b7['text']=='O' or b5['text']==b9['text']=='O')and b1['text']==''):
                        b1['text']='O'
                        b1['fg']='blue'

                    elif((b1['text']==b3['text']=='O' or b5['text']==b8['text']=='O')and b2['text']==''):
                        b2['text']='O'
                        b2['fg']='blue'

                    elif((b1['text']==b2['text']=='O' or b5['text']==b7['text']=='O' or b6['text']==b9['text']=='O')and b3['text']==''):
                        b3['text']='O'
                        b3['fg']='blue'
                    
                    elif((b1['text']==b7['text']=='O' or b5['text']==b6['text']=='O')and b4['text']==''):
                        b4['text']='O'
                        b4['fg']='blue'

                    elif((b2['text']==b8['text']=='O' or b3['text']==b7['text']=='O' or b4['text']==b6['text']=='O' or b1['text']==b9['text']=='O')and b5['text']==''):
                        b5['text']='O'
                        b5['fg']='blue'

                    elif((b3['text']==b7['text']=='O' or b4['text']==b5['text']=='O')and b6['text']==''):
                        b6['text']='O'
                        b6['fg']='blue'
                    
                    elif((b1['text']==b4['text']=='O' or b3['text']==b5['text']=='O' or b8['text']==b9['text']=='O')and b7['text']==''):
                        b7['text']='O'
                        b7['fg']='blue'

                    elif((b2['text']==b5['text']=='O' or b7['text']==b9['text']=='O')and b8['text']==''):
                        b8['text']='O'
                        b8['fg']='blue'

                    elif((b1['text']==b5['text']=='O' or b3['text']==b6['text']=='O' or b7['text']==b8['text']=='O')and b9['text']==''):
                        b9['text']='O'
                        b9['fg']='blue'


                    #defence moves.....

                        
                    elif((b2['text']==b3['text']=='X' or b4['text']==b7['text']=='X' or b5['text']==b9['text']=='X')and b1['text']==''):
                        b1['text']='O'
                        b1['fg']='blue'

                    elif((b1['text']==b3['text']=='X' or b5['text']==b8['text']=='X')and b2['text']==''):
                        b2['text']='O'
                        b2['fg']='blue'

                    elif((b1['text']==b2['text']=='X' or b5['text']==b7['text']=='X' or b6['text']==b9['text']=='X')and b3['text']==''):
                        b3['text']='O'
                        b3['fg']='blue'
                    
                    elif((b1['text']==b7['text']=='X' or b5['text']==b6['text']=='X')and b4['text']==''):
                        b4['text']='O'
                        b4['fg']='blue'

                    elif((b2['text']==b8['text']=='X' or b3['text']==b7['text']=='X' or b4['text']==b6['text']=='X' or b1['text']==b9['text']=='X')and b5['text']==''):
                        b5['text']='O'
                        b5['fg']='blue'

                    elif((b3['text']==b9['text']=='X' or b4['text']==b5['text']=='X')and b6['text']==''):
                        b6['text']='O'
                        b6['fg']='blue'
                    
                    elif((b1['text']==b4['text']=='X' or b3['text']==b5['text']=='X' or b8['text']==b9['text']=='X')and b7['text']==''):
                        b7['text']='O'
                        b7['fg']='blue'

                    elif((b2['text']==b5['text']=='X' or b7['text']==b9['text']=='X')and b8['text']==''):
                        b8['text']='O'
                        b8['fg']='blue'

                    elif((b1['text']==b5['text']=='X' or b3['text']==b6['text']=='X' or b7['text']==b8['text']=='X')and b9['text']==''):
                        b9['text']='O'
                        b9['fg']='blue'

                    #basic moves.....    

                    elif(b5['text']==''):
                        b5['text']='O'
                        b5['fg']='blue'

                    elif(b1['text']==''):
                        b1['text']='O'
                        b1['fg']='blue'

                    elif(b3['text']==''):
                        b3['text']='O'
                        b3['fg']='blue'
                        

                    elif(b7['text']==''):
                        b7['text']='O'
                        b7['fg']='blue'

                    elif(b9['text']==''):
                        b9['text']='O'
                        b9['fg']='blue'    
                i=i+1
                checkwin()

                
            def esypcturn():
                global i
                if(i%2==0):
                    if(b1['text']==''):
                        b1['text']='O'
                        b1['fg']='blue'
                        

                    elif(b2['text']==''):
                        b2['text']='O'
                        b2['fg']='blue'
                        

                    elif(b3['text']==''):
                        b3['text']='O'
                        b3['fg']='blue'
                        
                        
                    elif(b4['text']==''):
                        b4['text']='O'
                        b4['fg']='blue'
                        

                    elif(b5['text']==''):
                        b5['text']='O'
                        b5['fg']='blue'
                        

                    elif(b6['text']==''):
                        b6['text']='O'
                        b6['fg']='blue'

                    elif(b7['text']==''):
                        b7['text']='O'
                        b7['fg']='blue'
                        

                    elif(b8['text']==''):
                        b8['text']='O'
                        b8['fg']='blue'
                        

                    elif(b9['text']==''):
                        b9['text']='O'
                        b9['fg']='blue'
    

                i=i+1
                checkwin()
                    

            if(i%2==1):
                if(b['text']==''):
                 b['text']='X'
                 b['fg']='red'
                 i=i+1
                 checkwin()
                 root.after(300,lambda:pcturn())
                elif(b['text']=='X' or b['text']=='O'):
                 messagebox.showinfo('ERROR','Invalid move by player 1.TRY AGAIN')
                 

            

                    
            
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

obj=program()
obj.intro()
obj.loader()
obj.main()


