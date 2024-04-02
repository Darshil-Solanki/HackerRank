#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#
def chocolateFeast(n, c, m):
    # Write your code here
    bars = n//c
    n//=c
    rem=0
    while n+rem>m:
        c, r = divmod(n+rem, m)
        bars+=c
        n=c
        rem = rem+r if rem == 0 else r
    if n+rem==m:
        bars+=1
    return bars
    
# def chocolateFeast(n, c, m):
#     wrappers = n//c
#     bar = n//c 
#     while True:
#         if wrappers < m:
#             break
#         bar = bar + (wrappers // m)
#         wrappers = sum(divmod(wrappers, m))
#     return int(bar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
