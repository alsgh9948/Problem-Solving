from sys import stdin
input = stdin.readline

n = int(input())
t,p = [],[]
dp = [0]*(n+1)

for i in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

tmp = 0
for i in range(n):
    tmp = max(tmp, dp[i])
    if i+t[i] > n:
        continue
    dp[i+t[i]] = max(tmp+p[i], dp[i+t[i]])

print(max(dp))