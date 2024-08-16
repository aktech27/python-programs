list1=[]
oddlist=[]
evenlist=[]
size=int(input("Enter the size of the list:"))
for j in range(1,size+1):
    val=int(input("Enter the value :"))
    list1.append(val)

print('\n\nThe given list is:',list1)

for i in list1:
    if(i%2==0):
        evenlist.append(i)
    else:
        oddlist.append(i)

print("\nOdd numbers in the given list:",oddlist)
print("Total odd numbers is:",len(oddlist))
print("\nEven numbers in the given list:",evenlist)
print("Total even numbers is:",len(evenlist))
