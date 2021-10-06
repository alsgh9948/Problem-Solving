from collections import deque
from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = []

sx=sy=-1
q = deque()
for x in range(n):
    board.append(list(input()))
    for y in range(m):
        if board[x][y] == 'F':
            q.appendleft((x,y,-1))
        elif board[x][y] == 'J':
            sx,sy = x,y

def solv():
    global q, board
    visited = [[False]*m for _ in range(n)]
    q.appendleft((sx,sy,0))
    visited[sx][sy] = True
    while q:
        x,y,cnt = q.pop()

        if cnt >= 0 and (x == 0 or y == 0 or x == n - 1 or y == m - 1):
            print(cnt+1)
            return
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                if cnt == -1:
                    if not board[nx][ny] == 'F':
                        board[nx][ny] = 'F'
                        q.appendleft((nx,ny,cnt))
                else:
                    if not visited[nx][ny] and board[nx][ny] != 'F':
                        visited[nx][ny] = True
                        q.appendleft((nx,ny,cnt+1))
    print('IMPOSSIBLE')
    return
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '#':
        return False
    return True

solv()