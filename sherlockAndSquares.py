#!/bin/python3

import math
import os
import random
import re
import sys
import math
#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    squares=[ i*i for i in range(int(math.sqrt(a)),int(math.sqrt(b))+1)]
    c=0
    for i in squares:
        if(a<=i<=b):
            c+=1
    return c

# def squares(a, b):
#     lowSqrt = int(math.ceil(math.sqrt(a)))
#     highSqrt = int(math.floor(math.sqrt(b)))
#     return highSqrt-lowSqrt+1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
