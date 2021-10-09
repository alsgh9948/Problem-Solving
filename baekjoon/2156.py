from sys import stdin

input = stdin.readline
n = int(input())
juice = [0,0,0]
for _ in range(n):
    juice.append(int(input()))

ans = 0
dp = [0]*(n+3)
def solv():
    for idx in range(3,n+3):
        dp[idx] = max(juice[idx]+dp[idx-2], juice[idx]+juice[idx-1]+dp[idx-3])
        dp[idx] = max(dp[idx], dp[idx-1])
    print(dp[-1])

solv()