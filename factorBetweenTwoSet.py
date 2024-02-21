#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    num=0
    li=[]
    for i in range(a[len(a)-1],b[0]+1,a[len(a)-1]):
        for j in a:
            if(i%j!=0):
                break
        else:
            li.append(i)
    for i in li:
        for j in b:
            if(j%i!=0):
                break
        else:
            num+=1
    return num
    # start,end=max(a),min(b)
    # factors=[i for i in range(start,end+1) if all(i%x==0 for x in a)]
    # second_factors=[i for i in factors if all(x%i==0 for x in b)]
    # return len(second_factors)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
