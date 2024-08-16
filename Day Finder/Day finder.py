from tkinter import *
from tkinter.ttk import *
monthcode,yearcode,day=0,0,''

def gintro():
    ak=Tk()
    ak.title('Ahamed Kabeer')
    ak.geometry('515x508')
    loc=r'D:\BCA AK\Pics\logo.png'
    img=PhotoImage(file=loc)
    l=Label(ak,image=img)
    l.place(x=0,y=0)
    ak.after(3000,lambda:ak.destroy())
    ak.mainloop()
    

def main():
    def getday(root,c1,c2,c3,ll,l):
        global monthcode,yearcode,day
        days=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
        t=str(c1.get())+' '+str(c2.get())+','+str(c3.get())
        l['text']=t
        yearval=int(c2.get())%100
        dateval=int(c3.get())
        leapval=int(yearval/4)
        if(c2.get()>='1900' and c2.get()<='1999'):
            yearcode=0
        if(c2.get()>='2000' and c2.get()<='2999'):
            yearcode=6
        if(c1.get()=="January"):
            monthcode=1
        elif(c1.get()=="February"):
            monthcode=4
        elif(c1.get()=="March"):
            monthcode=4
        elif(c1.get()=="April"):
            monthcode=0
        elif(c1.get()=="May"):
            monthcode=2
        elif(c1.get()=="June"):
            monthcode=5
        elif(c1.get()=="July"):
            monthcode=0
        elif(c1.get()=="August"):
            monthcode=3
        elif(c1.get()=="September"):
            monthcode=6
        elif(c1.get()=="October"):
            monthcode=1
        elif(c1.get()=="November"):
            monthcode=4
        elif(c1.get()=="December"):
            monthcode=6
        daycode=int((dateval+yearval+leapval+yearcode+monthcode)%7)
        print(dateval,yearval,leapval,yearcode,monthcode,sep=',')
        print(daycode)
        for i in range(0,7):
            if(i==daycode):
                day=days[i]
        ll['text']=day        
            
    month=['January','February','March','April','May','June','July','August','September','October','November','December']
    year=[None]*1500
    date=[None]*31
    for i in range(0,1500):
        year[i]=int(i+1900)
    for i in range(1,32):
        date[i-1]=i


    root=Tk()
    root.geometry('500x500')
    root.title('AK-Tech 27')

    l1=Label(root,text='Day Finder',font=('times',26,'bold'),background='white')
    l1.place(x=160,y=10)

    c1=Combobox(root,values=month)
    c1.current(0)
    c1.place(x=10,y=100)

    c2=Combobox(root,values=year,width=4)
    c2.current(0)
    c2.place(x=160,y=100)

    c3=Combobox(root,values=date,width=3)
    c3.current(0)
    c3.place(x=230,y=100)

    ll=Label(root,text='',font=('Times',30,'bold'),foreground='red')
    ll.place(x=150,y=300)

    l=Label(root,text='',font=('Times',24),foreground='blue')
    l.place(x=150,y=250)        

    b1=Button(root,text="Get Day",command=lambda:getday(root,c1,c2,c3,ll,l))
    b1.place(x=300,y=100)

    
    root.mainloop()


gintro()
main()
