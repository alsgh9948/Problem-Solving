from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
input = stdin.readline

n,m = map(int, input().split())
board = []

srx=sry=sbx=sby=-1
for x in range(n):
    board.append(list(input().strip()))
    for y in range(m):
        if board[x][y] == 'R':
            srx,sry = x,y
        elif board[x][y] == 'B':
            sbx,sby = x,y

def solv():
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    q = deque([(srx,sry,sbx,sby,0)])

    visited[srx][sry][sbx][sby] = True
    while q:
        rx,ry,bx,by,cnt = q.pop()

        if board[rx][ry] == 'O':
            print(1)
            return

        if cnt == 10:
            continue

        for d in range(4):
            nbx,nby,bcnt = move_ball(bx,by,d)
            if board[nbx][nby] == 'O':
                continue

            nrx,nry,rcnt = move_ball(rx,ry,d)

            if nrx == nbx and nry == nby:
                if bcnt > rcnt:
                    nbx -= dx[d]
                    nby -= dy[d]
                else:
                    nrx -= dx[d]
                    nry -= dy[d]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.appendleft((nrx,nry,nbx,nby,cnt+1))
    print(0)
def move_ball(x,y,d):
    cnt = 0
    while True:
        x += dx[d]
        y += dy[d]
        if not point_validator(x,y):
            x -= dx[d]
            y -= dy[d]
            return x,y,cnt
        if board[x][y] == 'O':
            return x,y,cnt
        cnt += 1

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '#':
        return False
    return True

solv()