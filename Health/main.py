import fu
import time
ini=0
while(True):
    time.sleep(60)
    ini+=1
    if(ini==45):
        fu.phy()
    elif(ini==60):
        fu.sleep()
    elif(ini==15):
        fu.water()