#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    maxLength = 0
    def validate(arr):
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
        return True
        
    uniChars = list(set(list(s)))
    for i in range(len(uniChars)-1):
        for j in range(i+1,len(uniChars)):
            temp = [c for c in s if c==uniChars[i] or c==uniChars[j]]
            if validate(temp):
                maxLength = maxLength if len(temp)<=maxLength else len(temp)
    return maxLength

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
