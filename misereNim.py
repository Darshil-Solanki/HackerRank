#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # Write your code here
    if len(s)==sum(s):
        return "First" if len(s)%2==0 else "Second"
    total = 0
    for i in s:
        total ^=i
    return "First" if total else "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()

