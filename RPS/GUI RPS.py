from tkinter import *
from random import *
sysscore=0
usscore=0

def actual():
    global sysscore
    global usscore
    loc=r'tournament.png'
    stone=r'stone.png'
    paper=r'paper.png'
    srs=r'srs.png'
    bg=r'bg.png'
    rules=r'rules.png'
    null=r'null.png'
    wm=r'watermark2.png'
    

    def game(rule):
        def check(l3,l4):
            global sysscore,usscore
            from tkinter import messagebox
            if(l3['text']==7):
                messagebox.showinfo('GAME OVER','YOU LOST')
                answer=messagebox.askquestion('It is not over yet','BETTER LUCK NEXT TIME.\nWanna play again?')
                if(answer=='yes'):
                    sysscore=0
                    usscore=0
                    main.destroy()
                    actual()
                else:
                    import sys
                    main.destroy()
                    sys.exit()    
                    
            if(l4['text']==7):
                messagebox.showinfo('GAME OVER','YOU WON')
                answer=messagebox.askquestion('It is not over yet','WINNER WINNER CHICKEN DINNER.\nWanna play again?')
                if(answer=='yes'):
                    sysscore=0
                    usscore=0
                    main.destroy()
                    actual()
                else:
                    import sys
                    main.destroy()
                    sys.exit()
                
        def process(ch):
            global sysscore,usscore

            imglst=[img3,img4,img5]
            sysmove=choice(imglst)
            if(ch==1):
                l5['image']=img3
                l6['image']=sysmove
                if(img3==sysmove):
                   l8['text']="IT IS A TIE MOVE."
                   l8['fg']='black'
                elif(sysmove==img4):
                   l8['text']="SYSTEM SCORED."
                   l8['fg']='red'
                   sysscore=sysscore+1
                   l3['text']=sysscore
                   check(l3,l4)
                else:
                   l8['text']="YOU SCORED."
                   l8['fg']='black'
                   usscore=usscore+1
                   l4['text']=usscore
                   check(l3,l4)

            if(ch==2):
                l5['image']=img4
                l6['image']=sysmove
                if(img4==sysmove):
                   l8['text']="IT IS A TIE MOVE."
                   l8['fg']='black'
                elif(sysmove==img5):
                   l8['text']="SYSTEM SCORED."
                   l8['fg']='red'
                   sysscore=sysscore+1
                   l3['text']=sysscore
                   check(l3,l4)
                else:
                   l8['text']="YOU SCORED."
                   l8['fg']='black'
                   usscore=usscore+1
                   l4['text']=usscore
                   check(l3,l4)



                
            if(ch==3):
                l5['image']=img5
                l6['image']=sysmove
                if(img5==sysmove):
                   l8['text']="IT IS A TIE MOVE."
                   l8['fg']='black'
                elif(sysmove==img3):
                   l8['text']="SYSTEM SCORED."
                   l8['fg']='red'
                   sysscore=sysscore+1
                   l3['text']=sysscore
                   check(l3,l4)
                else:
                   l8['text']="YOU SCORED."
                   l8['fg']='black'
                   usscore=usscore+1
                   l4['text']=usscore
                   check(l3,l4)



                
                
            
       
        rule.destroy()
        main=Tk()
        main.geometry('600x600')
        main.title("RPS ROUTLETTE")
        
        img1=PhotoImage(file=bg)
        img2=PhotoImage(file=null)
        imgg2=PhotoImage(file=null)
        img3=PhotoImage(file=stone)
        img4=PhotoImage(file=paper)
        img5=PhotoImage(file=srs)
        img6=PhotoImage(file=wm)
        
        c1=Canvas(width=620,height=620,bg='black')
        c1.place(x=0,y=0)
        c1.create_image(0,0,image=img1,anchor=NW)
        l1=Label(text='SYSTEM',font=('Times','18'),bg='black',fg='yellow')
        l1.place(x=110,y=170)

        l2=Label(text=' USER ',font=('Times','18'),bg='black',fg='yellow')
        l2.place(x=420,y=170)

        l3=Label(text=sysscore,font=('ALGERIAN','70'),bg='WHITE',fg='BLACK')
        l3.place(x=130,y=30)

        l4=Label(text=usscore,font=('ALGERIAN','70'),bg='WHITE',fg='BLACK')
        l4.place(x=430,y=30)

        l5=Label(image=img2)
        l5.place(x=400,y=230)
        
        l6=Label(image=imgg2)
        l6.place(x=100,y=230)

        l7=Label(text='STATUS:',font=('Times','30','bold'),fg='WHITE',bg='BLACK')
        l7.place(x=40,y=400)

        l8=Label(text='NO MOVES YET!!',font=('Times','24'),bg='WHITE',fg='BLACK')
        l8.place(x=100,y=480)

        l9=Label(image=img6)
        l9.place(x=540,y=5)

        b1=Button(text=' STONE ',font=('Lucida Handwriting','14','bold'),bg='white',fg='black',command=lambda:process(1))
        b1.place(x=400,y=380)

        b2=Button(text=' PAPER ',font=('Lucida Handwriting','14','bold'),bg='grey',fg='white',command=lambda:process(2))
        b2.place(x=400,y=440)

        b3=Button(text='SCISSOR',font=('Lucida Handwriting','14','bold'),bg='yellow',fg='red',command=lambda:process(3))
        b3.place(x=400,y=500)
        main.mainloop()
        
    def terms(root):
       root.destroy()
       rule=Tk()
       rule.geometry('600x600')
       rule.title('PROGRAMMED BY AK')
       img1=PhotoImage(file=rules)
       c1=Canvas(width=620,height=620,bg='black')
       c1.place(x=0,y=0)
       c1.create_image(0,0,image=img1,anchor=NW)
       b1=Button(text="LET'S START",font=('Times','20','bold'),fg='red',bg='white',command=lambda:game(rule))
       b1.place(x=230,y=500)
       rule.mainloop()


    root=Tk()
    root.geometry('620x620')
    root.title('WELCOME TO RPS')

    img=PhotoImage(file=loc)
    c=Canvas(width=620,height=620,bg='black')
    c.place(x=0,y=0)
    c.create_image(0,0,image=img,anchor=NW)
    b=Button(text='START GAME',font=('Times','20','bold'),fg='red',bg='white',command=lambda:terms(root))
    b.place(x=230,y=500)
    root.mainloop()

from tkinter import *
def gintro():
    ak=Tk()
    ak.title('Ahamed Kabeer')
    ak.geometry('515x508')
    loc=r'Logo2.png'
    img=PhotoImage(file=loc)
    l=Label(ak,image=img)
    l.place(x=0,y=0)
    ak.after(3000,lambda:ak.destroy())
    ak.mainloop()
    
gintro()
actual()



