from sys import stdin

input = stdin.readline
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]

r,c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

dest_board = [[() for _ in range(c)] for _ in range(r)]
answer_board = [[0]*c for _ in range(r)]
def solv():
    for sx in range(r):
        for sy in range(c):
            if not dest_board[sx][sy]:
                move_ball(sx,sy)
    for row in answer_board:
        print(*row)
def move_ball(x,y):
    global dest_board, answer_board
    target = board[x][y]
    tx,ty = -1,-1
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny,target):
            target = board[nx][ny]
            tx,ty = nx,ny
    if tx == -1:
        nx,ny = x,y
    else:
        if dest_board[tx][ty]:
            nx,ny = dest_board[tx][ty]
        else:
            nx,ny = move_ball(tx,ty)

    dest_board[x][y] = (nx,ny)
    answer_board[nx][ny] += 1
    return dest_board[x][y]

def point_validator(x,y,num):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    elif board[x][y] > num:
        return False

    return True
solv()