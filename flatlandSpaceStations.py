#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
# def flatlandSpaceStations(n, m, c):
    # if len(c) == n:
    #     return 0  # All cities have a space station

    # c.sort()  # Sort space station locations
    # maximum = max(c[0], n - 1 - c[-1])  # Maximum distance to the nearest space station
    
    # for i in range(1, len(c)):
    #     distance = (c[i] - c[i - 1]) // 2  # Calculate distance between adjacent space stations
    #     maximum = max(maximum, distance)
    
    # return maximum
def flatlandSpaceStations(n, m, c):
    if len(c)==n:
        return 0
    c.sort()
    mx = max(c[0],n-1-c[-1])    
    for i in range(m-1):
        if (c[i+1]-c[i])//2>mx:
            mx=(c[i+1]-c[i])//2
    return mx

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, m, c)

    fptr.write(str(result) + '\n')

    fptr.close()
