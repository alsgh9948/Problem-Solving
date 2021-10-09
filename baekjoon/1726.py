from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]


n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
sx,sy,sd = map(int, input().split())
gx,gy,gd = map(int, input().split())

def convert_dir(d):
    if d == 1:
        return 1
    elif d == 2:
        return 3
    elif d == 3:
        return 2
    else:
        return 0
def solv():
    global sd, gd
    sd = convert_dir(sd)
    gd = convert_dir(gd)

    q = deque()
    visited = [[[False]*4 for _ in range(m)] for _ in range(n)]

    q.appendleft((sx-1,sy-1,sd,0))
    visited[sx-1][sy-1][sd] = True
    while q:
        x,y,d,cnt = q.pop()

        if x == gx-1 and y == gy-1 and d == gd:
            print(cnt)
            return

        nx = x
        ny = y
        for _ in range(3):
            nx += dx[d]
            ny += dy[d]

            if point_validator(nx,ny):
                if visited[nx][ny][d]:
                    continue
                visited[nx][ny][d] = True
                q.appendleft((nx,ny,d,cnt+1))
            else:
                break

        flag = False
        rd = (d+1)%4
        if not visited[x][y][rd]:
            visited[x][y][rd] = True
            q.appendleft((x,y,rd,cnt+1))
            flag = True

        ld = (d+3)%4
        if not visited[x][y][ld]:
            visited[x][y][ld] = True
            q.appendleft((x,y,ld,cnt+1))
            flag = True

        if flag:
            rd = (d + 2) % 4
            if not visited[x][y][rd]:
                visited[x][y][rd] = True
                q.appendleft((x, y, rd, cnt + 2))
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == 1:
        return False
    return True

solv()