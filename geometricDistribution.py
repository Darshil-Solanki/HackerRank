from math import factorial as ft
values = list(map(int,input().split()))
p=values[0]/values[1]
q=1-p
n=int(input())

def negBinomial(p,q,n):
    result=0
    for r in range(1,n+1):
        result+=((q**(r-1))*p)
    return result

print(round(negBinomial(p,q,n),3))
