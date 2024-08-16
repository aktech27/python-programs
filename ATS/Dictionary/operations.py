a={"Name":"Ahamed","Age":19,"Course":"Python"}
b={1001:"id","Place":"Chennai","Pin code":600100}

print("Type:",type(a))
print("Length:",len(a))
print("Elements in a using for loop:")
for i in a:
    print(i)

print("TYPE CASTING dictinary a")
l=list(a)
t=tuple(a)
print(l)
print(t)
##d=dict(l)
##print(d)
print('\nKeys of a:',a.keys())
print('\nValues of a:',a.values())
print('\nItems of a:',a.items())
a.update(b)
print('\nUpdation:',a)
a.clear()
print(a)

