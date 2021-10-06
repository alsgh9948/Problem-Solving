from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int, input().split())

board = []
sx=sy=-1
num = 1
for x in range(n):
    board.append(list(input().strip()))
    for y in range(m):
        if board[x][y] == 'S':
            sx,sy = x,y
        elif board[x][y] == 'X':
            board[x][y] = str(num)
            num += 1

def solv():
    q = deque()
    visited = [[[False]*64 for _ in range(m)] for _ in range(n)]

    q.appendleft((sx,sy,0,0))
    visited[sx][sy][0] = True

    while q:
        x,y,cnt,p = q.pop()

        if board[x][y] == 'E':
            if p == 2**num-2:
                return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                target = board[nx][ny]
                np = p
                if ord('1') <= ord(target) < ord(str(num)):
                    np = p | (1<<int(target))
                if not visited[nx][ny][np]:
                    visited[nx][ny][np] = True
                    q.appendleft((nx,ny,cnt+1,np))

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '#':
        return False
    return True

print(solv())