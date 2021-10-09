from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())

def solv():
    global board,m,n
    m,n,k = map(int, input().split())
    board = [[0]*m for _ in range(n)]
    for _ in range(k):
        y,x = map(int, input().split())
        board[x][y] = 1

    num = 2
    for sx in range(n):
        for sy in range(m):
            if board[sx][sy] == 1:
                bfs(sx,sy,num)
                num += 1

    print(num-2)

def bfs(sx,sy,num):
    global board

    q = deque([(sx,sy)])
    board[sx][sy] = num

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                board[nx][ny] = num
                q.appendleft((nx,ny))

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] != 1:
        return False
    return True
for _ in range(tc):
    solv()