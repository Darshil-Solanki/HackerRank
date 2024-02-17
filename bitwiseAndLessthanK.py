#Task
# Given set . Find two integers,  and  (where ), from set  such that the value of  is the maximum possible and also less than a given integer, . In this case,  represents the bitwise AND operator.

# Function Description
# Complete the bitwiseAnd function in the editor below.

# bitwiseAnd has the following paramter(s):
# - int N: the maximum integer to consider
# - int K: the limit of the result, inclusive

# Returns
# - int: the maximum value of  within the limit.
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#Sample Input

# STDIN   Function
# -----   --------
# 3       T = 3
# 5 2     N = 5, K = 2
# 8 5     N = 8, K = 5
# 2 2     N = 8, K = 5
# Sample Output

# 1
# 4
# 0

def bitwiseAnd(N, K):
    # Write your code here
    maxValue=0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            curValue=i&j
            if(curValue<K and curValue>maxValue):
                maxValue=curValue            
    return maxValue
    



t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    count = int(first_multiple_input[0])

    lim = int(first_multiple_input[1])

    res = bitwiseAnd(count, lim)
    print(res)

