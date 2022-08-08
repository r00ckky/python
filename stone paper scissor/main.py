import random
dic={"scissor":{"stone":1,"paper":0},"stone":{"scissor":0,"paper":1},"paper":{"stone":0,"scissor":1}}
l=["scissor","stone","paper"]
n=10
com=0
you=0
while(n>0):
    n-=1
    k=input()
    f=random.choice(l)
    print(f)
    if(f==k):
        continue
    else:
        for p,q in dic.items():
            if f==p:
                for g in q:
                    if(q==k):
                        if(q[g]==1):
                            you+=1
                            break
                        else:
                            com+=1
                            break
if(com>you):
    print("You lost")
elif(com<you):
    print("You win")
else:
    print("Tie")