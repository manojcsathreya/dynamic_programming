# 01 KnapSack
'''
wt = [1,2,4,5]
val = [5, 4, 8, 6]
def func(ind, W):
    if ind == 0:
        if (wt[ind] <= W):
            return val[ind]
        else:
            return 0
        
    notTake = 0 + func(ind-1, W)
    take = 0
    if wt[ind] <= W:   
        take = val[ind] + func(ind-1, W- wt[ind])
    
    return max(take, notTake)

print(func(3,5))
'''
'''
wt = [1,2,4,5]
val = [5, 4, 8, 6]
W = 5
ind = 3
dp = [[-1 for _ in range(W+1)] for _ in range(ind+1)]
def func(ind, W):
    if ind == 0:
        if (wt[ind] <= W):
            return val[ind]
        else:
            return 0
        
    if dp[ind][W] != -1:
        return dp[ind][W]
    notTake = 0 + func(ind-1, W)
    take = 0
    if wt[ind] <= W:   
        take = val[ind] + func(ind-1, W- wt[ind])
    dp[ind][W] = max(take, notTake)
    return dp[ind][W]

print(func(ind, W))
'''
'''
wt = [1,2,4,5]
n = len(wt)
val = [5, 4, 8, 6]
w = 5
ind = 3
dp = [[0 for _ in range(w+1)] for _ in range(ind+1)]
for i in range(wt[0],w):
    dp[0][i] = val[0]

for ind in range(1,n):
    for W in range(w+1):
        notTake = 0 + dp[ind-1][W]
        take = 0
        if wt[ind] <= W:   
            take = val[ind] + dp[ind-1][W- wt[ind]]
        dp[ind][W] = max(take, notTake)
    

print(dp[-1][-1])
'''

wt = [1,2,4,5]
n = len(wt)
val = [5, 4, 8, 6]
w = 5
ind = 3
prev = [0 for _ in range(w+1)]
for i in range(wt[0],w):
    prev[i] = val[0]
cur = [0 for _ in range(w+1)]
for ind in range(1,n):
    for W in range(w, -1, -1):
        notTake = 0 + prev[W]
        take = 0
        if wt[ind] <= W:   
            take = val[ind] + prev[W- wt[ind]]
        prev[W] = max(take, notTake)

print(prev)
