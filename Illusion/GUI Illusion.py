from tkinter import *
root=Tk()
ht=500
wd=500
col1='black'
col2='white'
xpos=0
ypos=0
turn=2
def main():
    global ht,wd,xpos,ypos,col1,col2
    def changecol():
        global col1,col2,turn,ht,wd,xpos,ypos
        if(turn%2==0):
            turn+=1
            col1='white'
            col2='black'
            ht=500
            wd=500
            xpos=0
            ypos=0
            main()
        else:
            turn+=1
            col2='white'
            col1='black'
            ht=500
            wd=500
            xpos=0
            ypos=0
            main()
 
    
    for i in range(1,8,1):            
        c1=Canvas(root,height=ht,width=wd,bg=col1,border=0)
        c1.place(x=xpos,y=ypos)
        ht=ht-40
        wd=wd-40
        xpos=xpos+20
        ypos=ypos+20
        c2=Canvas(root,height=ht,width=wd,bg=col2,border=0)
        c2.place(x=xpos,y=ypos)
        ht=ht-40
        wd=wd-40
        xpos=xpos+20
        ypos=ypos+20
    root.after(500,lambda:changecol())    
    root.title("AK-Tech")
    root.geometry("500x500")
    root.mainloop()

main()
