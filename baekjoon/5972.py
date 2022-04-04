from sys import stdin
from heapq import heappop,heappush

input = stdin.readline
INF = 9876543210

n,m = map(int, input().split())

adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))

def solv():
    pq = [(0,1)]

    visited = [INF]*(n+1)

    visited[1] = 0

    while pq:
        cnt, now = heappop(pq)
        if now == n:
            print(cnt)
            return
        for nxt,cost in adj_list[now]:
            if visited[nxt] > cnt+cost:
                visited[nxt] = cnt+cost
                heappush(pq,(cnt+cost,nxt))

solv()