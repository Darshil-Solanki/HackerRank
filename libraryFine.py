#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    rd=datetime.date(y1,m1,d1)
    dd=datetime.date(y2,m2,d2)
    diff=(rd-dd).days
    print(diff)
    if y1>y2:
        return 10_000
    if diff<=0:
        return 0
    elif diff<=30:
        return 15*diff
    elif diff<=365:
        return 500*(m1-m2)
    else:
        pass
        
# def libraryFine(d1, m1, y1, d2, m2, y2):
#     if y1 > y2:
#         return 10000
#     elif y1 == y2 and m1 > m2:
#         return 500 * (m1 - m2)
#     elif y1 == y2 and m1 == m2 and d1 > d2:
#         return 15 * (d1 - d2)
#     else:
#         return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
