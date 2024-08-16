print("\n\n\t\tTABLES\n\n")
num=int(input("Enter the number :"))
limit=int(input("Enter the limit  :"))
for i in range(1,limit+1):
    print('\t%2d x %2d = %d'%(num,i,num*i))
