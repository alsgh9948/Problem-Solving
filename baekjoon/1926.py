from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def solv():
    cnt = 1
    size = 0
    for sx in range(n):
        for sy in range(m):
            if board[sx][sy] == 1:
                size = max(size, bfs(sx,sy))
                cnt += 1

    print(cnt-1)
    print(size)

def bfs(sx,sy):
    global board

    q = deque([(sx,sy)])
    board[sx][sy] = 0
    size = 0
    while q:
        x,y = q.pop()
        size += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                board[nx][ny] = 0
                q.appendleft((nx,ny))

    return size
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == 0:
        return False
    return True

solv()