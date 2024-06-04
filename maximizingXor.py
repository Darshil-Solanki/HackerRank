#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    # Write your code here
    return max([i^j for i in range(l, r+1) for j in range(i, r+1)])
    # maxVal = float('-inf')
    # for i in range(l, r+1):
    #     for j in range(i, r+1):
    #         if i ^ j >maxVal:
    #             maxVal = i ^ j
    # return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()

