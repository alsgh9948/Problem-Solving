from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
MAX = 2001
START = 1000
n = int(input())

board = [[0]*MAX for _ in range(MAX)]
group_num = 1

def solv():
    input_data()

    set_group()

    if board[START][START] != 0:
        print(group_num-2)
    else:
        print(group_num-1)

def set_group():
    for x in range(MAX):
        for y in range(MAX):
            if board[x][y] == 1:
                bfs(x,y)
def bfs(sx,sy):
    global group_num, board
    group_num += 1
    q = deque([(sx,sy)])

    board[sx][sy] = group_num

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                board[nx][ny] = group_num
                q.appendleft((nx,ny))

def point_validator(x,y):
    if x < 0 or y < 0 or x >= MAX or y >= MAX:
        return False
    elif board[x][y] != 1:
        return False
    return True

def input_data():
    for _ in range(n):
        x1,y1,x2,y2 = map(lambda x:int(x)*2+1000, input().split())
        set_border(x1,y1,x2,y2)

def set_border(x1,y1,x2,y2):
    global board
    for x in range(x1,x2+1):
        board[x][y1] = 1
        board[x][y2] = 1

    for y in range(y1,y2+1):
        board[x1][y] = 1
        board[x2][y] = 1

solv()