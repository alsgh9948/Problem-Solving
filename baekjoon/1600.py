from sys import stdin
from collections import deque

hdx = [-1,-2,-2,-1,1,2, 2, 1]
hdy = [-2,-1, 1, 2,2,1,-1,-2]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

k = int(stdin.readline().strip())
w,h = map(int, stdin.readline().strip().split())

board = [list(map(int, stdin.readline().strip().split())) for _ in range(h)]

def bfs():
    visited = [[[False]*(k+1) for _ in range(w)] for _ in range(h)]
    q = deque()

    q.appendleft((0,0,0,0))
    visited[0][0][0] = True

    while q:
        x,y,h_cnt,cnt = q.pop()

        if x == h-1 and y == w-1:
            return cnt

        if h_cnt < k:
            for d in range(8):
                nx = x + hdx[d]
                ny = y + hdy[d]

                if not point_validator(nx,ny):
                    continue
                if not visited[nx][ny][h_cnt+1]:
                    q.appendleft((nx,ny,h_cnt+1,cnt+1))
                    visited[nx][ny][h_cnt+1] = True

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx, ny):
                continue
            if not visited[nx][ny][h_cnt]:
                q.appendleft((nx, ny, h_cnt, cnt + 1))
                visited[nx][ny][h_cnt] = True
    return -1
def point_validator(x,y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    elif board[x][y] == 1:
        return False
    return True

print(bfs())