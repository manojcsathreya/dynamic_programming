'''
arr = [1,2,3]
T = 7
def func(ind, T):
    if ind == 0:
        if T % arr[0] == 0:
            return T // arr[0]
        else:
            return float("inf")
    
    notTake = 0 + func(ind-1, T)
    take = float("inf")
    if arr[ind] <= T:
        take = 1 + func(ind, T - arr[ind])
    return min(take, notTake)

print(func(len(arr)-1,  T))
'''
'''
arr = [1,2,3]
T = 7
n = len(arr)
dp = [[-1 for _ in range(T+1)] for _ in range(n)]
def func(ind, T):
    if ind == 0:
        if T % arr[0] == 0:
            return T // arr[0]
        else:
            return float("inf")
    if dp[ind][T] != -1:
        return dp[ind][T]
    notTake = 0 + func(ind-1, T)
    take = float("inf")
    if arr[ind] <= T:
        take = 1 + func(ind, T - arr[ind])
    dp[ind][T] = min(take, notTake)
    return dp[ind][T]

print(func(len(arr)-1,  T))
'''
'''
arr = [1,2,3]
t = 7
n = len(arr)
dp = [[-1 for _ in range(t+1)] for _ in range(n)]
for i in range(t+1):
    if i % arr[0] == 0:
        dp[0][i] = i // arr[0]
    else:
        dp[0][i] = float("inf")
    for ind in range(1,n):
        for T in range(t+1):
            notTake = 0 + dp[ind-1][T]
            take = float("inf")
            if arr[ind] <= T:
                take = 1 + dp[ind][T - arr[ind]]
            dp[ind][T] = min(take, notTake)

print(dp)
'''
arr = [1,2,5]
t = 11
n = len(arr)
prev = [-1 for _ in range(t+1)]
cur = [-1 for _ in range(t+1)]
for i in range(t+1):
    if i % arr[0] == 0:
        prev[i] = i // arr[0]
    else:
        prev[i] = float("inf")
for ind in range(1,n):
    for T in range(t+1):
        notTake = 0 + prev[T]
        take = float("inf")
        if arr[ind] <= T:
            take = 1 + cur[T - arr[ind]]
        cur[T] = min(take, notTake)
    prev = cur 

print(prev)
