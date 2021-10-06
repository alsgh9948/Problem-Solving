from sys import stdin
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int, stdin.readline().strip().split())
_map = [list(map(int,stdin.readline().strip())) for _ in range(n)]

def point_check(x,y):
    if (x < 0 or y < 0 or x >= n or y >= m) or _map[x][y] == 0:
        return False
    return True

def bfs():
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    q = deque()

    q.appendleft((0,0))

    while q:
        x,y = q.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not point_check(nx,ny):
                continue
            if visited[nx][ny] != 0:
                if visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
            else:
                visited[nx][ny] = visited[x][y] + 1
                q.appendleft((nx,ny))
    print(visited[n-1][m-1])

bfs()
