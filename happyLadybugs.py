#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    c = collections.Counter(b)
    for i in (v for k, v in c.items() if 64<ord(k)<91 ):
        if i < 2:
            return "NO"

    shuffled = [i for i in c if b.find(2*i) < 0]

    if '_' not in c and shuffled:
        return "NO"
 
    return "YES"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
