from sys import stdin
from itertools import product

dx = [-1,0,1,0]
dy = [0,1,0,-1]

input = stdin.readline

n = int(input())
origin_board = [list(map(int, input().split())) for _ in range(n)]
board = [[0]*n for _ in range(n)]
merge_status = [[0]*n for _ in range(n)]
merge_num = 0
def solv():
    global board,merge_num
    answer = 0
    for dirs in product(range(4),repeat=5):
        board = copy_board(origin_board,board)
        for dir in dirs:
            merge_num += 1
            find_location(dir)
        for row in board:
            answer = max(answer,max(row))
    print(answer)
def copy_board(src,dest):
    for x in range(n):
        for y in range(n):
            dest[x][y] = src[x][y]
    return dest
def find_location(dir):
    if dir == 0:
        for y in range(n):
            for x in range(1,n):
                move_block(dir,x,y)
    elif dir == 1:
        for x in range(n):
            for y in range(n-2,-1,-1):
                move_block(dir, x, y)
    elif dir == 2:
        for y in range(n):
            for x in range(n-2,-1,-1):
                move_block(dir,x,y)
    else:
        for x in range(n):
            for y in range(1,n):
                move_block(dir,x,y)

def move_block(dir,x,y):
    global board
    target = board[x][y]
    if target == 0:
        return
    board[x][y] = 0
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            board[x][y] = target
            return
        elif board[nx][ny] != 0:
            merge_block(dir,target,nx,ny)
            return
        x,y = nx,ny
def merge_block(dir,target,x,y):
    global board,merge_status
    if board[x][y] == target and merge_status[x][y] != merge_num:
        board[x][y] *= 2
        merge_status[x][y] = merge_num
    else:
        bx = x - dx[dir]
        by = y - dy[dir]
        board[bx][by] = target
solv()