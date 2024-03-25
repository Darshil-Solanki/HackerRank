#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    if p<4 and q>3:
        p=4
        print("1", end=" ")
    elif p<4 and q<4:
        print("INVALID RANGE")
        return None
    else:
        pass
    f=False
    for i in range(p,q+1):
        s=str(i*i)
        if(int(s[:len(s)//2])+int(s[len(s)//2:]))==i:
            print(i,end=" ")
            f=True
    if not f:
        print('INVALID RANGE')

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
