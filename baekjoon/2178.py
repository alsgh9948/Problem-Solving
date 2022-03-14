from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = [input().strip() for _ in range(n)]

def solv():
    visited = [[False]*m for _ in range(n)]

    q = deque([(0,0,1)])
    visited[0][0] = True

    while q:
        x,y,cnt = q.pop()

        if x == n-1 and y == m-1:
            print(cnt)
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited):
                visited[nx][ny] = True
                q.appendleft((nx,ny,cnt+1))

def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif visited[x][y]:
        return False
    elif board[x][y] == '0':
        return False
    return True

solv()