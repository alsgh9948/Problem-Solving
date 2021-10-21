from sys import stdin

INF = 9876543210
input = stdin.readline

n,m = map(int, input().split())

board = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    board[a].append((b,c))

def solv():
    dist = [INF]*(n+1)

    dist[1] = 0
    for cnt in range(n):
        for now in range(1,n+1):
            if dist[now] != INF:
                for nxt,cost in board[now]:
                    if dist[nxt] > dist[now]+cost:
                        dist[nxt] = dist[now] + cost
                        if cnt == n-1:
                            print(-1)
                            return
    for cost in dist[2:]:
        if cost == INF:
            print(-1)
        else:
            print(cost)
solv()