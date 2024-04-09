#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
    pRow = 0
    prevIndex = -1
    for i in range(len(G)):
        start = 0
        while True:
            if P[pRow] not in G[i][start:]:
                break
            count = 1
            for j in range(1,len(P)):
                if i+j< len(G) and P[j]==G[i+j][start:start+len(P[j])]:
                    count+=1
                if count == len(P):
                    return "YES"
            start+=1
    return "NO"

# def gridSearch(G, P):
#     for i in range(len(G) - len(P) + 1):
#         first_line = re.finditer(f'(?={P[0]})', G[i])
#         rest_lines = []
#         for line in range(1, len(P)):
#             rest_lines.append(list(match.start() for match in re.finditer(f'(?={P[line]})', G[i + line])))
#         for match in first_line:
#             if all(match.start() in result for result in rest_lines):
#                 return "YES"
#     return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
