#FIB

# 0 1 1 2 3 5
'''
n =5
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2) 

print(fib(n))
'''
#meomoization
'''

n = 5
dp = [-1 for _ in range(n+1)]
def fib(n):
    if n < 2:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2) 
    return dp[n]

print(fib(n))
'''

# Tablulation
'''
n = 5
dp = [-1 for _ in range(n+1)]
dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
'''
#space optimization
n =  5
dp0 = 0
dp1 = 1
for i in range(2, n+1):
    temp = dp0 + dp1
    dp0 = dp1
    dp1 = temp

print(dp1)
