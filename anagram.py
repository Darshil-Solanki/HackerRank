#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s)%2!=0:
        return -1
    flist = list(s[:len(s)//2])
    slist = list(s[(len(s)//2):])
    count = 0
    for i in flist:
        if i in slist:
            slist.remove(i)
        else:
            count+=1
    return count

# def anagram(s):
#     d = len(s)
#     if d%2:
#         return -1
#     a, b, c = s[:d//2], s[d//2:], 0
#     for e in set(a).intersection(b):
#         c += min(a.count(e), b.count(e))
#     return d//2 - c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
