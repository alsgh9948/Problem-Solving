from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
INF = 9876543210

n,p,k = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
max_cost = 0

for _ in range(p):
    a,b,c = map(int, input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))
    max_cost = max(max_cost,c)

def solv():
    left = 0
    right = max_cost
    answer = -1
    while left <= right:
        mid = (left+right)//2

        if simul(mid):
            right = mid-1
            answer = mid
        else:
            left = mid+1

    print(answer)

def simul(target):

    dist = [INF]*(n+1)

    pq = [(0,1)]

    while pq:
        count, now = heappop(pq)

        if now == n:
            return count <= k
        for nxt,cost in adj_list[now]:
            next_count = count + (0 if cost <= target else 1)
            if dist[nxt] > next_count:
                dist[nxt] = next_count
                heappush(pq,(next_count,nxt))

solv()