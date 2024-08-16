
print("  X",end=' |')
for a in range(1,11):
    print('%5d'%a,end='')
print('\n----------------------------------------------------------')    
for i in range(1,11):
    print('%3d'%i,end=' |')
    for j in range(1,11):
        print('%5d'%(i*j),end='')
    print("\n")
