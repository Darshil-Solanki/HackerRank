#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    res = [[] for _ in range(len(arr)//2)]
    
    for i, l in enumerate(arr):
        res[int(l[0])].append(l[1] if i >= (len(arr) / 2) else '-')
        
    print(' '.join(' '.join(subarr) for subarr in res if subarr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
