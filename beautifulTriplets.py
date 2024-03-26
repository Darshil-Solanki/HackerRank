#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    if len(arr)<3:
        return 0
    else:
        count=0
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                if arr[j]-arr[i]==d:
                    for k in range(j+1,len(arr)):
                        if arr[k]-arr[j]==d:
                            count+=1
        return count 

#better version from discussion in hackerrank
# n,d=map(int,input().split())
# seq=list(map(int,input().split()))
# print(sum([(i+d in seq and i-d in seq) for i in seq]))
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
