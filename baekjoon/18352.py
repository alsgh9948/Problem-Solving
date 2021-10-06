from sys import stdin
import heapq

input = stdin.readline

n,m,k,x = map(int, input().split())

adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())

    adj_list[a].append(b)

def solv():
    pq = []
    visited = [False]*(n+1)
    ans = []
    heapq.heappush(pq,(0,x))
    visited[x] = True

    while pq:
        cnt,now = heapq.heappop(pq)

        if cnt == k:
            ans.append(now)
            continue

        for nxt in adj_list[now]:
            if not visited[nxt]:
                visited[nxt] = True
                heapq.heappush(pq,(cnt+1,nxt))
    if ans:
        for num in ans:
            print(num)
    else:
        print(-1)
    return

solv()