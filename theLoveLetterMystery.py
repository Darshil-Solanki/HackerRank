#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def LLM(s):
	return sum(abs(ord(s[i])-ord(s[-i-1])) for i in range(len(s)//2))

def theLoveLetterMystery(s):
    # Write your code here
    if s == s[::-1]:
        return 0
    first = s[:len(s)//2]
    second = s[(len(s)//2)+1:] if len(s)%2!=0 else s[len(s)//2:]
    op = 0
    for i,j in zip(first,second[::-1]):
        op += abs(ord(i)-ord(j))
    return op

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
