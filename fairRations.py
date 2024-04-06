#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Write your code here
    d = {i:val for i, val in enumerate(B) if val % 2}
    if len(d) % 2:
        return "NO"
    return str(sum(list(d.keys())[i]-list(d.keys())[i-1] for i in range(1, len(d)+1, 2)) * 2)
#code by https://www.hackerrank.com/anna_nagy98
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
