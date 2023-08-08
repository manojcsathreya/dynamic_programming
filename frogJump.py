# Frog Jump
'''
height = [30, 10, 60 , 10, 60 ,50]
def func(ind):
    if ind == 0:
        return 0
    jumpTwo = float("inf")
    jumpOne = func(ind-1) + abs(height[ind] - height[ind-1])
    if ind > 1:
        jumpTwo = func(ind-2) + abs(height[ind] - height[ind-2])
    return min(jumpOne, jumpTwo)

print(func(len(height)-1))
'''
#memoization
'''
height = [30, 10, 60 , 10, 60 ,50]
dp = [-1 for _ in range(len(height))]
def func(ind):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    jumpTwo = float("inf")
    jumpOne = func(ind-1) + abs(height[ind] - height[ind-1])
    if ind > 1:
        jumpTwo = func(ind-2) + abs(height[ind] - height[ind-2])
    dp[ind] = min(jumpOne, jumpTwo)
    return dp[ind]

print(func(len(height)-1))
'''

#Tabulation
'''
height = [30, 10, 60 , 10, 60 ,50]
n = len(height)
dp = [-1 for _ in range(len(height))]
dp[0] = 0
for i in range(1, n):
    jumpTwo = float("inf")
    jumpOne = dp[i-1] + abs(height[i] - height[i-1])
    if i > 1:
        jumpTwo = dp[i-2] + abs(height[i] - height[i-2])
    dp[i] = min(jumpOne, jumpTwo)
print(dp[n-1])
'''

#Space Optimization
height = [30, 10, 60 , 10, 60 ,50]
n = len(height)
#dp = [-1 for _ in range(len(height))]
prev = 0
prev2 = 0
for i in range(1, n):
    jumpTwo = float("inf")
    jumpOne = prev + abs(height[i] - height[i-1])
    if i > 1:
        jumpTwo = prev2 + abs(height[i] - height[i-2])
    cur = min(jumpOne, jumpTwo)
    prev2 = prev
    prev = cur

print(prev)

