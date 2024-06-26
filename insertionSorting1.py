#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(n-1, -1, -1):
        key = arr[i]
        j= i-1
        flag = False
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            print(*arr)
            flag = True
            j-=1
        arr[j+1]=key
        if flag:
            print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
