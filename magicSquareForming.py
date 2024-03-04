#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
#given 3x3 maatrix according to the formula n(n^2+1)/2 
#we get 15. so find all the possibilities of sum 15 between the range [ 1,9] .
#the possibilities are 1+9+5 2+8+5 3+7+5 4+6+5 4+3+8 6+2+7 6+1+8 9+2+4
#now we gonna keep the five number at center of the matrix and
#edges will be 1,9,3,7 corners will be 2,6,8,4 
#now we will see the code according to this logic 

def formingMagicSquare(s):
    # Write your code here
    pos=[[[4,3,8],[9,5,1],[2,7,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[8,1,6],[3,5,7],[4,9,2]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,7,6],[9,5,1],[4,3,8]],
        [[6,1,8],[7,5,3],[2,9,4]]
        ]
    diffList=[]
    for item in pos:
        diff=0
        for i in range(3):
            for j in range(3):
                diff+=abs(item[i][j]-s[i][j])
        diffList.append(diff)
    return min(diffList)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
