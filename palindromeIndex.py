#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    n = len(s)
    for i in range(n//2):
        if s[i] != s[-(i+1)]:
            firstSub = s[:i] + s[i+1:]
            secondSub = s[:n-i-1] + s[n-i:]
            if firstSub == firstSub[::-1]:
                return i
            if secondSub == secondSub[::-1]:
                return n-i-1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
