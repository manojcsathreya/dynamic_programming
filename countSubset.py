'''
arr = [1, 2, 2, 3]
def func(ind, target):
    if target == 0:
        return 1
    if ind == 0:
        return 1 if arr[ind] == target else 0
    
    notTake = func(ind-1, target)
    take = 0
    if arr[ind] <= target:
        take = func(ind-1, target-arr[ind])
    
    return take + notTake

print(func(3,3))
'''
'''
arr = [1, 2, 2, 3]
k = 3
n = len(arr)
dp = [[-1 for _ in range(k+1)] for _ in range(n)]
def func(ind, target):
    if target == 0:
        return 1
    if ind == 0:
        return 1 if arr[ind] == target else 0
    
    if dp[ind][target] != -1:
        return dp[ind][target]
    notTake = func(ind-1, target)
    take = 0
    if arr[ind] <= target:
        take = func(ind-1, target-arr[ind])
    
    dp[ind][target] = take + notTake
    return dp[ind][target]

print(func(3,3))
'''
'''
arr = [1, 2, 2, 3]
k = 3
n = len(arr)
dp = [[0 for _ in range(k+1)] for _ in range(n)]
target = 3
for i in range(n):
    dp[i][0] = 1

dp[0][arr[0]] = 1
    
for ind in range(1, n):
    for target in range(1,k+1): 
        notTake = dp[ind-1][target]
        take = 0
        if arr[ind] <= target:
            take = dp[ind-1][target-arr[ind]]
        dp[ind][target] = take + notTake


print(dp)
'''
arr = [1, 2, 2, 3]
k = 3
n = len(arr)
prev = [0 for _ in range(k+1)]

prev[0] = 1

prev[arr[0]] = 1
    
for ind in range(1, n):
    cur = [0 for _ in range(k+1)]
    cur[0] = 1
    for target in range(1,k+1): 
        notTake = prev[target]
        take = 0
        if arr[ind] <= target:
            take = prev[target-arr[ind]]
        cur[target] = take + notTake
    prev = cur

print(cur)
