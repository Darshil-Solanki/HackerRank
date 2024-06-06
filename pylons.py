#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr, n):
    # Write your code here
    count = 0
    try:
        prevPlant = k-list(reversed(arr[:k])).index(1)
        count = 1
    except ValueError:
        return -1
    while prevPlant+k-1<n:
        try:
            prevPlant += 2*(k-1)-list(reversed(arr[prevPlant:prevPlant+2*k-1])).index(1)+1
            count += 1
        except ValueError:
            return -1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()

