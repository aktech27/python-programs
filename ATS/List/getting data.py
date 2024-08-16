list2=[]
size=int(input("Enter the size of the list:"))
for j in range(1,size+1):
    val=int(input("Enter the value of :"))
    list2.append(val)

print(list2)
print("Maximum value in the list is:",max(list2))
print("Minimum value in the list is:",min(list2))
list2.sort()
print("Sorted form of the list is:",list2)
