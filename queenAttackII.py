#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    obstacle = {(ob[0],ob[1]) for ob in obstacles} #unique set of obstacle coordinates
    
    sides, count = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)],0 #eight side and count
    
    for mv in sides:
        q_cr, q_cc = r_q,c_q
        while((q_cr+mv[0]>=1 and q_cr+mv[0]<=n) and (q_cc+mv[1]>=1 and q_cc+mv[1]<=n)):
            q_cr+=mv[0]
            q_cc+=mv[1]
            if (q_cr,q_cc) in obstacle: break
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
