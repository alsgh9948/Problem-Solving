from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(1000000)

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,-1,1,1,-1]

w, h = 0, 0
_map = []

def bfs(sx,sy):
    global _map
    q = deque()
    q.appendleft((sx,sy))

    while q:
        x,y = q.pop()
        _map[x][y] = 2
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if not point_check(nx,ny):
                continue
            _map[nx][ny] = 2
            q.appendleft((nx,ny))

def dfs(x,y):
    global _map
    _map[x][y] = 2
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if not point_check(nx, ny):
            continue
        dfs(nx,ny)

def point_check(x,y):
    if (x < 0 or y < 0 or x >= h or y >= w) or _map[x][y] != 1:
        return False
    return True

while True:
    ans = 0
    w, h = map(int, stdin.readline().strip().split())
    if w+h == 0:
        break

    _map = [list(map(int,stdin.readline().strip().split())) for _ in range(h)]

    for x in range(h):
        for y in range(w):
            if _map[x][y] == 1:
                dfs(x,y)
                ans += 1
    print(ans)
