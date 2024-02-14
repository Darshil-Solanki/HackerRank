# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial as ft
values = list(map(float,input().split()))
p=values[0]/100
q=1-p
n=int(values[1])

def binomial(rbeg,rend):
    result=0.0
    for r in range(rbeg,rend+1):
        result+=(((ft(n)/(ft(n-r)*ft(r))))*(p**r)*(q**(n-r)))
    return result


print(round(binomial(0,2),3))
print(round(binomial(2,10),3))
