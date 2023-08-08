#climbing stairs
'''
recursion
def func(ind):
    if ind == 0 or ind == 1:
        return 1
    firstStep  = func(ind-1)
    secondStep  = func(ind-2)
    return firstStep + secondStep

print(func(4))
'''
# Memoization
'''
n = 4
dp = [-1 for _ in range(n)]
def func(ind):
    if ind == 0 or ind == 1:
        return 1
    if dp[ind-1] != -1:
        return dp[ind-1]
    if dp[ind-2] != -1:
        return dp[ind-2]
    return func(ind-1) + func(ind-2)

print(func(n))
'''
#Tabulation
'''
n = 4
dp = [-1 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
'''

# SPace optimization
n = 5
dpZero = 1
dpOne = 1
for i in range(2, n+1):
    temp = dpOne + dpZero
    dpZero = dpOne
    dpOne = temp

print(dpOne)
