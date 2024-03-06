#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    newRank=[]
    uniqueRank = list(set(ranked))
    uniqueRank.sort(reverse=True)
    for score in player:
        newRank.append(find_rank(score,uniqueRank))
    return newRank

def find_rank(score,uniqueRank,mid=None):
    low=0;high=len(uniqueRank)-1
    if(uniqueRank[low]<=score):
        return 1
    elif(uniqueRank[high]==score):
        return high+1
    elif(uniqueRank[high]>score):
        return high+2
    else:
        pass
    
    while low<=high:
        mid = (low+high)//2
        if uniqueRank[mid]==score:
            return mid+1
        elif uniqueRank[mid]<score:
            high = mid-1
        else:
            low = mid+1
    return low+1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
