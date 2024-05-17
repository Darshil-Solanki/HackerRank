#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid, n):
    # Write your code here
    grid = [ sorted(list(item)) for item in grid]
    for i in range(len(grid[0])):
        col = [ grid[j][i] for j in range(n)]
        if col != sorted(col):
            return "NO"
    return "YES"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid, n)

        fptr.write(result + '\n')

    fptr.close()

