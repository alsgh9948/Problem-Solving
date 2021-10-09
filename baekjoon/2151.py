from sys import stdin
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(stdin.readline().strip())
board = []
ans = 1000000000

sx=sy=gx=gy=-1
for i in range(n):
    board.append(stdin.readline().strip())
    for j in range(n):
        if board[i][j] == '#':
            if sx == -1:
                sx,sy = i,j
            else:
                gx,gy = i,j

def bfs():
    global ans

    visited = [[False]*n for _ in range(n)]
    q = deque()

    visited[sx][sy] = True
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if not point_validator(nx, ny, visited):
            continue

        if nx == gx and ny == gy:
            ans = 0
            return
        q.appendleft((nx, ny, 0, d))
        visited[nx][ny] = True
    while q:
        x,y,cnt,dir = q.pop()

        if x == gx and y == gy:
            ans = min(ans, cnt)
            if ans == 0:
                return
            continue
        if board[x][y] == '.':
            nx = x + dx[dir]
            ny = y + dy[dir]

            if not point_validator(nx,ny,visited):
                continue

            if not (nx == gx and ny == gy):
                visited[nx][ny] = True
            q.appendleft((nx,ny,cnt,dir))
        else:
            for d in range(4):
                if d == (dir+2)%4:
                    continue

                nx = x + dx[d]
                ny = y + dy[d]

                if not point_validator(nx,ny,visited):
                    continue

                if not (nx == gx and ny == gy):
                    visited[nx][ny] = True
                if d == dir:
                    q.appendleft((nx,ny,cnt,d))
                else:
                    q.appendleft((nx,ny,cnt+1,d))

def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y]:
        return False
    elif board[x][y] == '*':
        return False

    return True

bfs()
print(ans)