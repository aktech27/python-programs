import time
import os
class Timer:

    def __init__(self):
        self.HH,self.MM,self.SS=0,0,1
        
    def incrementor(self):
        self.SS+=1
        if(int(self.SS)==60):
            self.MM+=1
            self.SS=0
        if(int(self.MM)==60):
            self.HH+=1
            self.MM=0
            
            
    def show(self):
        os.system('cls')
        print('{:0>2}'.format(self.HH),':','{:0>2}'.format(self.MM),':','{:0>2}'.format(self.SS))
        Timer.incrementor(self)

t=Timer()
while(True):
    t.show()
    time.sleep(1)
