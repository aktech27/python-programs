total=0
even_total=0
odd_total=0

print("\n\n\t\tSUM OF 'N' numbers\n\n")
size=int(input("Enter a number:"))

for i in range(1,size+1):
    total+=i

    if i%2==0 :
        even_total+=i
    else:
        odd_total+=i

print('\n\nSum of first ',size,' natural numbers is:',total)        
print('\n\nSum of first ',size,' odd natural numbers is:',odd_total)
print('\n\nSum of first ',size,' even natural numbers is:',even_total)
