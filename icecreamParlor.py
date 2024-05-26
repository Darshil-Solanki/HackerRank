#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr, n):
    # Write your code here
    remainder = [-1]*10001
    for i in range(n):
        x = arr[i]
        y = m -x
        if y>-1:
            if remainder[y]!=-1:
                return [remainder[y]+1, i+1]
        remainder[x]=i
            
        
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr, n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
