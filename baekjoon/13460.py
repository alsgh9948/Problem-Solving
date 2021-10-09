from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, stdin.readline().strip().split())
board = []
rx,ry,bx,by,gx,gy = -1,-1,-1,-1,-1,-1
for i in range(n):
    row = stdin.readline()
    board.append(row)
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j
        elif board[i][j] == 'O':
            gx,gy = i,j

def point_check(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '#':
        return False
    return True

def move_ball(x,y,d):
    cnt = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == gx and ny == gy:
            return cnt, nx, ny
        if not point_check(nx,ny):
            return cnt, x, y
        x,y = nx,ny
        cnt += 1

def bfs():
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    q = deque()
    q.appendleft((0,rx,ry,bx,by))
    visited[rx][ry][bx][by] = True
    while q:
        cnt,x1,y1,x2,y2 = q.pop()
        if cnt >= 10:
            return -1
        for d in range(4):
            cnt2, nx2, ny2 = move_ball(x2, y2, d)
            cnt1, nx1, ny1 = move_ball(x1, y1, d)

            if nx2 == gx and ny2 == gy:
                continue
            elif nx1 == gx and ny1 == gy:
                return cnt+1

            if nx1 == nx2 and ny1 == ny2:
                if cnt1 > cnt2:
                    nx1 -= dx[d]
                    ny1 -= dy[d]
                else:
                    nx2 -= dx[d]
                    ny2 -= dy[d]
            if visited[nx1][ny1][nx2][ny2]:
                continue
            visited[nx1][ny1][nx2][ny2] = True
            q.appendleft((cnt+1,nx1,ny1,nx2,ny2))
    return -1
print(bfs())
