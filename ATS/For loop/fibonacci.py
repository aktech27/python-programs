print("\n\n\t\tFIBONACCI SERIES\n\n")
a=-1
b=1
num=int(input("Enter the limit of series:"))
print("\nFIBONACCI SERIES IS:")
for i in range(1,num+1):
    c=a+b
    a=b
    b=c
    print(c,end='  ')
