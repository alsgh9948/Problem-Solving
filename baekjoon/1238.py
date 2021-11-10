from sys import stdin
from heapq import heappush, heappop

INF = 9876543210
input = stdin.readline

n,m,x = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    adj_list[a].append((b,c))
def solv():
    cost = dijkstra(x)
    answer = 0
    for start in range(1,n+1):
        if start == x:
            continue

        answer = max(answer, cost[start]+dijkstra(start,x))
    print(answer)
def dijkstra(start, target=-1):
    cost = [INF]*(n+1)

    pq = [(0,start)]
    cost[start] = 0

    while pq:
        now_cost, now = heappop(pq)

        if cost[now] != now_cost:
            continue

        if now == target:
            return now_cost
        for nxt,nxt_cost in adj_list[now]:
            if cost[nxt] > now_cost + nxt_cost:
                cost[nxt] = now_cost + nxt_cost
                heappush(pq,(cost[nxt],nxt))

    return cost
solv()