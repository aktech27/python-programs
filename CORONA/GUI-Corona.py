import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.ttk as TK
ctype="Active"


def showchart(event):
    global ctype
    statename=c1.get()
    lastdate=str(df.Date[-1:])
    lastdate=lastdate[8:16]
    title="Status of "+statename+" as of "+lastdate
    ST=df[['Date','State','Confirmed','Deaths','Cured','Active']][(df.State==statename)]
    plt.scatter(ST.Date,ST[ctype],color='r')
    plt.plot(ST.Date,ST[ctype],color='b')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Number of cases : '+ctype)
    plt.xticks(rotation=80)
    plt.show()
    
def settype():
    global ctype
    ctype=selection.get()

def showbar(df1):
    plt.barh(df1['State'],df1['Confirmed'],label="Confirmed Cases")
    plt.barh(df1['State'],df1['Active'],label="Active Cases")
    plt.barh(df1['State'],df1['Deaths'],label="Deaths")
    plt.legend()
    for index,value in enumerate(df1['Confirmed']):
        plt.text(value+2,index-0.3,str(value),fontsize=7)
    for index,value in enumerate(df1['Active']):
        plt.text(value+2,index-0.3,str(value),fontsize=7)
    for index,value in enumerate(df1['Deaths']):
        plt.text(value+2,index-0.3,str(value),fontsize=7)
    plt.show()        


    
df=pd.read_csv('covid_19_india.csv')
lastdate=str(df.Date[-1:])
lastdate=lastdate[8:16]
df['Active']=df['Confirmed']-df['Cured']-df['Deaths']
df['State']=df['State/UnionTerritory']
df=df.drop(['Sno','Time','State/UnionTerritory','ConfirmedIndianNational','ConfirmedForeignNational'],axis='columns')
df=df[['Date','State','Confirmed','Cured','Deaths','Active']]
bardata=df[['Date','State','Confirmed','Cured','Deaths','Active']][df.Date==lastdate]
bardata=bardata.sort_values(by=['Active'])
StateList=list(set(df.State))
StateList.sort()

root=Tk()
root.geometry('500x500')
root.title('COVID-19')
l1=Label(root,text="Choose State : ",font=('Lucida Bright',20,'bold'))
l1.place(x=10,y=200)
c1=TK.Combobox(root,values=StateList,font=('Times',18,'bold'))
c1.place(x=225,y=205)
c1.bind("<<ComboboxSelected>>",showchart)
l2=Label(root,text="Choose Case Type : ",font=('Lucida Bright',18,'bold'))
l2.place(x=10,y=100)
selection=StringVar(None,"none")
rb1=Radiobutton(root,text="Active Cases",variable=selection,value="Active",font=('Times',15),fg="red",indicatoron=0,command=settype)
rb2=Radiobutton(root,text="Confirmed cases",variable=selection,value="Confirmed",font=('Times',15),fg="blue",indicatoron=0,command=settype)
rb3=Radiobutton(root,text="Cured",variable=selection,value="Cured",font=('Times',15),fg="green",indicatoron=0,command=settype)
rb4=Radiobutton(root,text="Death",variable=selection,value="Deaths",font=('Times',15),indicatoron=0,command=settype)
rb1.place(x=10,y=140)
rb2.place(x=150,y=140)
rb3.place(x=330,y=140)
rb4.place(x=420,y=140)
b=Button(root,text="Show All",font=('Times',24,'bold'),bg="yellow",fg="black",command=lambda:showbar(bardata))
b.place(x=200,y=20)
l3=Label(root,text=("Last Updated Date : "+lastdate),font=('Times',12,'bold'))
l3.place(x=280,y=465)
root.mainloop()
