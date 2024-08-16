from tkinter import *
import random
import time
array=[None]*38
img=[None]*38
txt=[None]*38
recbtn=None
default=None
class inro:
  def intro(self):
    ak=Tk()
    ak.title('Ahamed Kabeer')
    ak.geometry('515x508')
    loc=r'Logo2.png'
    img=PhotoImage(file=loc)
    l=Label(ak,image=img)
    l.place(x=0,y=0)
    ak.after(2500,lambda:ak.destroy())
    ak.mainloop()
  def title(self):
    bg=Tk()
    bg.title('Ahamed Kabeer')
    bg.geometry('500x500')
    loc=r'mem_bg.png'
    img=PhotoImage(file=loc)
    l=Label(bg,image=img)
    l.place(x=0,y=0)
    bg.after(2500,lambda:bg.destroy())
    bg.mainloop()
 
    
class Program:
    click=1
    match=0
    u_timer=0
    v_timer=0

    def main(self):
        global array,img,txt,default
        def checkwin():
          if(Program.match==18):
            Program.v_timer=time.time()
            now=Program.v_timer-Program.u_timer
            from tkinter import messagebox
            import sys
            messagebox.showinfo("GAME OVER","ALL MATCHES FOUND PERFECTLY\nTIME TAKEN:  %.2f seconds"%now)
            root.destroy()
            sys.exit()

        def checkmatch(b):
            if(b['text']==recbtn['text'] and b!=recbtn):
                b.destroy()
                recbtn.destroy()
                Program.match+=1
                checkwin()
            else:
                b['image']=default
                recbtn['image']=default
                
            

        def but1(b):
            global img,recbtn
            b['image']=img[0]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but2(b):
            global img,recbtn
            b['image']=img[1]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but3(b):
            global img,recbtn
            b['image']=img[2]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but4(b):
            global img,recbtn
            b['image']=img[3]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but5(b):
            global img,recbtn
            b['image']=img[4]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but6(b):
            global img,recbtn
            b['image']=img[5]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but7(b):
            global img,recbtn
            b['image']=img[6]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but8(b):
            global img,recbtn
            b['image']=img[7]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but9(b):
            global img,recbtn
            b['image']=img[8]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but10(b):
            global img,recbtn
            b['image']=img[9]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but11(b):
            global img,recbtn
            b['image']=img[10]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but12(b):
            global img,recbtn
            b['image']=img[11]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but13(b):
            global img,recbtn
            b['image']=img[12]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but14(b):
            global img,recbtn
            b['image']=img[13]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but15(b):
            global img,recbtn
            b['image']=img[14]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but16(b):
            global img,recbtn
            b['image']=img[15]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but17(b):
            global img,recbtn
            b['image']=img[16]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but18(b):
            global img,recbtn
            b['image']=img[17]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but19(b):
            global img,recbtn
            b['image']=img[18]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but20(b):
            global img,recbtn
            b['image']=img[19]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but21(b):
            global img,recbtn
            b['image']=img[20]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but22(b):
            global img,recbtn
            b['image']=img[21]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but23(b):
            global img,recbtn
            b['image']=img[22]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but24(b):
            global img,recbtn
            b['image']=img[23]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but25(b):
            global img,recbtn
            b['image']=img[24]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but26(b):
            global img,recbtn
            b['image']=img[25]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but27(b):
            global img,recbtn
            b['image']=img[26]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but28(b):
            global img,recbtn
            b['image']=img[27]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but29(b):
            global img,recbtn
            b['image']=img[28]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but30(b):
            global img,recbtn
            b['image']=img[29]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but31(b):
            global img,recbtn
            b['image']=img[30]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but32(b):
            global img,recbtn
            b['image']=img[31]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but33(b):
            global img,recbtn
            b['image']=img[32]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but34(b):
            global img,recbtn
            b['image']=img[33]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but35(b):
            global img,recbtn
            b['image']=img[34]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but36(b):
            global img,recbtn
            b['image']=img[35]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1
                       
        Program.u_timer=time.time()                            
        root=Tk()
        root.geometry('600x650')
        root.title('MEMORY GAME')

        loc1=r'doraemon.png'
        loc2=r'nobita.png'
        loc3=r'manny.png'
        loc4=r'buzz.png'
        loc5=r'buck.png'
        loc6=r'hima.png'
        loc7=r'olaf.png'
        loc8=r'po.png'
        loc9=r'pumba.png'
        loc10=r'shinchan.png'
        loc11=r'shifu.png'
        loc12=r'tigress.png'
        loc13=r'woody.png'
        loc=r'ak_bg.png'

        default=PhotoImage(file=loc)
        array=[loc1,loc2,loc3,loc4,loc5,loc6,loc7,loc8,loc9,loc10,loc11,loc12,loc13]
        templist=array
        #print(templist)
        list2=[None]*5
        for j in range(0,5,1):
              list2[j]=random.choice(templist)
              templist.remove(list2[j])
        array=[loc1,loc2,loc3,loc4,loc5,loc6,loc7,loc8,loc9,loc10,loc11,loc12,loc13]
        array=array+list2
        array=array+array
        
        for i in range(0,36,1):
            x=random.choice(array)
            img[i]=PhotoImage(file=x)
            txt[i+1]=str(x)
            array.remove(x)
                        
            


        c=Canvas(root,bg='black',height=700,width=700)
        c.place(x=0,y=0)

        #row1
        b11=Button(root,image=default,text=txt[1],bg='white',height=95,width=88,command=lambda:but1(b11))
        b11.place(x=10,y=20)
        b12=Button(root,image=default,text=txt[2],bg='white',height=95,width=88,command=lambda:but2(b12))
        b12.place(x=105,y=20)
        b13=Button(root,image=default,text=txt[3],bg='white',height=95,width=88,command=lambda:but3(b13))
        b13.place(x=200,y=20)
        b14=Button(root,image=default,text=txt[4],bg='white',height=95,width=88,command=lambda:but4(b14))
        b14.place(x=295,y=20)
        b15=Button(root,image=default,text=txt[5],bg='white',height=95,width=88,command=lambda:but5(b15))
        b15.place(x=390,y=20)
        b16=Button(root,image=default,text=txt[6],bg='white',height=95,width=88,command=lambda:but6(b16))
        b16.place(x=485,y=20)

        #row2
        b21=Button(root,image=default,text=txt[7],bg='white',height=95,width=88,command=lambda:but7(b21))
        b21.place(x=10,y=122)
        b22=Button(root,image=default,text=txt[8],bg='white',height=95,width=88,command=lambda:but8(b22))
        b22.place(x=105,y=122)
        b23=Button(root,image=default,text=txt[9],bg='white',height=95,width=88,command=lambda:but9(b23))
        b23.place(x=200,y=122)
        b24=Button(root,image=default,text=txt[10],bg='white',height=95,width=88,command=lambda:but10(b24))
        b24.place(x=295,y=122)
        b25=Button(root,image=default,text=txt[11],bg='white',height=95,width=88,command=lambda:but11(b25))
        b25.place(x=390,y=122)
        b26=Button(root,image=default,text=txt[12],bg='white',height=95,width=88,command=lambda:but12(b26))
        b26.place(x=485,y=122)

        #row3
        b31=Button(root,image=default,text=txt[13],bg='white',height=95,width=88,command=lambda:but13(b31))
        b31.place(x=10,y=224)
        b32=Button(root,image=default,text=txt[14],bg='white',height=95,width=88,command=lambda:but14(b32))
        b32.place(x=105,y=224)
        b33=Button(root,image=default,text=txt[15],bg='white',height=95,width=88,command=lambda:but15(b33))
        b33.place(x=200,y=224)
        b34=Button(root,image=default,text=txt[16],bg='white',height=95,width=88,command=lambda:but16(b34))
        b34.place(x=295,y=224)
        b35=Button(root,image=default,text=txt[17],bg='white',height=95,width=88,command=lambda:but17(b35))
        b35.place(x=390,y=224)
        b36=Button(root,image=default,text=txt[18],bg='white',height=95,width=88,command=lambda:but18(b36))
        b36.place(x=485,y=224)

        #row4
        b41=Button(root,image=default,text=txt[19],bg='white',height=95,width=88,command=lambda:but19(b41))
        b41.place(x=10,y=326)
        b42=Button(root,image=default,text=txt[20],bg='white',height=95,width=88,command=lambda:but20(b42))
        b42.place(x=105,y=326)
        b43=Button(root,image=default,text=txt[21],bg='white',height=95,width=88,command=lambda:but21(b43))
        b43.place(x=200,y=326)
        b44=Button(root,image=default,text=txt[22],bg='white',height=95,width=88,command=lambda:but22(b44))
        b44.place(x=295,y=326)
        b45=Button(root,image=default,text=txt[23],bg='white',height=95,width=88,command=lambda:but23(b45))
        b45.place(x=390,y=326)
        b46=Button(root,image=default,text=txt[24],bg='white',height=95,width=88,command=lambda:but24(b46))
        b46.place(x=485,y=326)

        #row5
        b51=Button(root,image=default,text=txt[25],bg='white',height=95,width=88,command=lambda:but25(b51))
        b51.place(x=10,y=428)
        b52=Button(root,image=default,text=txt[26],bg='white',height=95,width=88,command=lambda:but26(b52))
        b52.place(x=105,y=428)
        b53=Button(root,image=default,text=txt[27],bg='white',height=95,width=88,command=lambda:but27(b53))
        b53.place(x=200,y=428)
        b54=Button(root,image=default,text=txt[28],bg='white',height=95,width=88,command=lambda:but28(b54))
        b54.place(x=295,y=428)
        b55=Button(root,image=default,text=txt[29],bg='white',height=95,width=88,command=lambda:but29(b55))
        b55.place(x=390,y=428)
        b56=Button(root,image=default,text=txt[30],bg='white',height=95,width=88,command=lambda:but30(b56))
        b56.place(x=485,y=428)

        #row6
        b61=Button(root,image=default,text=txt[31],bg='white',height=95,width=88,command=lambda:but31(b61))
        b61.place(x=10,y=530)
        b62=Button(root,image=default,text=txt[32],bg='white',height=95,width=88,command=lambda:but32(b62))
        b62.place(x=105,y=530)
        b63=Button(root,image=default,text=txt[33],bg='white',height=95,width=88,command=lambda:but33(b63))
        b63.place(x=200,y=530)
        b64=Button(root,image=default,text=txt[34],bg='white',height=95,width=88,command=lambda:but34(b64))
        b64.place(x=295,y=530)
        b65=Button(root,image=default,text=txt[35],bg='white',height=95,width=88,command=lambda:but35(b65))
        b65.place(x=390,y=530)
        b66=Button(root,image=default,text=txt[36],bg='white',height=95,width=88,command=lambda:but36(b66))
        b66.place(x=485,y=530)


        root.mainloop()
obj=inro()
obj.intro()
obj.title()
obj1=Program()
obj1.main()
