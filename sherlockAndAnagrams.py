#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from collections import defaultdict

def sherlockAndAnagrams(s):
    n = len(s)
    anagram_count = 0
    substring_map = defaultdict(int)
    
    # Iterate over all possible substrings
    for length in range(1, n):
        # Generate all substrings of current length
        for start in range(n - length + 1):
            substr = ''.join(sorted(s[start:start + length]))
            substring_map[substr] += 1
    
    # Count anagrammatic pairs
    for count in substring_map.values():
        anagram_count += count * (count - 1) // 2
    
    return anagram_count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

