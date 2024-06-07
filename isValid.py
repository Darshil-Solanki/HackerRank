#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    counter = [s.count(i) for i in "abcdefghijklmnopqrstuvwxyz"]
    c = Counter(counter)
    if 0 in c:
        c.pop(0)
    if len(c)>2:
        return "NO"
    if len(c)==1:
        return "YES"
    else:
        val = list(c.items())
        val.sort(key=lambda x: x[1], reverse=True)
        if abs(val[1][0]*val[1][1] - val[0][0]) == 1 or val[1][0]*val[1][1] == 1:
            return "YES"
        return "NO"
        
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

