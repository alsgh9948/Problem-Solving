from sys import stdin

input = stdin.readline
INF = 9876543210

n,k = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = INF
dist = [[0]*n for _ in range(n)]
dp = [[INF]*(k+1) for _ in range(n)]
def solv():
    global dist
    for i in range(n):
        for j in range(i+1,n):
            dist[i][j] = calc_dist(points[i],points[j])
            dist[j][i] = dist[i][j]
    select_point(0,k)
    print(min(dp[0]))

def select_point(now,count):
    global answer,dist

    if dp[now][count] != INF:
        return dp[now][count]

    if now == n-1:
        return 0

    for cnt in range(count+1):
        if now+cnt+1 < n:
            dp[now][count] = min(dp[now][count], select_point(now+cnt+1,count-cnt)+dist[now][now+cnt+1])
    return dp[now][count]
def calc_dist(now,nxt):
    return abs(now[0]-nxt[0])+abs(now[1]-nxt[1])

solv()