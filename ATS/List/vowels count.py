vowels=["A","E","I","O","U",'a','e','i','o','u']
v_count=0
text=str(input("Enter a passage:"))
for i  in text:
    if(i in vowels):
        v_count+=1
print("Number of vowels in the text are:",v_count)


