#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    sortedArr = sorted(arr)
    if arr == sortedArr:
        print("yes")
    else:
        idx = []
        for i in range(len(arr)):
            if sortedArr[i]!=arr[i]:
                idx.append(i)
        if len(idx)==2:
            arr.insert(idx[0], arr.pop(idx[1]))
            arr.insert(idx[1], arr.pop(idx[0]+1))
            if arr == sortedArr:
                print("yes")
                print("swap", idx[0]+1, idx[1]+1)
            else:
                print("no")
        elif len(idx)>2:
            temp = arr[:idx[0]]
            temp.extend(reversed(arr[idx[0]:idx[-1]+1]))
            temp.extend(arr[idx[-1]+1:])
            if temp == sortedArr:
                print("yes")
                print("reverse", idx[0]+1, idx[-1]+1)
            else:
                print("no")
        else:
            print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
