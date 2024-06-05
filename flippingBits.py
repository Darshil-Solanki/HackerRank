#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    # return int(''.join('1' if bit == '0' else '0' for bit in format(n, "032b")), 2)
    num=''
    num += (32-len(bin(n))+2)*'1'
    for i in bin(n)[2:]:
        if i=='1':
            num+='0'
        else:
            num+='1'
    return int(num, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

