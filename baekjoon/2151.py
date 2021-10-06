from sys import stdin
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(stdin.readline().strip())
board = []
ans = 1000000000

sx=sy=gx=gy=-1
for i in range(n):
    board.append(list(stdin.readline().strip()))
    for j in range(n):
        if board[i][j] == '#':
            if sx == -1:
                sx,sy = i,j
            else:
                gx,gy = i,j

def bfs():
    global ans

    visited = [[[10000000]*4 for _ in range(n)] for _ in range(n)]
    q = deque()

    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if not point_validator(nx, ny):
            continue

        if nx == gx and ny == gy:
            return 0
        q.appendleft((nx, ny, 0, d))
        visited[nx][ny][d] = 0
    while q:
        x,y,cnt,dir = q.pop()

        if x == gx and y == gy:
            continue
        if board[x][y] == '.':
            nx = x + dx[dir]
            ny = y + dy[dir]

            if not point_validator(nx,ny) or visited[nx][ny][dir] <= visited[x][y][dir]:
                continue

            visited[nx][ny][dir] = visited[x][y][dir]
            q.appendleft((nx,ny,cnt,dir))
        else:
            for d in range(4):
                if d == (dir+2)%4:
                    continue

                nx = x + dx[d]
                ny = y + dy[d]

                if not point_validator(nx,ny):
                    continue

                if d == dir and visited[nx][ny][d] > visited[x][y][dir]:
                    visited[nx][ny][d] = visited[x][y][dir]
                    q.appendleft((nx,ny,cnt,d))
                elif d != dir and visited[nx][ny][d] > visited[x][y][dir]+1:
                    visited[nx][ny][d] = visited[x][y][dir]+1
                    q.appendleft((nx,ny,cnt+1,d))
    return min(visited[gx][gy])
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == '*':
        return False

    return True

print(bfs())
