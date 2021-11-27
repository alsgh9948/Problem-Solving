from sys import stdin
from collections import deque

input = stdin.readline
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

k = int(input())
n = k*4
board = [[[0]*n for _ in range(n)] for _ in range(n)]

origin_board = []
sx=sy=-1
for x in range(n):
    origin_board.append(input().strip())
    for y in range(n):
        if origin_board[x][y] == 'S':
            sx,sy = x,y
        for z in range(n):
            board[z][x][y] = origin_board[x][y]
def solv():
    set_board()
    print(simul())
def simul():
    q = deque([(sx,sy,0,0)])
    visited = [[[False]*n for _ in range(n)] for _ in range(n)]

    while q:
        x,y,t,cnt = q.pop()

        now_num = k*x//4+y//4
        nxt_cnt = now_num if cnt+1 == now_num+4 else cnt+1
        if board[cnt][x][y] == 'E':
            return t

        for d in range(5):
            nx = x + dx[d]
            ny = y + dy[d]

            nx, ny = ny,now_num+3-nx
            if point_validator(nx,ny,visited,cnt):
                visited[nx][ny][cnt] = True
                q.appendleft((nx,ny,t+1,nxt_cnt))

    return -1
def point_validator(x,y,visited,cnt):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y][cnt]:
        return False
    elif board[cnt][x][y] == '#':
        return False
    return True
def set_board():
    num = 0
    for x in range(0,n,4):
        for y in range(0,n,4):
            num += 1
            for _ in range(3):
                rotate_array(num,x,y)
                num += 1

def rotate_array(num,tsx,tsy):
    global board
    tex,tey = tsx+4,tsy+4
    for x in range(tsx,tex):
        for y in range(tsy,tey):
            board[num][y][tey-x-1] = board[num-1][x][y]
solv()