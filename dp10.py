grid = [[1,2,3],[4,5,6]]
'''
def func(i,j):
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return  float("inf")
    up = grid[i][j] + func(i-1,j)
    left = grid[i][j] + func(i,j-1)
    return min(up,left)

print(func(2,2))
'''
'''
dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
def func(i,j):
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return  float("inf")
    if dp[i][j] != -1:
        return dp[i][j]
    
    up = grid[i][j] + func(i-1,j)
    left = grid[i][j] + func(i,j-1)
    dp[i][j] = min(up, left)
    return dp[i][j]

print(func(2,2))
'''
'''
dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
for i in range(len(grid[0])):
    for j in range(len(grid)):
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]
        else:
            up = grid[i][j]
            if i > 0:
                up += dp[i-1][j]
            else:
                up += float('inf')
    
            left = grid[i][j]
            if j > 0:
                left += dp[i][j-1]
            else:
                left = float('inf')
    
            dp[i][j] = min(up, left)

print(dp[-1][-1])
'''
n = len(grid)
m = len(grid[0])
prev = [0 for _ in range(m)]
for i in range(n):
    cur = [0 for _ in range(m)]
    for j in range(m):
        if i == 0 and j == 0:
            cur[j] = grid[i][j]
        else:
            up = grid[i][j]
            if i > 0:
                up += prev[j]
            else:
                up = float('inf')
    
            left = grid[i][j]
            if j > 0:
                left += cur[j-1]
            else:
                left = float('inf')
    
            cur[j] = min(up, left)
    prev = cur

print(cur)
