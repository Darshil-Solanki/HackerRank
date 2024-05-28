#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    total = 0
    n = len(matrix)
    for i in range(n//2):
        for j in range(n//2):
            possible = []
            possible.append(matrix[i][j])
            possible.append(matrix[i][n-1-j])
            possible.append(matrix[n-1-i][j])
            possible.append(matrix[n-1-i][n-1-j])
            total += max(possible)
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()

