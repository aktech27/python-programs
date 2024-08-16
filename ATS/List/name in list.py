listname=["Keethir","Ahamed","Kabeer","Python"]
empty=[]
for i in listname:
    temp1=i.upper()
    temp2=i.lower()
    empty.append(temp1)
    empty.append(temp2)
    
listname=listname+empty
print(listname)
name=str(input('Enter a name:'))
if(name in listname):
    print("The given name is present")
else:
    print("The given name is not present")
