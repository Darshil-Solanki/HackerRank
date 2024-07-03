#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    n = len(s1)
    table = [[0]*(n+1) for i in range(n+1)]
    for i in range(n):
        for j in range(n):
           table[i+1][j+1]= table[i][j]+1  if s1[i]==s2[j] else max(table[i+1][j], table[i][j+1])
    return table[n][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
