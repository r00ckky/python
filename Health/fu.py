import time
from pygame import mixer
def gettime():
    return time.asctime(time.localtime(time.time()))

def tim():
    return time.time()

def water():
    mixer.init()
    mixer.music.load('Panni.mp3')
    mixer.music.play(-1)
    while(True):
        k=input("Type 1 if you have drunk water")
        if(k=='1'):
            mixer.music.stop()
            break
    f=open("water.txt","a")
    f.write(gettime()+"\n")
    f.close()

def sleep():
    mixer.init()
    mixer.music.load('Sojao.mp3')
    mixer.music.play(-1)
    while (True):
        k = input("Type 1 if you have decided to sleep")
        if (k == '1'):
            mixer.music.stop()
            break
    f = open("sleep.txt", "a")
    f.write(gettime() + "\n")
    f.close()

def phy():
    mixer.init()
    mixer.music.load('Phys.mp3')
    mixer.music.play(-1)
    while (True):
        k = input("Type 1 if you have exercised")
        if (k == '1'):
            mixer.music.stop()
            break
    f = open("physical.txt", "a")
    f.write(gettime() + "\n")
    f.close()