#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    result = []
    arr.sort()
    minDiff = float('inf')
    
    for i in range(len(arr)-1):
        minDiff = min(abs(arr[i]-arr[i+1]),minDiff)
    
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])==minDiff:
            result.extend([arr[i],arr[i+1]])
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
