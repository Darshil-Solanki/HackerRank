#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    left = list(s[:n//2])
    right = list(s[n//2+1:][::-1]) if n % 2==1 else list(s[n//2:][::-1])
    diff = 0
    length = len(left)
    for i in range(length):
        if left[i]!=right[i]:
            diff += 1
    for i in range(length):
        leftNum = left[i]
        rightNum = right[i]
        if leftNum==rightNum:
            if leftNum=='9':
                continue
            if k-2 >= diff:
                left[i], right[i] = '9', '9'
                k-=2
        elif leftNum!=rightNum:
            if leftNum=='9':
                if k-1>=diff-1:
                    right[i]='9'
                    diff-=1
                    k-=1
                else:
                    return '-1'
            elif rightNum == '9':
                if k-1>=diff-1:
                    left[i]='9'
                    diff-=1
                    k-=1
                else:
                    return '-1'
            else:
                if k-2>=diff-1:
                    left[i]='9'
                    right[i]='9'
                    k-=2
                    diff-=1
                elif k-1>=diff-1:
                    if leftNum>rightNum:
                        right[i]=leftNum
                    else:
                        left[i]=rightNum
                    diff-=1
                    k-=1
                else:
                    return '-1'
    if n%2 == 0: 
        return "".join(left+(right[::-1]))
    else:
        mid = ['9'] if k>0 else [s[n//2]]
        return "".join(left+mid+(right[::-1]))
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
