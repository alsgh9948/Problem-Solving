from sys import stdin
import heapq

input = stdin.readline
INF = 9876543210

v,e = map(int, input().split())
start = int(input())

adj_list = [[] for _ in range(v)]

for _ in range(e):
    a,b,w = map(int, input().split())
    adj_list[a-1].append((b-1,w))

def solv():
    cost_map = [INF]*v

    pq = []
    heapq.heappush(pq,(0,start-1))
    cost_map[start-1] = 0

    while pq:
        cost,now = heapq.heappop(pq)

        for nxt,w in adj_list[now]:
            if cost_map[nxt] == INF or cost_map[nxt] > cost+w:
                cost_map[nxt] = cost+w
                heapq.heappush(pq,(cost+w,nxt))

    for cost in cost_map:
        if cost == INF:
            print('INF')
        else:
            print(cost)
solv()