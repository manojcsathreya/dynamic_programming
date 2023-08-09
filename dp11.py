'''
triangle = [[1],[2,3],[4,5,6]]
rows = len(triangle)
def func(i,j):
    if i == rows-1:
        return triangle[i][j]
    if i > rows:
        return float('inf')
    down = triangle[i][j] + func(i+1,j)
    diag = triangle[i][j] + func(i+1, j+1)
    return min(down, diag)

print(func(0,0))
'''
'''
triangle = [[1],[2,3],[4,5,6]]
dp = [[-1 for _ in range(len(triangle))] for _ in range(len(triangle))]
rows = len(triangle)
def func(i,j):
    if i == rows-1:
        return triangle[i][j]
    if i > rows:
        return float('inf')
    if dp[i][j] != -1:
        return dp[i][j]
    down = triangle[i][j] + func(i+1,j)
    diag = triangle[i][j] + func(i+1, j+1)
    dp[i][j] = min(down, diag)
    return dp[i][j]

print(func(0,0))
print(dp)
'''
'''
triangle = [[1], [2,3], [3,6,7], [8,9,6,10]]
n = len(triangle)
dp = [[0 for _ in range(n)] for _ in range(n)]

for j in range(len(triangle[-1])):
    dp[-1][j] = triangle[-1][j]

for i in range(len(triangle)-2, -1, -1):
    for j in range(i, -1, -1):
        down = triangle[i][j] + dp[i+1][j]
        diag = triangle[i][j] + dp[i+1][j+1]
        dp[i][j] += min(down, diag)

print(dp[0][0])
'''
triangle = [[1], [2,3], [3,6,7], [8,9,6,10]]
n = len(triangle)
front = [0 for _ in range(n)]

for j in range(len(triangle[-1])):
    front[j] = triangle[-1][j]
cur  = [0 for _ in range(n)]
for i in range(len(triangle)-2, -1, -1):
    for j in range(i, -1, -1):
        down = triangle[i][j] + front[j]
        diag = triangle[i][j] + front[j+1]
        cur[j] = min(down, diag)
    front = cur

print(front)

