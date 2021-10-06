import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())

schedule = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0]*(n+1)
ans = -1
def solv(now, sum, temp_price):
    if now >= len(schedule):
        if now == n and (dp[now] == 0 or dp[now] < sum+temp_price):
            dp[n] = sum+temp_price
        return
    nxt = now + schedule[now][0]
    if nxt <= n and (dp[nxt] == 0 or dp[nxt] < sum+temp_price):
        dp[nxt] = sum + temp_price
        solv(now + schedule[now][0], sum+temp_price, schedule[now][1])
    if temp_price == 0:
        solv(now + schedule[now][0], sum+temp_price, schedule[now][1])
    solv(now + 1, sum+temp_price, 0)

    return

solv(0,0,0)

print(max(dp))