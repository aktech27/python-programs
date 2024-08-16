list1=[]
poslist=[]
neglist=[]
zero=[]
size=int(input("Enter the size of the list:"))
for j in range(1,size+1):
    val=int(input("Enter the value :"))
    list1.append(val)

print('\n\nThe given list is:',list1)

for i in list1:
    if(i>0):
        poslist.append(i)
    elif(i<0):
        neglist.append(i)
    else:
        zero.append(i)
print("\nPositive numbers in the given list:",poslist)
print("Total postive numbers are:",len(poslist))
print("\nNegative numbers in the given list:",neglist)
print("Total negative numbers are:",len(neglist))
print("\nZeros given are:",len(zero))
