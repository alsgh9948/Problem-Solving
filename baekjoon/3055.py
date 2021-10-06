from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int, stdin.readline().strip().split())
q = deque()
sx, sy = -1, -1
ex, ey = -1, -1
_map = []
for i in range(r):
    _map.append(list(stdin.readline().strip()))
    for j in range(c):
        if _map[i][j] == '*':
            q.appendleft((-1,i,j))
        elif _map[i][j] == 'S':
            sx, sy = i, j
            _map[i][j] = '.'
        elif _map[i][j] == 'D':
            ex, ey = i, j

q.appendleft((0,sx,sy))
def bfs():
    global q
    visited = [[False]*c for _ in range(r)]
    visited[sx][sy] = True

    while q:
        cnt,x,y = q.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_check(nx,ny):
                continue
            if cnt == -1:
                if _map[nx][ny] == '.':
                    _map[nx][ny] = '*'
                    q.appendleft((cnt, nx, ny))
            else:
                if nx == ex and ny == ey:
                    print(cnt + 1)
                    return True
                elif _map[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.appendleft((cnt+1,nx,ny))
    return False

def point_check(x,y):
    if x < 0 or y < 0 or x>= r or y >= c:
        return False
    elif _map[x][y] == 'X':
        return False
    return True

if not bfs():
    print('KAKTUS')