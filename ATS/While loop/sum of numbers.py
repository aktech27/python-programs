total=0
even_total=0
odd_total=0
i=1

print("\n\n\t\tSUM OF 'N' numbers\n\n")
size=int(input("Enter a number:"))

while i<=size:
    
    total+=i

    if i%2==0 :
        even_total+=i
    else:
        odd_total+=i
    i+=1    

print('\n\nSum of first ',size,' natural numbers is:',total)        
print('\n\nSum of first ',size,' odd natural numbers is:',odd_total)
print('\n\nSum of first ',size,' even natural numbers is:',even_total)
