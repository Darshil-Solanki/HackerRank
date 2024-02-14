# Enter your code here. Read input from STDIN. Print output to STDOUT
values = list(map(int,input().split()))
p=values[0]/values[1]
q=1-p
n=int(input())

def negBinomial(p,q,n):
    return (q**(n-1))*p

print(round(negBinomial(p,q,n),3))
