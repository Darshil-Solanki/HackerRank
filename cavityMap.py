#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    if len(grid)<3:
        return grid
    newCavity = [grid[0]]
    for i in range(1, len(grid)-1):
        temp=[grid[i][0]]
        for j in range(1, len(grid)-1):
            if grid[i-1][j] < grid[i][j] and grid[i][j-1] < grid[i][j] and grid[i][j+1] < grid[i][j] and grid[i+1][j]<grid[i][j]:
                temp.append('X')
            else:
                temp.append(grid[i][j])
        temp.append(grid[i][-1])
        newCavity.append("".join(temp))
    newCavity.append(grid[-1])
    return newCavity

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
