from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = []
for _ in range(n):
    row = []
    tmp = list(map(int, input().split()))

    for idx in range(m):
        a,b,c = tmp[idx*3:idx*3+3]
        row.append((a+b+c)/3)
    board.append(row)

t = int(input())
def solv():
    set_board()

    answer = 0
    for sx in range(n):
        for sy in range(m):
            if board[sx][sy] == 255:
                bfs(sx,sy)
                answer += 1

    print(answer)

def bfs(sx,sy):
    global board

    q = deque([(sx,sy)])
    board[sx][sy] = 0

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validatr(nx,ny):
                board[nx][ny] = 0
                q.appendleft((nx,ny))

def point_validatr(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == 0:
        return False
    return True

def set_board():
    global board
    for x in range(n):
        for y in range(m):
            board[x][y] = 255 if board[x][y] >= t else 0

solv()