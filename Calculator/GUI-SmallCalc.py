from tkinter import *

class intro:
        
    def gintro():
        ak=Tk()
        ak.title('Ahamed Kabeer')
        ak.geometry('515x508')
        loc=r'logo2.png'
        img=PhotoImage(file=loc)
        l=Label(ak,image=img)
        l.place(x=0,y=0)
        ak.after(3000,lambda:ak.destroy())
        ak.mainloop()
        

class Calculator:

    memory=''        #the calculating part
    display=''       #the displaying part
    status='OFF'     #to terminate all activity
    deci=False       #to avoid adding additional decimal points
    operator=False    #to avoid error when operators are pressed more than once
    
    def layout(self):
        root=Tk()
        root.geometry('450x450')
        root.title("AK-TECH27")

        #image loading...
        logo=PhotoImage(file=r'calclogo.png')
        one=PhotoImage(file=r'one.png')
        two=PhotoImage(file=r'two.png')
        three=PhotoImage(file=r'three.png')
        four=PhotoImage(file=r'four.png')
        five=PhotoImage(file=r'five.png')
        six=PhotoImage(file=r'six.png')
        seven=PhotoImage(file=r'seven.png')
        eight=PhotoImage(file=r'eight.png')
        nine=PhotoImage(file=r'nine.png')
        zero=PhotoImage(file=r'zero.png')
        dot=PhotoImage(file=r'dot.png')
        plus=PhotoImage(file=r'plus.png')
        minus=PhotoImage(file=r'minus.png')
        divide=PhotoImage(file=r'div.png')
        multiply=PhotoImage(file=r'mul.png')
        equal=PhotoImage(file=r'equal.png')
        percentage=PhotoImage(file=r'perc.png')
        on=PhotoImage(file=r'on.png')
        off=PhotoImage(file=r'soff.png')
        cut=PhotoImage(file=r'cut.png')
        x2=PhotoImage(file=r'x2.png')
        sqrt=PhotoImage(file=r'sqrtx.png')
        negation=PhotoImage(file=r'negation.png')

        #canvas and labels...
        c1=Canvas(root,bg='white',height=450,width=450)
        c1.place(x=0,y=0)
        c2=Canvas(root,bg='black',height=380,width=260)
        c2.place(x=95,y=35)
        l1=Label(root,bg='#91ff91',width=11,height=1,text='',anchor=E,font=('times','24','bold'))
        l1.place(x=120,y=80)
        l2=Label(root,bg='black',fg='white',text="AK-CALC",font=("Times",'14','bold'))
        l2.place(x=120,y=50)
        l3=Label(root,image=logo,bd=0)
        l3.place(x=313,y=38)

        #Coloumn 1 buttons...
        b1=Button(root,image=on,bd=1,width=45,bg='red',command=lambda:Power.fn_on(l1))
        b1.place(x=120,y=155)
        b2=Button(root,image=cut,bd=1,width=45,bg='white',command=lambda:Power.fn_cut(l1))
        b2.place(x=120,y=195)
        b3=Button(root,image=seven,bd=1,width=45,bg='white',command=lambda:Numbers.fn_7(l1))
        b3.place(x=120,y=235)
        b4=Button(root,image=four,bd=1,width=45,bg='white',command=lambda:Numbers.fn_4(l1))
        b4.place(x=120,y=275)
        b5=Button(root,image=one,bd=1,width=45,bg='white',command=lambda:Numbers.fn_1(l1))
        b5.place(x=120,y=315)
        b6=Button(root,image=zero,bd=1,width=45,bg='white',command=lambda:Numbers.fn_0(l1))
        b6.place(x=120,y=355)

        #Coloumn 2 buttons...
        b7=Button(root,image=negation,bd=1,width=45,bg='white',command=lambda:Arithmetic.fn_neg(l1))
        b7.place(x=175,y=155)
        b8=Button(root,image=percentage,bd=1,width=45,bg='white',command=lambda:Arithmetic.fn_percent(l1))
        b8.place(x=175,y=195)
        b9=Button(root,image=eight,bd=1,width=45,bg='white',command=lambda:Numbers.fn_8(l1))
        b9.place(x=175,y=235)
        b10=Button(root,image=five,bd=1,width=45,bg='white',command=lambda:Numbers.fn_5(l1))
        b10.place(x=175,y=275)
        b11=Button(root,image=two,bd=1,width=45,bg='white',command=lambda:Numbers.fn_2(l1))
        b11.place(x=175,y=315)
        b12=Button(root,image=dot,bd=1,width=45,bg='white',command=lambda:Numbers.fn_decimal(l1))
        b12.place(x=175,y=355)

        #Coloumn 3 buttons...
        b13=Button(root,image=sqrt,bd=1,width=45,bg='white',command=lambda:Arithmetic.fn_root(l1))
        b13.place(x=230,y=155)
        b14=Button(root,image=x2,bd=1,width=45,bg='white',command=lambda:Arithmetic.fn_square(l1))
        b14.place(x=230,y=195)
        b15=Button(root,image=nine,bd=1,width=45,bg='white',command=lambda:Numbers.fn_9(l1))
        b15.place(x=230,y=235)
        b16=Button(root,image=six,bd=1,width=45,bg='white',command=lambda:Numbers.fn_6(l1))
        b16.place(x=230,y=275)
        b17=Button(root,image=three,bd=1,width=45,bg='white',command=lambda:Numbers.fn_3(l1))
        b17.place(x=230,y=315)
        b18=Button(root,image=equal,bd=1,width=45,bg='white',command=lambda:Power.fn_equalto(l1))
        b18.place(x=230,y=355)

        #Coloumn 4 buttons...
        b19=Button(root,image=off,bd=1,width=45,bg='white',command=lambda:Power.fn_off(l1))
        b19.place(x=285,y=155)
        b20=Button(root,image=divide,bd=1,width=45,bg='white',command=lambda:Arithmetic.fn_div(l1))
        b20.place(x=285,y=195)
        b21=Button(root,image=multiply,bd=1,width=45,bg='white',command=lambda:Arithmetic.fn_mul(l1))
        b21.place(x=285,y=235)
        b22=Button(root,image=minus,bd=1,width=45,bg='white',command=lambda:Arithmetic.fn_sub(l1))
        b22.place(x=285,y=275)
        b23=Button(root,image=plus,bd=1,width=45,height=72,bg='white',command=lambda:Arithmetic.fn_add(l1))
        b23.place(x=285,y=315)


        root.mainloop()

class Power(Calculator):
    def fn_on(l1):
        l1["text"]='0'
        cal.status='ON'
        cal.display=''
        cal.deci=False
        cal.memory=''
        cal.operator=False
    def fn_off(l1):
        l1["text"]=''
        cal.status='OFF'
        cal.display=''
        cal.deci=False
        cal.operator=False
        cal.memory=''
    def fn_equalto(l1):
        op_list=['+','-','*','/']
        cal.deci=False    #to enable decimal after equal is pressed
        if('/0' in cal.memory):   #division by  zero
            cal.memory='infinity'
            l1['text']='INFINITY'
        elif(cal.memory[-1] in op_list):
            l1['text']='Error'
            cal.status='OFF'      
        else:    
            cal.memory=str(eval(cal.memory))
            cal.display=cal.memory[0:12] #limit to 10 digits including decimal point
            if(not('.' in cal.display) and len(cal.memory)>13):
                l1['text']='Error'
                cal.status='OFF'
            else:
                l1['text']=cal.display
                cal.display=''
                        
    def fn_cut(l1):
        cal.memory=cal.memory[0:(len(cal.memory)-1)]
        cal.display=cal.memory
        l1['text']=cal.display

        
class Arithmetic(Calculator):
    def fn_add(l1):
         if(cal.status=='ON' and cal.operator==True):
            cal.memory=cal.memory.replace(cal.memory[-1],'+')
            
         elif(cal.status=='ON' and cal.operator==False):
            cal.operator=True
            cal.deci=False
            l1["text"]=Power.fn_equalto(l1)
            cal.memory=cal.memory+'+'
            cal.display=''
            
    def fn_sub(l1):
         if(cal.status=='ON' and cal.operator==True):             
             cal.memory=cal.memory.replace(cal.memory[-1],'-')
             
         elif(cal.status=='ON' and cal.operator==False):
            cal.operator=True
            cal.deci=False
            l1["text"]=Power.fn_equalto(l1)
            cal.memory=cal.memory+'-'
            cal.display=''
           
    def fn_mul(l1):
         if(cal.status=='ON' and cal.operator==True):             
             cal.memory=cal.memory.replace(cal.memory[-1],'*')
         elif(cal.status=='ON' and cal.operator==False):
            cal.operator=True
            cal.deci=False
            l1["text"]=Power.fn_equalto(l1)
            cal.memory=cal.memory+'*'
            cal.display=''
         
    def fn_div(l1):
         if(cal.status=='ON' and cal.operator==True):
             cal.memory=cal.memory.replace(cal.memory[-1],'/')
         elif(cal.status=='ON' and cal.operator==False):
            cal.operator=True
            cal.deci=False
            l1["text"]=Power.fn_equalto(l1)
            cal.memory=cal.memory+'/'
            cal.display=''
            
    def fn_percent(l1):
         if(cal.status=='ON' and cal.operator==False):
            cal.deci=False
            l1["text"]=Power.fn_equalto(l1)
            cal.memory=cal.memory+'*100.00'
            cal.display=Power.fn_equalto(l1)
         elif(cal.status=='ON' and cal.operator==True):
             cal.memory=cal.memory.replace(cal.memory[-1],'*100.00')
             cal.display=Power.fn_equalto(l1)
    def fn_square(l1):
         if(cal.status=='ON' and cal.operator==False):
            cal.deci=False
            l1["text"]=Power.fn_equalto(l1)
            cal.memory=cal.memory+'**2'
            cal.display=Power.fn_equalto(l1)
         elif(cal.status=='ON' and cal.operator==True):
             cal.memory=cal.memory.replace(cal.memory[-1],'**2')
             cal.display=Power.fn_equalto(l1)
    def fn_root(l1):
         if(cal.status=='ON' and cal.operator==False):
            cal.operator=True
            cal.deci=False
            l1["text"]=Power.fn_equalto(l1)
            cal.memory=cal.memory+'**0.5'
            cal.display=Power.fn_equalto(l1)
         elif(cal.status=='ON' and cal.operator==True):
             cal.memory=cal.memory.replace(cal.memory[-1],'**0.5')
             cal.display=Power.fn_equalto(l1)
    def fn_neg(l1):
         if(cal.status=='ON' and cal.operator==False):
            cal.deci=False
            l1["text"]=Power.fn_equalto(l1)
            cal.memory=cal.memory+'*-1'
            cal.display=Power.fn_equalto(l1)
        
class Numbers(Calculator):
    Calculator.operator=False
    def fn_1(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'1'
            cal.display=cal.display+'1'
            l1["text"]=cal.display
            cal.operator=False
    def fn_2(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'2'
            cal.display=cal.display+'2'
            l1["text"]=cal.display
            cal.operator=False
    def fn_3(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'3'
            cal.display=cal.display+'3'
            l1["text"]=cal.display
            cal.operator=False
    def fn_4(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'4'
            cal.display=cal.display+'4'
            l1["text"]=cal.display
            cal.operator=False
    def fn_5(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'5'
            cal.display=cal.display+'5'
            l1["text"]=cal.display
            cal.operator=False
    def fn_6(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'6'
            cal.display=cal.display+'6'
            l1["text"]=cal.display
            cal.operator=False
    def fn_7(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'7'
            cal.display=cal.display+'7'
            l1["text"]=cal.display
            cal.operator=False
    def fn_8(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'8'
            cal.display=cal.display+'8'
            l1["text"]=cal.display
            cal.operator=False
    def fn_9(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'9'
            cal.display=cal.display+'9'
            l1["text"]=cal.display
            cal.operator=False
    def fn_0(l1):
        if(cal.status=='ON'):
            cal.memory=cal.memory+'0'
            cal.display=cal.display+'0'
            l1["text"]=cal.display
            cal.operator=False
    def fn_decimal(l1):
        if(cal.status=='ON' and cal.deci==False):
            cal.deci=True                          #to avoid displaying further decimal points
            cal.memory=cal.memory+'.'
            cal.display=cal.display+'.'
            l1["text"]=cal.display
            cal.operator=False

  
intro.gintro()

#object of main class...
cal=Calculator()
cal.layout()


