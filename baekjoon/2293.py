from sys import stdin

n,k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0]*(k+1)

def solv(now,sum):
    global dp
    if now == n or sum > k:
        return 0
    if sum == k:
        return 1

    if sum+coins[now] <= k:
        if dp[sum+coins[now]] == 0:
            dp[sum] += solv(now,sum+coins[now])
        else:
            dp[sum] += dp[sum+coins[now]]
    solv(now+1,sum)
    return dp[now]

solv(0,0)
print(dp[coins[0]])