from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
INF = 98765432100

n,m,k = map(int, input().split())

adj_list = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int, input().split())
    adj_list[a-1].append((b-1,c))
    adj_list[b-1].append((a-1,c))

def solv():
    visited = [[INF]*(k+1) for _ in range(n)]
    pq = [(0,0,0)]
    visited[0][0] = 0
    while pq:
        total,cnt,now = heappop(pq)
        if total > visited[now][cnt]:
            continue
        if now == n-1:
            print(total)
            return
        for nxt,cost in adj_list[now]:
            nxt_total = total + cost
            if visited[nxt][cnt] > nxt_total:
                visited[nxt][cnt] = nxt_total
                heappush(pq,(nxt_total,cnt,nxt))

            if cnt+1 <= k and visited[nxt][cnt+1] > total:
                visited[nxt][cnt+1] = total
                heappush(pq, (total, cnt+1, nxt))

solv()