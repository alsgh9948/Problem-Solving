from sys import stdin
from collections import deque
import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int, stdin.readline().strip().split())

_map = [list(map(int,stdin.readline().strip())) for _ in range(n)]

#0-1bfs
# def bfs():
#     visited = [[False]*m for _ in range(n)]
#     dq = deque()
#
#     dq.append((0,0,0))
#     visited[0][0] = True
#
#     while dq:
#         x,y,cnt = dq.pop()
#         if x == n-1 and y == m-1:
#             print(cnt)
#             return
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if not point_check(nx,ny,visited):
#                 continue
#             visited[nx][ny] = True
#             if _map[nx][ny] == 0:
#                 dq.append((nx,ny,cnt))
#             else:
#                 dq.appendleft((nx,ny,cnt+1))

def bfs():
    visited = [[False]*m for _ in range(n)]
    pq = []
    heapq.heappush(pq,(0,0,0))
    visited[0][0] = True

    while pq:
        cnt, x, y = heapq.heappop(pq)
        if x == n-1 and y == m-1:
            print(cnt)
            return
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not point_check(nx,ny,visited):
                continue
            visited[nx][ny] = True
            if _map[nx][ny] == 0:
                heapq.heappush(pq, (cnt,nx,ny))
            else:
                heapq.heappush(pq, (cnt+1,nx,ny))

def point_check(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif visited[x][y]:
        return False
    else:
        return True

bfs()