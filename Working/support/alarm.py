import winsound
import time
def beeper():
    for i in range(1,60):
        winsound.Beep(4500,200)
        winsound.Beep(4500,200)
        time.sleep(0.5)
