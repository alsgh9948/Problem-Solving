from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = [[0]*m for _ in range(n)]

k = int(input())
for _ in range(k):
    x,y = map(int, input().split())
    board[x][y] = -1

sx,sy = map(int, input().split())
op_list = list(map(int, input().split()))

def solv():
    global board
    op = 0
    x,y=sx,sy
    board[x][y] = 1
    while True:
        nx,ny,op = move_robot(x,y,op)
        if nx == -1:
            print(x,y)
            return
        x,y = nx,ny
        board[x][y] = 1
def move_robot(x,y,op):
    for _ in range(4):
        d = op_list[op]-1
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny):
            return nx,ny,op
        op = (op+1)%4
    return -1,-1,-1

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] != 0:
        return False
    return True

solv()