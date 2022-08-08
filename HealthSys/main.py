#a  1=rohan 2=harry 3=hammad
#b  1=food 2=exercise
def getdate():
    import datetime
    return datetime.datetime.now()
def retrieve(a,b):
    if a==1:
        if b==1:
            f=open("RohanFood.txt")
            print(f.read())
            f.close()
        elif b==2:
            f=open("RohanEx.txt")
            print(f.read())
            f.close()
    elif a==2:
        if b==1:
            f = open("HarryFood.txt")
            print(f.read())
            f.close()
        elif b == 2:
            f = open("HarryEx.txt")
            print(f.read())
            f.close()
    elif a==3:
        if b==1:
            f = open("HammadFood.txt")
            print(f.read())
            f.close()
        elif b == 2:
            f = open("HammadEx.txt")
            print(f.read())
            f.close()
def imp(a,b,c):
    if a==1:
        if b==1:
            f=open("RohanFood.txt","a")
            f.write(str([str(getdate())])+"->"+c)
            f.close()
        elif b==2:
            f=open("RohanEx.txt","a")
            f.write(str([str(getdate())])+"->"+c)
            f.close()
    elif a==2:
        if b==1:
            f=open("HarryFood.txt","a")
            f.write(str([str(getdate())])+"->"+c)
            f.close()
        elif b==2:
            f=open("HarryEx.txt","a")
            f.write(str([str(getdate())])+"->"+c)
            f.close()
    elif a==3:
        if b==1:
            f=open("HammadFood.txt","a")
            f.write(str([str(getdate())])+"->"+c)
            f.close()
        elif b==2:
            f=open("HammadEx.txt","a")
            f.write(str([str(getdate())])+"->"+c)
            f.close()
n=int(input("For data retrieval 1\nFor data input 2\n"))
if(n==1):
    a=int(input("Type 1 for Rohan\nType 2 for Harry\nType 3 for Hammad\n"))
    b=int(input("For food type 1\nFor exercise type 2\n"))
    retrieve(a,b)
elif(n==2):
    a = int(input("Type 1 for Rohan\nType 2 for Harry\nType 3 for Hammad\n"))
    b = int(input("For food type 1\nFor exercise type 2\n"))
    if(b==1):
        c=input("Food ingested")
        imp(a,b,c)
    elif(b==2):
        c=input("Exercise completed")
        imp(a,b,c)