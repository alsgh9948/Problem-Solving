from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

board = []
sx=sy=-1
for x in range(n):
    board.append(list(map(int, input().split())))
    if sy == -1:
        for y in range(m):
            if board[x][y] == 2:
                sx,sy=x,y
                break

def solv():
    global board
    answer = [[0]*m for _ in range(n)]
    q = deque([(sx,sy,0)])
    board[sx][sy] = 0

    while q:
        x,y,cnt = q.pop()
        answer[x][y] = cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                board[nx][ny] = -1
                q.appendleft((nx,ny,cnt+1))

    for x in range(n):
        for y in range(m):
            if board[x][y] > 0 and answer[x][y] == 0:
                answer[x][y] = -1
    for row in answer:
        print(*row)
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == 0:
        return False
    elif board[x][y] == -1:
        return False
    return True
solv()