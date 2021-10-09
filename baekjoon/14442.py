from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m,k = map(int, stdin.readline().strip().split())

board = [list(map(int,stdin.readline().strip())) for _ in range(n)]

def bfs():
    visited = [[[False]*(k+1) for _ in range(m)] for _ in range(n)]
    q = deque()

    q.appendleft((0,0,0,1))
    visited[0][0][0] = True

    while q:
        x,y,wall_cnt,cnt = q.pop()
        if x == n-1 and y == m-1:
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny):
                continue

            if board[nx][ny] == 1:
                if wall_cnt < k and not visited[nx][ny][wall_cnt+1]:
                    q.appendleft((nx,ny,wall_cnt+1,cnt+1))
                    visited[nx][ny][wall_cnt+1] = True
            else:
                if not visited[nx][ny][wall_cnt]:
                    q.appendleft((nx,ny,wall_cnt,cnt+1))
                    visited[nx][ny][wall_cnt] = True
    return -1
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

print(bfs())