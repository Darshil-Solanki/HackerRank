#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here

    def explode(gr):
        bombs = [(i, j) for i, line in enumerate(gr) for j in range(len(line)) if gr[i][j] == 'O']
        deton = [(i + 1, j) for i, j in bombs if i + 1 < len(gr)]
        deton = deton + [(i, j + 1) for i, j in bombs if j + 1 < len(gr[0])]
        deton = deton + [(i - 1, j) for i, j in bombs if i - 1 >= 0]
        deton = deton + [(i, j - 1) for i, j in bombs if j - 1 >= 0]
        gri = ['O' * len(grid[0])] * len(grid)
        for i, j in bombs + deton:
            gri[i] = gri[i][0: j] + '.' + gri[i][j + 1:len(gri[i])]
        return gri
    
    if 0 <= n <= 1:
        return grid
    
    if n % 2 <= 0:
        return ['O' * len(grid[0])] * len(grid)
    
    if n % 4 == 1:
        return explode(explode(grid))
        
    if n % 4 == 3:
        return explode(grid)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
