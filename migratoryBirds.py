#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
144453
1345
def migratoryBirds(arr):
    # Write your code here
    mostSighted=None
    maxCount=0
    newArr=list(set(arr))
    print(newArr)
    for i in newArr:
        if(arr.count(i)>maxCount):
            maxCount=arr.count(i)
            if(mostSighted == None):
                mostSighted=i
            else:
                mostSighted=i
        if(arr.count(i)==maxCount):
            if(mostSighted>i):
                mostSighted=i
    return mostSighted
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
