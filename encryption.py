#!/bin/python3

from math import *
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s="".join(s.split())
    n=len(s)
    r = floor(sqrt(n))
    c = ceil(sqrt(n))
    temp=""
    for i in range(c):
        j=0
        while((i+(j*c))<n):
            temp+=s[i+(j*c)]
            j+=1
        temp+=" "
    return temp
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
