from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

board = []
cheese = deque()
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] == 1:
            cheese.appendleft((x,y))

def solv():
    set_board()

    t = 0
    cnt = 0
    while cheese:
        cnt = len(cheese)
        remove_point = cheese_melt()
        remove_cheese(remove_point)
        t += 1
    print(t)
    print(cnt)
def set_board():
    global board

    for sx in range(n):
        for sy in range(m):
            if board[sx][sy] == 0:

                q = deque([(sx,sy)])
                board[sx][sy] = -1

                while q:
                    x,y = q.pop()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if point_validator(nx,ny):
                            board[nx][ny] = -1
                            q.appendleft((nx,ny))
                return

def cheese_melt():
    remove_point = []
    cheese_cnt = len(cheese)
    for _ in range(cheese_cnt):
        x,y = cheese.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny, False):
                board[x][y] = 2
                remove_point.append((x,y))
                break
        if board[x][y] == 1:
            cheese.appendleft((x,y))
    return remove_point

def remove_cheese(remove_point):
    global board
    for x,y in remove_point:
        board[x][y] = -1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                active_hole(x,y)
                break

def active_hole(sx,sy):
    global board
    q = deque([(sx,sy)])
    board[sx][sy] = -1

    while q:
        x,y = q.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                board[nx][ny] = -1
                q.appendleft((nx,ny))

def point_validator(x,y,flag = True):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif flag and board[x][y] != 0:
        return False
    elif not flag and board[x][y] != -1:
        return False
    return True

solv()