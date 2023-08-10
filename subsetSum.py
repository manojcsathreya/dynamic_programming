'''
arr = [6,2,3,4]
target = 19
def func(ind, target):
    if target == 0:
        return True
    if ind == 0:
        return arr[0] == target

    notTake =  func(ind-1, target)
    take = False
    if arr[ind] <= target:
        take = func(ind-1, target-arr[ind])
    
    return take or notTake

print(func(3,target))
'''
'''
arr = [6,2,3,4]
k = 3
n = len(arr)
dp = [[-1 for _ in range(k + 1)]for _ in range(n)]
def func(ind, target):
    if target == 0:
        return True
    if ind == 0:
        return arr[0] == target
    
    if dp[ind][target] != -1:
        return dp[ind][target]
    
    notTake =  func(ind-1, target)
    take = False
    if arr[ind] <= target:
        take = func(ind-1, target-arr[ind])
    
    dp[ind][target] = take or notTake
    return dp[ind][target]

print(func(n-1,k))
'''
'''
arr = [6,2,3,4]
k = 1
n = len(arr)
dp = [[False for _ in range(k + 1)]for _ in range(n)]

for i in range(n):
    dp[i][0] = True

if arr[0] <= k:
    dp[0][arr[0]] = True

for ind in range(n):
    for target in range(k+1):
        notTake =  dp[ind-1][target]
        take = False
        if arr[ind] <= target:
            take = dp[ind-1][target-arr[ind]]
        dp[ind][target] = take or notTake

print(dp[-1][-1])
'''
arr = [6,2,3,4]
k = 20
n = len(arr)
prev = [False for _ in range(k + 1)]


for i in range(n):
    prev[0] = True

if arr[0] <= k:
    prev[arr[0]] = True

for ind in range(n):
    cur = [False for _ in range(k + 1)]
    cur[0] = True
    for target in range(k+1):
        notTake =  prev[target]
        take = False
        if arr[ind] <= target:
            take = prev[target-arr[ind]]
        cur[target] = take or notTake
    prev = cur 

print(cur)
