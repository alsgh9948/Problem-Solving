from sys import stdin
from heapq import heappush,heappop

input = stdin.readline

k,n,f = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
adj_mat = [[False]*(n+1) for _ in range(n+1)]

for _ in range(f):
    a,b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

    adj_mat[a][b] = adj_mat[b][a] = True

for idx in range(1,n+1):
    adj_list[idx].sort()
end = -1
def solv():
    for start in range(1,n+1):
            rst = bfs(start)
            if rst:
                rst.sort()
                for num in rst:
                    print(num)
                return
    print(-1)

def bfs(start):
    visited = [False]*(n+1)
    path = [start]
    pq = [start]
    visited[start] = True
    while pq:
        now = heappop(pq)
        for nxt in adj_list[now]:
            if not visited[nxt]:
                visited[nxt] = True
                flag = False
                for target in path:
                    if not adj_mat[nxt][target]:
                        flag = True
                        break
                if not flag:
                    path.append(nxt)
                    if len(path) == k:
                        return path
                    heappush(pq,nxt)
    return None
if k == 1:
    print(1)
else:
    solv()