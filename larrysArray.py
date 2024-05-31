#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Write your code here
    SA = sorted(A)
    for i in range(len(A)-2):
        idx = A.index(i+1)
        if (idx-i)%2==0:
            A.insert(i, A.pop(idx))
        else:
            A.insert(i, A.pop(idx))
            A[i+1],A[i+2]=A[i+2],A[i+1]
    return "YES" if A == SA else "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()

