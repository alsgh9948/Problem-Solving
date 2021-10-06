from sys import stdin
from collections import deque

input = stdin.readline
dx = [1,0,1]
dy = [0,1,1]

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

def solv():
    q = deque([(0,0)])
    visited = [[987654321]*m for _ in range(n)]
    visited[0][0] = board[0][0]

    while q:
        x,y = q.pop()
        if x == n-1 and y == m-1:
            continue

        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                if visited[nx][ny] == 987654321 or visited[nx][ny] < visited[x][y] + board[nx][ny]:
                    visited[nx][ny] = visited[x][y] + board[nx][ny]
                    q.appendleft((nx,ny))
    print(visited[n-1][m-1])
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solv()