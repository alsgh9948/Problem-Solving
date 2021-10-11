from sys import stdin
from heapq import heappush, heappop

INF = 9876543210
input = stdin.readline

n = int(input())
a,b,c = map(int, input().split())
m = int(input())

adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int, input().split())
    adj_list[x].append((y,z))
    adj_list[y].append((x,z))

def solv():
    dists = set_dists()

    answer = (0,-1)
    for idx in range(1,n+1):
        dist = dists[idx]
        if INF in dist:
            continue
        if answer[0] < min(dist):
            answer = (min(dist),idx)
    print(answer[1])
def set_dists():
    dist = [[INF,INF,INF] for _ in range(n+1)]

    dist_idx = -1
    for start in (a,b,c):
        dist_idx += 1
        dist[start][dist_idx] = 0

        pq = [(0,start)]
        while pq:
            length, now = heappop(pq)
            if dist[now][dist_idx] != length:
                continue

            for nxt, cost in adj_list[now]:
                nxt_cost = length+cost
                if dist[nxt][dist_idx] > nxt_cost:
                    dist[nxt][dist_idx] = nxt_cost
                    heappush(pq,(nxt_cost,nxt))
    return dist
solv()