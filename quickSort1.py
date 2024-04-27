#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def partition(arr, beg, end):
    pivot = arr[beg]
    i = beg+1
    j = end
    while(i<=j):
        while(i<=end and arr[i]<=pivot):
            i+=1
        while (arr[j]>pivot):
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[beg],arr[j] = arr[j],arr[beg]
    return j

def sorting(arr, beg, end):
    if beg<end:
        p = partition(arr, beg, end)
        sorting(arr, beg, p-1)
        sorting(arr, p+1, end)
        
def quickSort(arr):
    # Write your code here
    sorting(arr, 0, len(arr)-1)
    return arr
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
