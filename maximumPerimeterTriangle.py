#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations 
#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    combos = combinations(sticks, 3)
    triangles = [comb for comb in combos if comb[0]+comb[1]>comb[2] and comb[1]+comb[2]>comb[0] and comb[2]+comb[0]>comb[1]]
    area = [ sum(comb) for comb in triangles ]
    return sorted(triangles[area.index(max(area))]) if triangles else [-1]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

