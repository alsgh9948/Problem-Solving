from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
cheeses = deque()

board = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] == 1:
            cheeses.appendleft((x,y))

def solv():
    set_board()

    ans = 0
    while cheeses:
        ans += 1

        remove_cheese_point = melt_cheese()
        if remove_cheese_point:
            remove_cheese(remove_cheese_point)
    print(ans)

def set_board():
    global board
    q = deque([(0,0)])
    board[0][0] = 2

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny) and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.appendleft((nx,ny))

def melt_cheese():
    global cheeses
    cnt_cheese = len(cheeses)
    remove_cheese_point = []
    for _ in range(cnt_cheese):
        x,y = cheeses.pop()

        cnt = 0
        flag = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny):
                if board[nx][ny] == 2:
                    cnt += 1
                elif board[nx][ny] == 0:
                    flag = True

        if cnt >= 2:
            remove_cheese_point.append((x,y,flag))
        else:
            cheeses.appendleft((x,y))

    return remove_cheese_point

def remove_cheese(remove_chees_point):
    global board
    for x,y,flag in remove_chees_point:
        board[x][y] = 2
        if flag:
            renew_hole(x,y)
def renew_hole(sx,sy):
    global board
    q = deque([(sx,sy)])

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny) and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.appendleft((nx, ny))
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solv()