#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the xorSequence function below.
def getXOR(n):
    num = n%8
    if num==0 or num==1: return n
    if num==2 or num==3: return 2
    if num==4 or num==5: return n+2
    return 0
    
def xorSequence(l, r):
    return getXOR(r)^getXOR(l-1)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()

