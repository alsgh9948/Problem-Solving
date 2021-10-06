from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c,n = map(int, stdin.readline().strip().split())
board = []

for i in range(r):
    board.append(list(stdin.readline().strip()))
    for j in range(c):
        if board[i][j] == 'O':
            board[i][j] = 1
        else:
            board[i][j] = 0

def solv():
    q = deque()
    for i in range(1,n):
        op = i%2
        if op == 1:
            for x in range(r):
                for y in range(c):
                    if board[x][y] == 0:
                        board[x][y] = 1
                    else:
                        q.appendleft((x,y))
        else:
            bumb(q)

    for row in board:
        for num in row:
            if num == 0:
                print('.',end='')
            else:
                print('O',end='')
        print()

def bumb(q):
    while q:
        x,y = q.pop()
        board[x][y] = 0

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny):
                continue
            board[nx][ny] = 0

def point_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True

solv()