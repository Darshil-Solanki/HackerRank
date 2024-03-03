#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if(abs(z-x) == abs(z-y)):
        return "Mouse C"
    elif(abs(z-x) < abs(z-y)):
        return "Cat A"
    else:
        return "Cat B"
    #return 'Cat B' if abs(y-z) < abs(x-z) else( 'Cat A' if abs(x-z) < abs(y-z) else 'Mouse C')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
