import matplotlib.pyplot as plt
xrange=[0,10,20,30,40,50,60,70,80,90]
yvalues=[1,21,37,34,5,5,64,7,56,7,78,78,76,89,86,90,87,90,90,88]
a=plt.hist(yvalues,xrange,histtype='bar')
plt.show()
