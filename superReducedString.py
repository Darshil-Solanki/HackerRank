#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    prev = s[0]
    res = ""
    count = 1
    for i in range(1,len(s)):
        if s[i]==prev:
            count+=1
            if i == len(s)-1:
                if count%2!=0:
                    res+=prev
                if len(res)>=2 and res[-1] == res[-2]:
                    res=res[:-2]
        else:
            if count%2!=0:
                res+=prev
            if len(res)>=2 and res[-1] == res[-2]:
                res=res[:-2]
            if i==len(s)-1 and res[-1] == s[i]:
                res=res[:-1]
            elif i==len(s)-1 and count%2!=0:
                res+=s[i]
            count=1
            prev = s[i]
    return "Empty String" if res=="" else res
    
# def superReducedString(s):
#     temp = []
#     for c in s:
#         if len(temp)>0 and c==temp[-1]:
#             temp.pop()
#             continue
#         temp.append(c)
#     return "".join(temp) if temp else "Empty String"
    
# regex = re.compile(r'([a-z])\1')

# def superReducedString(s):
#     prev = s
#     while True:
#         res = regex.sub('', prev)
#         if prev == res:
#             break
#         else:
#             prev = res
        
#     return 'Empty String' if not res else res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
