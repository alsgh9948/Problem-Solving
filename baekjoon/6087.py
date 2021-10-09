from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

w,h = map(int, stdin.readline().strip().split())
sx,sy,ex,ey = -1,-1,-1,-1
board = []
for i in range(h):
    board.append(list(stdin.readline().strip()))
    for j in range(w):
        if board[i][j] == 'C':
            if sx == -1:
                sx,sy = i,j
                board[i][j] = '*'
            else:
                ex,ey = i,j
def bfs():
    visited = [[[10000000]*4 for _ in range(w)] for _ in range(h)]
    q = deque()
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if not point_validator(nx, ny):
            continue
        q.appendleft((0,nx,ny,d))
        visited[nx][ny][d] = 1
    min_cnt = 10000000
    while q:
        # cnt, x, y, dir = heapq.heappop(pq)
        cnt, x, y, dir = q.pop()

        if x == ex and y == ey:
            # print(cnt)
            min_cnt = min(cnt,min_cnt)
            visited[x][y][dir] = 10000000
            continue

        for d in range(4):
            if not dir_validator(dir,d):
                continue
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny):
                continue

            if dir == d:
                if visited[nx][ny][d] > cnt:
                    q.appendleft((cnt,nx,ny,d))
                    visited[nx][ny][d] = cnt
            else:
                if visited[nx][ny][d] > cnt+1:
                    q.appendleft((cnt+1,nx,ny,d))
                    visited[nx][ny][d] = cnt+1

    return min_cnt
def point_validator(x,y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    elif board[x][y] == '*':
        return False
    return True

def dir_validator(now, nxt):
    if now == 0 and nxt == 1:
        return False
    elif now == 1 and nxt == 0:
        return False
    elif now == 2 and nxt == 3:
        return False
    elif now == 3 and nxt == 2:
        return False
    return True

print(bfs())