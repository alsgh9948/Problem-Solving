from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
INF = 9876543210

n,e = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))

v1,v2 = map(int, input().split())

def solv():
    visited = [[INF,INF,INF,INF] for _ in range(n+1)]
    start_status = 0
    if 1 == v1:
        start_status = 1
    visited[1][start_status] = 0
    pq = [(0,1,start_status)]

    while pq:
        dist,now,status = heappop(pq)

        if status == 3 and now == n:
            print(visited[n][status])
            return

        for nxt,cost in adj_list[now]:
            nxt_status = status
            if nxt == v1:
                if status == 0:
                    nxt_status = 1
                elif status == 2:
                    nxt_status = 3
            elif nxt == v2:
                if status == 0:
                    nxt_status = 2
                elif status == 1:
                    nxt_status = 3

            if visited[nxt][nxt_status] == INF or visited[nxt][nxt_status] > dist+cost:
                visited[nxt][nxt_status] = dist + cost
                heappush(pq,(dist+cost, nxt, nxt_status))

    print(-1)

solv()