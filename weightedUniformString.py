#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    prev = s[0]
    weight = [ord(s[0])-96]
    for i in range(1,len(s)):
        if s[i]==prev:
            weight.append(weight[len(weight)-1]+ord(s[i])-96)
        else:
            weight.append(ord(s[i])-96)
        prev = s[i]
    weight = set(weight)
    return ['Yes' if i in weight else 'No' for i in queries]


# def weightedUniformStrings(s, queries):
    # str_weights = set()
    # curr = ("", 0)
    # for l in s:
    #     curr = (l, (curr[1] if l == curr[0] else 0) + ord(l) - 96)
    #     str_weights.add(curr[1])
    
    # return ['Yes' if q in str_weights else 'No' for q in queries]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
