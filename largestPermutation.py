#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(n, k, arr):
    # Write your code here
    position_map = { value: idx for idx, value in enumerate(arr)}
    current_max = max(arr)
    for i in range(n):
        if k==0:
            break
        if arr[i]!=current_max:
            arr[i], arr[position_map[current_max]] = current_max, arr[i]
            position_map[arr[position_map[current_max]]] = position_map[current_max]
            position_map[current_max] = i
            k-=1
        current_max -= 1
    return arr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(n, k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

