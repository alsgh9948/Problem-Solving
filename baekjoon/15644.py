from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int, input().split())
board = []

srx=sry=sbx=sby=-1
for x in range(n):
    board.append(list(input().strip()))
    for y in range(m):
        if board[x][y] == 'R':
            srx,sry = x,y
            board[x][y] = '.'
        elif board[x][y] == 'B':
            sbx,sby = x,y
            board[x][y] = '.'

def solv():
    q = deque([(srx,sry,sbx,sby,'')])
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    visited[srx][sry][sbx][sby] = True

    while q:
        rx,ry,bx,by,path = q.pop()

        if len(path) == 10:
            continue

        for d in range(4):
            nrx,nry,r_cnt = move_ball(rx,ry,d)
            nbx,nby,b_cnt = move_ball(bx,by,d)

            if board[nbx][nby] == 'O':
                continue
            elif board[nrx][nry] == 'O':
                print(len(path)+1)
                print(path+'UDLR'[d])
                return
            elif (nrx,nry) == (nbx,nby):
                if r_cnt > b_cnt:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.appendleft((nrx,nry,nbx,nby,path+'UDLR'[d]))

    print(-1)
def move_ball(x,y,d):
    count = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if not point_validator(nx,ny):
            return x,y,count
        elif board[nx][ny] == 'O':
            return nx,ny,count+1

        x,y = nx,ny
        count += 1
def point_validator(x,y):
    if board[x][y] == '#':
        return False
    return True
solv()