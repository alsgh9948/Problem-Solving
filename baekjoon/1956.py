from sys import stdin
from heapq import heappush, heappop
INF = 9876543210
input = stdin.readline

v,e = map(int, input().split())
adj_list = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    adj_list[a].append((b,c))

def solv():
    answer = INF
    for start in range(1,v+1):
        answer = min(answer, search_cycle(start))
    print(answer if answer < INF else -1)

def search_cycle(start):
    dist = [INF]*(v+1)
    pq = []
    for nxt, cost in adj_list[start]:
        dist[nxt] = cost
        heappush(pq, (cost, nxt))
    while pq:
        length, now = heappop(pq)

        if dist[now] != length:
            continue

        if now == start:
            return length
        for nxt,cost in adj_list[now]:
            nxt_length = cost + length
            if dist[nxt] > nxt_length:
                dist[nxt] = nxt_length
                heappush(pq,(nxt_length,nxt))
    return INF
solv()
