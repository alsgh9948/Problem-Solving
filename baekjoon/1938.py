from sys import stdin
from collections import deque

input = stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())

board = []

s = []
g = []
for x in range(n):
    board.append(list(input()))
    if len(s) < 3 or len(g) < 3:
        for y in range(n):
            if board[x][y] == 'B':
                s.append((x,y))
            elif board[x][y] == 'E':
                g.append((x,y))

sx,sy = s[1]
gx,gy = g[1]
sd = 0 if s[0][0]+1 == s[1][0] else 1
gd = 0 if g[0][0]+1 == g[1][0] else 1

def solv():
    q = deque()
    visited = [[[False,False] for _ in range(n)] for _ in range(n)]

    q.appendleft((sx,sy,0,sd))
    visited[sx][sy][sd] = True

    while q:
        x,y,cnt,dir = q.pop()

        if x == gx and y == gy and dir == gd:
            return cnt

        nxt_dir = (dir+1)%2
        if rotate_validator(x,y) and not visited[x][y][nxt_dir]:
            q.appendleft((x,y,cnt+1,nxt_dir))
            visited[x][y][nxt_dir] = True

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,dir,visited) and point_validator(nx-dx[dir],ny-dy[dir]) and point_validator(nx+dx[dir],ny+dy[dir]):
                visited[nx][ny][dir] = True
                q.appendleft((nx,ny,cnt+1,dir))
    return 0

def rotate_validator(sx,sy):
    for x in range(sx-1,sx+2):
        for y in range(sy-1,sy+2):
            if not point_validator(x,y):
                return False
    return True
def point_validator(x,y,dir=-1,visited=None):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == '1':
        return False
    elif dir != -1 and visited[x][y][dir]:
        return False
    return True

print(solv())