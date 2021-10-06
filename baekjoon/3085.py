from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(stdin.readline().strip())

board = [list(stdin.readline().strip()) for _ in range(n)]

ans = 0
def solv():
    for i in range(n):
        row_check(i)
        cul_check(i)

    for i in range(n):
        for j in range(n):
            change_char(i,j)


def change_char(x,y):
    global ans
    c = board[x][y]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if not point_validator(nx,ny,c):
            continue

        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

        row_check(nx)
        row_check(x)
        cul_check(ny)
        cul_check(y)

        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

def point_validator(x,y,c):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif c == board[x][y]:
        return False
    return True

def row_check(x):
    global ans
    c = board[x][0]
    cnt = 1
    for y in range(1,n):
        if c == board[x][y]:
            cnt += 1
        else:
            c = board[x][y]
            ans = max(ans,cnt)
            cnt = 1
    ans = max(ans,cnt)

def cul_check(y):
    global ans
    c = board[0][y]
    cnt = 1
    for x in range(1,n):
        if c == board[x][y]:
            cnt += 1
        else:
            c = board[x][y]
            ans = max(ans,cnt)
            cnt = 1
    ans = max(ans,cnt)

solv()
print(ans)