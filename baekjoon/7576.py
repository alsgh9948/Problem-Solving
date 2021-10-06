from sys import stdin
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]
m, n = map(int, stdin.readline().strip().split())

_map = []

q = deque()
tomato_cnt = 0

def bfs():
    global q, tomato_cnt

    total_day = 0
    while q:
        x,y,day = q.pop()
        total_day = day
        _map[x][y] = 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_check(nx,ny):
                continue
            _map[nx][ny] = 1
            tomato_cnt -= 1
            q.appendleft((nx,ny,day+1))
    if tomato_cnt != 0:
        print(-1)
    else:
        print(total_day)

def point_check(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif _map[x][y] != 0:
        return False
    else:
        return True


for i in range(n):
    row = list(map(int, stdin.readline().strip().split()))
    _map.append(row)
    for j in range(m):
        if row[j] == 0:
            tomato_cnt += 1
        elif row[j] == 1:
            q.appendleft((i,j, 0))

bfs()