from tkinter import *
from tkcalendar import DateEntry
import tkinter.ttk as TTK
import os
import pandas as pd

yy=40
class Beneficiary:
    def __init__(self):
        self.df=pd.read_excel('details.xlsx',index=False)
        self.df2=pd.read_excel('products.xlsx',index=False)
        self._companies_=list(self.df['Company name'])
        self._products_=list(self.df2['Items'])
        self.Company_name=""
        self.Company_GST=""
        self.Company_ad1=""
        self.Company_ad2=""
        self.Company_ad3=""
        self.Company_phone=""
        self.CGST=""
        self.SGST=""
        self.IGST=""
        self.Date=""
        self.Lorryno=""
        self.Total,self.GrandTotal,self.GSTTotal=0.0,0.0,0.0
        self.cgstamt,self.sgstamt,self.igstamt=0,0,0
        self.Products=[]
        self.HSNs=[]
        self.Quantities=[]
        self.Rates=[]
        self.Raters=[]
        self.Rateps=[]
        self.Amounts=[]
        self.Amountrs=[]
        self.Amountps=[]        

        
    def getbenf(self):
        
        def finish(e1,e2,cb,de1,le1):
                
            if self.Date=="" :
                self.Date=de1.get()
                self.Date=str(self.Date[3:5]+"/"+self.Date[0:2]+"/"+self.Date[6:])

            self.Lorryno=le1.get()    

            self.Quantities.append(e1.get())
            self.Rates.append('{:.2f}'.format(float(e2.get())))
            product=cb.get()
            if self.Company_name=="TECHNO CRAFTS":
                hsncode=(list(self.df2['TechnoHSN'][self.df2.TechnoItems==product]))
            else:
                hsncode=(list(self.df2['HSN'][self.df2.Items==product]))
            self.Products.append(product)
            self.HSNs.append(str(int(hsncode[0])))

            for (i,j) in zip(self.Quantities,self.Rates):
                self.Total+=float(i)*float(j)
                self.Amounts.append('{:.2f}'.format(float(i)*float(j)))
            
            self.cgstamt=(self.Total*(int(self.CGST[0])))/100
            self.sgstamt=(self.Total*(int(self.SGST[0])))/100
            self.igstamt=(self.Total*(int(self.IGST[0])))/100

            self.GSTTotal=self.cgstamt+self.sgstamt+self.igstamt
            self.GrandTotal=self.Total+self.cgstamt+self.sgstamt+self.igstamt

            self.Total='{:.2f}'.format(self.Total)
            self.cgstamt='{:.2f}'.format(self.cgstamt)
            self.sgstamt='{:.2f}'.format(self.sgstamt)
            self.igstamt='{:.2f}'.format(self.igstamt)
            self.GSTTotal='{:.2f}'.format(self.GSTTotal)
            self.GrandTotal='{:.2f}'.format(self.GrandTotal)

            for i in range(0,len(self.Rates)):
                rs,ps=self.Rates[i].split('.')
                self.Raters.append(rs)
                self.Rateps.append(ps)
                rs,ps=self.Amounts[i].split('.')
                self.Amountrs.append(rs)
                self.Amountps.append(ps)

            
            print(self.Company_name)
            print(self.Company_GST)
            print(self.Company_ad1)
            print(self.Company_ad2)
            print(self.Company_ad3)
            print(self.Company_phone)
            print(self.CGST)
            print(self.SGST)
            print(self.IGST)
            print(self.Date)
            print(self.Lorryno)
            print(self.Products)
            print(self.HSNs)        
            print(self.Quantities)
            print(self.Rates)
            print(self.Raters)
            print(self.Rateps)
            print(self.Amounts)
            print(self.Amountrs)
            print(self.Amountps)
            print(self.Total)
            print(self.cgstamt,self.sgstamt,self.igstamt)
            print(self.GrandTotal)
           
        def newitem(e1,e2,cb,de1,le1):
            global yy
            product=cb.get()
            if self.Company_name=="TECHNO CRAFTS":
                hsncode=(list(self.df2['TechnoHSN'][self.df2.TechnoItems==product]))
            else:
                hsncode=(list(self.df2['HSN'][self.df2.Items==product]))
            self.Products.append(product)
            self.HSNs.append(str(int(hsncode[0])))
            self.Quantities.append(e1.get())
            self.Rates.append('{:.2f}'.format(float(e2.get())))
            cb2=TTK.Combobox(root,values=self._products_,font=('Times',20),width=30)
            cb2.bind("<<ComboboxSelected>>",lambda arg:addItem(cb2,de1,le1))
            cb2.place(x=370,y=315+yy)
            yy+=40
            
        def gsttype():
            if selection.get()=="within" :
                self.CGST="9%"
                self.SGST="9%"
                self.IGST="0%"
            
            if selection.get()=="outside" :
                self.CGST="0%"
                self.SGST="0%"
                self.IGST="18%"
                
        def setdate(event):
            mmddyyyy=de1.get()
            self.Date=str(mmddyyyy[3:5]+"/"+mmddyyyy[0:2]+"/"+mmddyyyy[6:])

        def addItem(cb,de1,le1):
            def addQty():
                e1=Entry(root,width=5,font=('Times',20,'bold'))
                e1.place(x=850,y=275+yy)
                l4e1=Label(root,text="  Quantity")
                l4e1.place(x=855,y=315+yy)
                e2=Entry(root,width=5,font=('Times',20,'bold'))
                e2.place(x=950,y=275+yy)
                l4e2=Label(root,text="  Rate")
                l4e2.place(x=955,y=315+yy)
                b1=Button(root,text='+',font=('Times',14,'bold'),width=3,fg='red',command=lambda:newitem(e1,e2,cb,de1,le1))
                b1.place(x=1050,y=315)
                b2=Button(root,text='>>',font=('Times',14,'bold'),width=3,fg='green',command=lambda:finish(e1,e2,cb,de1,le1))
                b2.place(x=1100,y=315)
                
            
            addQty()
            
        def setcompany(cb1,cb2):
            Company_Name=cb1.get()
            
            Company_GST=(list(self.df['GST'][self.df['Company name']==Company_Name]))
            Company_ad1=(list(self.df['Address1'][self.df['Company name']==Company_Name]))
            Company_ad2=(list(self.df['Address2'][self.df['Company name']==Company_Name]))
            Company_ad3=(list(self.df['Address3'][self.df['Company name']==Company_Name]))
            Company_phone=(list(self.df['Phone'][self.df['Company name']==Company_Name]))

            if Company_Name=="TECHNO CRAFTS":
                self._products_=list(self.df2['TechnoItems'])
                cb2['values']=self._products_

            else:
                self._products_=list(self.df2['Items'])
                cb2['values']=self._products_

                
            self.Company_name=Company_Name
            self.Company_GST=Company_GST[0]
            self.Company_ad1=Company_ad1[0]
            self.Company_ad2=Company_ad2[0]
            self.Company_ad3=Company_ad3[0]
            self.Company_phone=Company_phone[0]
            

        root=Tk()
        root.state('zoomed')
        root.geometry('500x500')
        
        l1=Label(root,text="VICTORY INDUSTRIES",font=('Times',50,'bold'))

        l2=Label(root,text="Choose Beneficiary :",font=('Times',30,'bold'))
        cb1=TTK.Combobox(root,values=self._companies_,font=('Times',20),width=30)
        
        l3=Label(root,text="Choose GST Type   :",font=('Times',30,'bold'))
        selection=StringVar(None,"none")
        rb1=Radiobutton(root,text="Within TamilNadu",variable=selection,value="within",font=('Times',20),indicatoron=0,command=gsttype)
        rb2=Radiobutton(root,text="Outside TamilNadu",variable=selection,value="outside",font=('Times',20),indicatoron=0,command=gsttype)

        l4=Label(root,text="Choose Product       :",font=('Times',30,'bold'))
        cb2=TTK.Combobox(root,values=self._products_,font=('Times',20),width=30)
        
        l5=Label(root,text="Select Invoice Date :",font=('Times',30,'bold'))
        de1=DateEntry(root,locale='en_US', date_pattern='MM/dd/yyyy',font=('Times',18),weekendbackground="white",weekendforeground="black")

        l6=Label(root,text="Lorry No:",font=('Times',30,'bold'))
        le1=Entry(root,width=16,font=('Times',18))

        cb1.bind("<<ComboboxSelected>>",lambda arg :setcompany(cb1,cb2))
        cb2.bind("<<ComboboxSelected>>",lambda arg :addItem(cb2,de1,le1))
        de1.bind("<<DateEntrySelected>>",setdate)
        
        l1.place(x=350,y=10)
        l2.place(x=10,y=150)
        l3.place(x=10,y=200)
        l4.place(x=10,y=305)
        l5.place(x=10,y=250)
        l6.place(x=570,y=255)
        cb1.place(x=370,y=160)
        cb2.place(x=370,y=315)
        rb1.place(x=400,y=210)
        rb2.place(x=650,y=210)
        de1.place(x=370,y=265)
        le1.place(x=750,y=267)
        
        root.mainloop()

        
