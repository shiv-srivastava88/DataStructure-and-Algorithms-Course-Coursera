# Uses python3
import sys

def subsetSum(A, val):
    n = len(A)
    res = [[False for i in range(val+1)] for j in range(n+1)]

    for i in range(n+1):
        res[i][0] = True 

    for i in range(n+1):
        for j in range(val+1):

            if j < A[i-1]:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = res[i-1][j-l[i-1]] or res[i-1][j]

    if res[n][val] == True:
        return 1
    else: return 0

def partition3(A):
    
    if sum(A) % 3 != 0:
        return 0
    
    return subsetSum(A, sum(A) // 3)


n = int(input())
l = list(map(int, input().split()))
print(partition3(l))

