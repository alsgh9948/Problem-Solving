from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

board = [input() for _ in range(n)]
ans = 0
def solv():
    global ans
    for sx in range(n):
        for sy in range(m):
            if board[sx][sy] == 'L':
              ans = max(ans, bfs(sx,sy))

    print(ans)
def bfs(sx,sy):
    global ans
    visited = [[0] * m for _ in range(n)]
    q = deque([(sx,sy)])
    visited[sx][sy] = 1

    max_length = 0
    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited):
                visited[nx][ny] = visited[x][y] + 1
                max_length = visited[nx][ny]
                q.appendleft((nx,ny))

    return max_length-1
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == 'W':
        return False
    elif visited[x][y] != 0:
        return False
    return True

solv()