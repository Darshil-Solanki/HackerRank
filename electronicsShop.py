#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards.sort()
    drives.sort()
    maxSum=0
    for i in reversed(keyboards):
        if(i<b):
            for j in reversed(drives):
                if((i+j)<=b and i+j>maxSum):
                    maxSum=i+j
    return maxSum if maxSum!=0 else -1
    #    return max(
    #     [m + n for m in keyboards for n in drives if m + n <= b] + [-1]
    # )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
