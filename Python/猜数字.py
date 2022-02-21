import random
print("First Python")
time=3
Key=random.randint(1,10) #随机数
while time!=0:
    num=input("gess number")
    gess=int(num)
    if(gess<Key):
         print("small")
    elif(gess>Key):
         print("big")
    else:
         print("Yes")
         break
    time-=1
print("end Game")
while input():
    break
