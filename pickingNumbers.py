#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# pick number such that the subarray generated has an absolute difference of consecutive no. is less than or equal to 1. 

def pickingNumbers(a):
    # Write your code here
    unique_a = list(set(a)) # get unique value from list a
    unique_a.sort()
    cnt = Counter(a)
    print(cnt)
    max_counter = 0
    temp = 0
    prev = 0
    for value in unique_a:
        if value - prev != 1:
            temp = 0
        if temp + cnt[value] > max_counter:
            max_counter = temp + cnt[value]
        temp = cnt[value]
        prev = value
    return max_counter
    # result=1
    # for i in range(len(a)-1):
    #     j=i
    #     length=2
    #     while j<len(a)-1 and abs(a[j]-a[j+1])<=1:
    #         j+=1
    #         length+=1
    #     else:
    #         result= length if(length>result) else result
    # return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
