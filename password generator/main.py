import random
import datetime
def getdate():
    import datetime
    return datetime.datetime.now()
capl=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','Z','X','Z']
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','z','x','z']
sym=['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':','"','\'','\\','|','/','?','.',',','<','>']
num=['1','2','3','4','5','6','7','8','9','0']
task=int(input("Type 1 for password retreival or 2 for password generator "))
if(task==1):
    f=open("pass.txt","r")
    content=f.read()
    print(content)
    f.close()
elif(task==2):
    isalornum=int(input("Type 1 for alphanumeric, Type 2 for numeric, Type 3 for alphabet, Type 4 for symbol or Type 5 for symbol and alphanumeric "))
    mi=int(input("What is the minimum size of password "))
    ma=int(input("What is the maximum size of password "))
    mini=random.randint(mi,ma)
    k=""
    if(isalornum==1):
        while(mini>0):
            k+=random.choice(random.choice(capl)+random.choice(l)+random.choice(num))
            mini-=1
    elif(isalornum==2):
        while(mini>0):
            k+=random.choice(num)
            mini-=1
    elif(isalornum==3):
        while(mini>0):
            k+=random.choice(random.choice(capl)+random.choice(l))
            mini-=1
    elif(isalornum==4):
        while(mini>0):
            k+=random.choice(sym)
            mini-=1
    elif(isalornum==5):
        while(mini>0):
            k+=random.choice(random.choice(capl)+random.choice(l)+random.choice(num)+random.choice(sym))
            mini-=1
    print(k)
    save=int(input("Type 1 if you wish to save the password "))
    if(save==1):
        web=input("Enter name of website")
        ID=input("Type ID")
        with open("pass.txt","a") as f:
            f.write("\n"+web+" "+ID+"\n"+str([str(getdate())])+"  "+k)