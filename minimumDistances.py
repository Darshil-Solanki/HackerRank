#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    uA = set(a)
    md, flag = len(a)-1, False
    for i in uA:
        if a.count(i)==2:
            fi = a.index(i)
            si = a.index(i, fi+1)
            if si-fi<=md:
                md=si-fi
                flag=True
    return md if flag else -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
