import math
n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))

for i in num:
    if(i==1):
        print("Not prime")
        continue
    if(i==2):
        print("Prime")
        continue
    if(i%2==0):
        print("Not prime")
        continue
    for j in range(3, int(math.sqrt(i))+1,2):
        if(i%j==0):
            print("Not prime")
            break
    else:
        print("Prime")