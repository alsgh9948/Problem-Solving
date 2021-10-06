import heapq

dx = [1,-1,0,0]
dy = [0,0,-1,1]
n,k = map(int, input().split())

def bfs():
    visited = [False] *100001
    visited[n] = True
    pq = []
    heapq.heappush(pq,(0,n))

    while pq:
        cnt, now = heapq.heappop(pq)
        if now == k:
            print(cnt)
            return
        if 0 <= now*2 and  now*2 <= 100000 and not visited[now*2]:
            visited[now*2] = True
            heapq.heappush(pq,(cnt,now*2))

        if now+1 <= 100000 and not visited[now+1]:
            visited[now+1] = True
            heapq.heappush(pq,(cnt+1, now+1))

        if now-1 >= 0 and not visited[now-1]:
            visited[now-1] = True
            heapq.heappush(pq,(cnt+1, now-1))

bfs()