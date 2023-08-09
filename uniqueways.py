'''
def  func(i,j):
    if (i == 0 and j ==0):
        return 1
    if (i < 0 or j < 0):
        return 0

    up = func(i-1,j)
    down = func(i,j-1)
    return up+down

print(func(3,2))
'''
'''
m,n = 3, 2
dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
print(dp)
def func(i,j):
    if (i == 0 and j == 0):
        return 1
    if (i < 0 or j < 0):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    up = func(i-1,j)
    down = func(i,j-1)
    
    dp[i][j] = up+down
    return dp[i][j]

print(func(m-1,n-1))
'''
'''
m,n = 3,2
dp = [[-1 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if i ==0 and j ==0:
            dp[0][0] = 1
            continue
        up, left = 0,0
        if i > 0:
            up = dp[i-1][j]
        if j > 0:
            left = dp[i][j-1]
        dp[i][j] = up+left
print(dp)

'''
m,n = 3,2
prev = [-1 for _ in range(2)]

for i in range(1,m):
    for j in range(1,n):
        if i ==0 and j ==0:
            prev[0] = 1
            continue
        up, left = 0,0
        if i > 0:
            up = prev[j]
        if j > 0:
            left = prev[j-1]
        prev[j] = up+left
    temp = prev
print(temp)
