matrix = [[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]
m = len(matrix[0])
n = len(matrix)
'''
def func(i,j):
    if j < 0 or j >= m:
        return float("-inf")

    if i == 0:
        return matrix[i][j]
    
    up = matrix[i][j] + func(i-1,j)
    left = matrix[i][j] + func(i-1,j-1)
    right = matrix[i][j] + func(i-1,j+1)

    return max(up, left, right)

maxi = 0
for i in range(m):
    maxi = max(maxi, func(n-1,i))

print(maxi)
'''
'''
dp = [[ -1 for _ in range(m)] for _ in range(n)]
def func(i,j):
 
    
    if j < 0 or j >= m:
        return float("-inf")
    
    if dp[i][j] != -1:
        return dp[i][j]

    if i == 0:
        return matrix[i][j]

    up = matrix[i][j] + func(i-1,j)
    left = matrix[i][j] + func(i-1,j-1)
    right = matrix[i][j] + func(i-1,j+1)
    dp[i][j] = max(up, left, right)
    return dp[i][j]

maxi = 0
for i in range(m):
    maxi = max(maxi, func(n-1,i))
print(dp)
print(maxi)

'''
'''
dp = [[ -1 for _ in range(m)] for _ in range(n)]
for i in range(m):
    dp[0][i] = matrix[0][i]

for i in range(1,n):
    for j in range(m):
        down = matrix[i][j] + dp[i-1][j]

        left = matrix[i][j]
        
        if j > 0:
            left +=  dp[i-1][j-1]
        else:
        left += float("inf")

        right = matrix[i][j]
        
        if j < m-2:
            right += dp[i-1][j+1]
        
        dp[i][j] = max(down, left, right)

print(max(dp[-1]))
'''
prev = [0] * m
cur = [0] * m
for i in range(m):
    prev[i] = matrix[0][i]

for i in range(1,n):
    for j in range(m):
        down = matrix[i][j] + prev[j]

        left = matrix[i][j]
        
        if j > 0:
            left +=  prev[j-1]
        else:    
            left += float("-inf")

        right = matrix[i][j]
        
        if j < m-2:
            right += prev[j+1]
        else:
            right += float("-inf")
        
        cur[j] = max(down, left, right)
    prev = cur.copy()

print(cur)
