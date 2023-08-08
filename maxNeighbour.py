'''
a = [2,1,4,9]
def func(ind):
    if ind == 0:
        return a[ind]
    if ind < 0:
        return 0
    pick = a[ind] + func(ind-2)
    notPick = 0 + func(ind -1)
    return max(pick, notPick)

print(func(len(a)-1))
'''
'''
a = [2,1,4,9]
dp = [-1 for _ in range(len(a))]

def func(ind):
    if ind == 0:
        return a[ind]
    if ind < 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    pick = a[ind] + func(ind-2)
    notPick = 0 + func(ind -1)
    dp[ind] = max(pick, notPick)
    return dp[ind]

print(func(len(a)-1))
'''
'''
a = [2,1,4,9]
dp = [-1 for _ in range(len(a))]
dp[0] = a[0]
for ind in range(1, len(a)):
    notPick = 0 + dp[ind -1]
    pick = 0
    if ind > 1:
        pick = a[ind] + dp[ind-2]
    dp[ind] = max(pick, notPick)

print(dp[len(a)-1])
'''
a = [2,1,4,9]
#dp = [-1 for _ in range(len(a))]
prev = a[0]
prev2 = 0 
for ind in range(1, len(a)):
    notPick = 0 + prev
    pick = 0
    if ind > 1:
        pick = a[ind] + prev2
    cur = max(pick, notPick)
    prev2 = prev
    prev = cur

print(prev)
