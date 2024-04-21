#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    nFlag = lFlag = uFlag = scFlag = True
    for i in password:
        if i in numbers:
            nFlag = False
        elif i in lower_case:
            lFlag = False
        elif i in upper_case:
            uFlag = False
        else:
            scFlag = False
    mn=0
    if nFlag:
        mn+=1
    if lFlag:
        mn+=1
    if uFlag:
        mn+=1
    if scFlag:
        mn+=1
    mn = (mn if 6-n<mn else 6-n) if n<6 else mn
    return mn
    
# def minimumNumber(n, password):
#     count = 0
#     special_characters = "!@#$%^&*()-+"
#     if not any(char.isdigit() for char in password):
#         count += 1
#     if not any(char.islower() for char in password):
#         count += 1
#     if not any(char.isupper() for char in password):
#         count += 1
#     if not any(char in special_characters for char in password):
#         count += 1
#     min_length = max(0, 6 - n)
#     return max(count, min_length)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
