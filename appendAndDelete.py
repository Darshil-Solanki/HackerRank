#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    i=0
    for i in range(min(len(t),len(s))):
        if(s[i]!=t[i]):
            break
    else:
        opMinusremainChang=k-abs(len(s)-len(t))
        return "Yes" if ( opMinusremainChang >(2*min(len(s),len(t))) or opMinusremainChang%2==0 ) else "No"
    return "No" if ( ((len(s)-i)+(len(t)-i))>k ) else "Yes"
    
# def appendAndDelete(s, t, k):
#     common_length = 0
#     for i in range(min(len(s), len(t))):
#         if s[i] == t[i]:
#             common_length += 1
#         else:
#             break

#     total_operations = len(s) + len(t) - 2 * common_length
    
#     if k >= len(s) + len(t) or (k >= total_operations and (k - total_operations) % 2 == 0):
#         return 'Yes'
#     else:
#         return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
