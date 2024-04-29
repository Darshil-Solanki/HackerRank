#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    tempSNum = tempStr = None
    n = len(s)
    for i in range(1, (len(s)//2)+1):
        if s==tempStr:
            print(f"YES {tempSNum}")
            return 0
           
        tempSNum = tempStr = s[0:i]
        j = 1
        while(len(tempStr) < n):
            tempStr += str(int(tempSNum)+j)
            j+=1
    print("YES "+str(tempSNum) if s==tempStr else "NO")
         
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
